# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from spiderFiction import dao, readConfig

read = readConfig.ParserConfig()
path = "configParser.conf"


class Sender(object):
	
	def __init__(self):
		self.mail_host = "smtp.163.com"  # SMTP服务器
		self.mail_user = "17770848782"  # 用户名
		self.mail_pass = "QWErty123" # 授权密码，非登录密码
		
		self.sender = "17770848782@163.com"
		self.receivers = ["2930807240@qq.com"]
		self.dao = dao.Dao()
	
	# 从数据库中查询数据并组合成字符串
	def select_data(self, novel_id, chapter_id):
		content = self.dao.select_content(int(novel_id), int(chapter_id))
		return content
	
	# 发送邮件
	def send_mail(self, novel_id, chapter_id, chapter_title):
		title = chapter_title
		content = self.select_data(novel_id, chapter_id)[0][0]
		message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
		message['From'] = "{}".format(self.sender)
		message['To'] = ",".join(self.receivers)
		message['Subject'] = title
		
		try:
			smtpObj = smtplib.SMTP_SSL(self.mail_host, 465)  # 启用SSL发信, 端口一般是465
			smtpObj.login(self.mail_user, self.mail_pass)  # 登录验证
			smtpObj.sendmail(self.sender, self.receivers, message.as_string())  # 发送
			print(title + "mail has been send successfully.")
		except smtplib.SMTPException as e:
			print(e)


if __name__ == '__main__':
	sender = Sender()
	sender.send_mail(30152, 1034424, "第二十九章 一举成名天下知（2）")
