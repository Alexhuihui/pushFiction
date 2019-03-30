import time, datetime

from spiderFiction import html_downloader, html_parser, dao, sendEmail


class SpiderMain(object):
	def __init__(self):
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.dao = dao.Dao()
		self.send = sendEmail.Sender()
	
	# 返回所有的小说的地址
	def get_urls(self):
		novel_urls = self.dao.select_novel()
		return novel_urls
	
	"""
	根据单个的小说地址获取该本书所有的章节地址,
	如果是新的章节则存入到数据库中, 同时调用craw_content()函数，
	并发送邮件
	"""
	
	def get_chapter(self, url):
		# 根据URL查询对应的status字段如果为0代表是新增加的，就不进行发送邮件，调用get_new_chapter
		if self.dao.select_new_novel(url) == 0:
			self.get_new_chapter(url)
			self.dao.put_novel_status(url)
			return
		print(url)
		html_content = self.downloader.download(url)
		data = self.parser.parse(url, html_content)
		# 遍历data
		for value in data.values():
			rs = self.dao.select_chapter(value)
			if rs[0][0] != 1:
				time.sleep(200)
				self.dao.insert_chapter(value)
				self.craw_content(value)
				self.send_email(value)
		
		data.clear()
	
	# 获取新增加的小说的所有章节目录并存入novelchapter表中，但不会爬取章节的具体内容以及发送邮件
	def get_new_chapter(self, url):
		html_content = self.downloader.download(url)
		data = self.parser.parse(url, html_content)
		# 遍历data
		for value in data.values():
			rs = self.dao.select_chapter(value)
			if rs[0][0] != 1:
				self.dao.insert_chapter(value)
		
		data.clear()
	
	# 根据小说的章节地址爬取内容, 并存入到数据库中
	def craw_content(self, value):
		url = value[1]
		html_content = self.downloader.download(url)
		chapter_content = self.parser.parse_content(url, html_content)
		self.dao.insert_content(value, chapter_content)
	
	# 发送邮件
	def send_email(self, value):
		self.send.send_mail(value[0], value[2], value[3])
	
	# 控制函数
	def main(self):
		while True:
			now = datetime.datetime.now()
			urls = self.get_urls()
			for url in urls:
				self.get_chapter(url)
			print(now.year, '-', now.month, '-', now.day, '  ', now.hour, ':', now.minute)
			time.sleep(60)


if __name__ == '__main__':
	obj_spider = SpiderMain()
	obj_spider.main()
