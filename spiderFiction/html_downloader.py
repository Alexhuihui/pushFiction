from urllib import request
from fake_useragent import UserAgent
import ssl
import requests


class HtmlDownloader(object):
	def download(self, url):
		if url is not None:
			
			try:
				ssl._create_default_https_context = ssl._create_unverified_context
				
				ua = UserAgent()
				
				headers = {
					'User-Agent': ua.random
				}
				req = request.Request(url=url, headers=headers)
				
				response = request.urlopen(req, timeout=10)
				
				if response.getcode() == 200:
					r = requests.get(url)
					r.encoding = 'utf-8'
					return r.text
				
				else:
					return None
			
			except Exception as e:
				
				print(str(e))
		
		else:
			
			return None
