# -*- coding:utf-8 -*-
from spiderFiction import html_downloader, html_parser
downloader = html_downloader.HtmlDownloader()
parser = html_parser.HtmlParser()


url = "http://www.biquge.com.cn/book/36681/52529.html"

html_content = downloader.download(url)
print(parser.parse_content(url, html_content))
