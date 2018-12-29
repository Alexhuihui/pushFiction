import re

from bs4 import BeautifulSoup


class HtmlParser(object):
	
	def __init__(self):
		self.chapter_data = {}
	
	# 把章节的信息组装到dict中
	def get_chapter_data(self, novel_id, chapter_title, chapter_url, chapter_id):
		chapter = []
		chapter.append(novel_id)
		chapter.append(chapter_url)
		chapter.append(chapter_id)
		chapter.append(chapter_title)
		
		self.chapter_data[chapter_id] = chapter
	
	# 解析章节列表页面
	def parse(self, page_url, html_cont):
		if html_cont is None:
			return
		
		soup = BeautifulSoup(html_cont, features="html.parser")
		novel_id = page_url[-6:-1]
		
		for link in soup.find_all('a', href=re.compile("\d\.html")):
			chapter_title = link.get_text()
			chapter_url = page_url + link.get('href')[12:]
			chapter_id = link.get('href')[12:-5]
			
			self.get_chapter_data(novel_id, chapter_title, chapter_url, chapter_id)
		
		return self.chapter_data
	
	# 解析文章内容页面
	def parse_content(self, page_url, html_cont):
		if html_cont is None:
			return
		
		soup = BeautifulSoup(html_cont, features="html.parser")
		chapter_content = soup.find("div", id="content")
		text = ""
		for row in chapter_content.strings:
			text += row + "\n"
		
		return self.process_text(text)

	# 处理正文的缩进和换行
	def process_text(self, text):
		c = re.compile(r"^\s")
		v_text = text
		v_text = c.sub("\n", v_text)
		v_text = v_text.replace("\xa0", "")  # 清除缩进
		v_text = v_text.replace("\u3000", "")  # 清除缩进
		v_text = v_text.replace("\r", "\n")  #
		v_text = v_text.replace("\n \n", "\n")  # 清除多余换行
		v_text = v_text.replace("select", "elect")
		v_text = v_text.replace("insert", "inset")
		v_text = v_text.replace("'", "(单引号)")
		v_text = v_text.replace('"', '(双引号)')
		while "\n\n" in v_text:
			v_text = v_text.replace("\n\n", "\n")  # 清除多余换行
		return v_text
