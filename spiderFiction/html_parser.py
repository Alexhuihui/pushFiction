import re

from bs4 import BeautifulSoup


class HtmlParser(object):
	
	def __init__(self):
		self.new_data = {}
	
	def get_new_data(self, novel_id, chapter_title, chapter_url, chapter_id):
		chapter = []
		chapter.append(novel_id)
		chapter.append(chapter_url)
		chapter.append(chapter_id)
		chapter.append(chapter_title)
		
		self.new_data[chapter_id] = chapter
	
	def parse(self, page_url, html_cont):
		if html_cont is None:
			return
		
		soup = BeautifulSoup(html_cont, features="html.parser")
		novel_id = page_url[-6:-1]
		
		for link in soup.find_all('a', href=re.compile("\d\.html")):
			chapter_title = link.get_text()
			chapter_url = page_url + link.get('href')[12:]
			chapter_id = link.get('href')[12:-5]
			
			self.get_new_data(novel_id, chapter_title, chapter_url, chapter_id)
		
		return self.new_data
