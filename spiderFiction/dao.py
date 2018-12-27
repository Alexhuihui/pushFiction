# -*- coding:utf-8 -*-
import pymysql
import time

from conf import readConfig

read = readConfig.ParserConfig()
path = "../conf/configParser.conf"


class Dao(object):
	
	def __init__(self):
		self.host = read.readValueFromPath(path, "db", "host")
		self.port = read.readIntValue(path, "db", "port")
		self.user = read.readValueFromPath(path, "db", "user")
		self.passwd = read.readValueFromPath(path, "db", "passwd")
		self.db = read.readValueFromPath(path, "db", "db")
		self.charset = read.readValueFromPath(path, "db", "charset")
	
	def get_conn(self):
		conn = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.passwd, db=self.db,
		                       charset=self.charset)
		return conn
	
	# 从novelinfo表中查出所有数据, 返回包含所有小说地址的集合
	def select_novel(self):
		select_sql = "select novel_id, novel_url, novel_name from novelinfo"
		novel_urls = []
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(select_sql)
			rs = cur.fetchall()
			for r in rs:
				novel_urls.append(r[1])
		except Exception as e:
			print(e)
			conn.rollback()
			
		return novel_urls
	
	# 向novelchapter表中插入数据
	def insert_chapter(self):
		pass
	
	# 从数据库里查询content并返回true或false，比对要存入的数据，保证数据不重复
	def select_check(self, data):
		select_sql = "select content from information where status = 0"
		content = ""
		flag = True
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(select_sql)
			rs = cur.fetchall()
			for r in rs:
				if (str(r[0]) == str(data)):
					flag = False
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
		return flag
	
	def insert(self, contents):
		createtimes = str(time.time())
		insert_sql = "insert into information(content, createtime) values('%s', '%s' ) " % (contents, createtimes)
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(insert_sql)
			conn.commit()
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
	
	def delete(self):
		pass
	
	def update(self):
		update_sql = "update information set status = 1 where status = 0"
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(update_sql)
			conn.commit()
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
	
	def select(self):
		select_sql = "select content from information where status = 0"
		content = ""
		list = []
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(select_sql)
			rs = cur.fetchall()
			for line in rs:
				list.append(line)
			for i in range(0, list.__len__()):
				list[i] = str(list[i])
			content = '\n'.join(list)
			conn.commit()
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
		self.update()
		return content
	
	def select_once_data(self):
		select_sql = "select content from information where status = 0"
		content = ""
		list = []
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(select_sql)
			rs = cur.fetchall()
			for line in rs:
				list.append(line)
			for i in range(0, list.__len__()):
				list[i] = str(list[i])
			content = '\n'.join(list)
			conn.commit()
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
		return content


if __name__ == '__main__':
	dao = Dao()
	dao.select_check("特斯拉涨幅扩大至5.5%。")
