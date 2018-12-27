from spiderFiction import url_manager, html_downloader, html_output, html_parser, dao


class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_output.HtmlOutputer()
		self.dao = dao.Dao()
		
	# 返回所有的小说的地址
	def get_urls(self):
		novel_urls = self.dao.select_novel()
		return novel_urls
	
	# 根据小说地址爬取小说的章节
	def craw_chapter(self, urls):
		count = 1
		self.urls.add_new_urls(urls)
		while self.urls.has_new_url():
			try:
				
				new_url = self.urls.get_new_url()
				
				print('craw %d : %s' % (count, new_url))
				
				html_cont = self.downloader.download(new_url)
				new_data = self.parser.parse(new_url, html_cont)
				for data in new_data:
					if (self.dao.select_check(str(data)) is True):
						self.dao.insert(data)
				self.outputer.collect_data(new_data)
				
				if count == 1:
					break
				
				count += 1
			
			except:
				print('craw failed')
		
		self.outputer.output_html()
	
	def craw_content(self, url):
		pass


if __name__ == '__main__':
	obj_spider = SpiderMain()
	obj_spider.get_urls()
