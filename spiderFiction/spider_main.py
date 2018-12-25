from spiderFiction import url_manager, html_downloader, html_output, html_parser
import datetime
import time


class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_output.HtmlOutputer()
		self.dao = dao.Dao()
	
	def main(self, root_url, m=0, h=21):
		while True:
			now = datetime.datetime.now()
			print(now.hour, now.minute)
			# 每天晚上9点停止程序
			if now.minute == m and now.hour == h:
				break
				# 每隔60秒爬取一次
			time.sleep(60)
			self.craw(root_url)
	
	def craw(self, root_url):
		count = 1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				
				new_url = self.urls.get_new_url()
				self.urls.add_new_url(root_url)
				
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


if __name__ == '__main__':
	root_url = 'https://wallstreetcn.com/live/global'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
