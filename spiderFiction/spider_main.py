from spiderFiction import html_downloader, html_parser, dao


class SpiderMain(object):
	def __init__(self):
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.dao = dao.Dao()
	
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
		print(url)
		html_content = self.downloader.download(url)
		data = self.parser.parse(url, html_content)
		# 遍历data
		for value in data.values():
			rs = self.dao.select_chapter(value)
			if rs[0][0] != 1:
				self.dao.insert_chapter(value)
				self.craw_content(value)
				self.send_email()
		
		data.clear()
	
	# 根据小说的章节地址爬取内容, 并存入到数据库中
	def craw_content(self, url):
		pass
		# html_content = self.downloader.download(url)
		# print(html_content)
		
	# 发送邮件
	def send_email(self):
		pass
	
	# 控制函数
	def main(self):
		urls = self.get_urls()
		for url in urls:
			self.get_chapter(url)


if __name__ == '__main__':
	obj_spider = SpiderMain()
	obj_spider.main()
