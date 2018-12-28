import re

from bs4 import BeautifulSoup


class HtmlParser(object):
	def get_new_data(self, soup):
		res_data = []
		anodes = soup.find_all('p')
		for anode in anodes:
			res_data.append(anode.get_text())
		
		return res_data
	
	def parse(self, page_url, html_cont):
		if html_cont is None:
			return
		
		soup = BeautifulSoup(html_cont, features="html.parser")
		novel_id = page_url[-6:-1]
		
		for link in soup.find_all('a', href=re.compile("\d\.html")):
			chapter_title = link.get_text()
			chapter_url = page_url + link.get('href')[12:]
			chapter_id = link.get('href')[12:-5]
			
			
