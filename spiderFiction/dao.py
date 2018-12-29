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
	def insert_chapter(self, chapter_list):
		createtime = str(time.time())
		insert_sql = "insert into novelchapter(novel_id, chapter_url, chapter_real_id, chapter_title, createtime) values('%d', '%s', '%d', '%s', '%s' ) " % (
			int(chapter_list[0]), chapter_list[1], int(chapter_list[2]), chapter_list[3], createtime)
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
	
	# 从novelchapter表中差寻是否包含某条记录
	def select_chapter(self, chapter_list):
		select_sql = "select COUNT(*) from novelchapter where novel_id = '%d' and chapter_real_id = '%d' " % (
			int(chapter_list[0]), int(chapter_list[2]))
		rs = 0
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(select_sql)
			rs = cur.fetchall()
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
		return rs
	
	# 把章节内容插入到novelchapterdetail表中
	def insert_content(self, value, chapter_text):
		createtime = str(time.time())
		insert_sql = "insert into `novelchapterdetail`(`novel_id`, `chapter_id`, `content_url`, `title`, `content`, `createtime`) values('%d', '%d', '%s', '%s', '%s', '%s' ) " % (
			int(value[0]), int(value[2]), value[1], value[3], str(chapter_text), createtime)
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(insert_sql)
			conn.commit()
		except Exception as e:
			print(value[1])
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
	
	# 从novelchapterdetail表中查询小说内容
	def select_content(self, novel_id, chapter_id):
		select_sql = "select content from novelchapterdetail where novel_id = '%d' and chapter_id = '%d'" % (
			novel_id, chapter_id)
		try:
			conn = self.get_conn()
			cur = conn.cursor()
			cur.execute(select_sql)
			rs = cur.fetchall()
		except Exception as e:
			print(e)
			conn.rollback()
		cur.close()
		conn.close()
		return rs


if __name__ == '__main__':
	dao = Dao()
	dao.select_check("特斯拉涨幅扩大至5.5%。")
