from urllib import request
import ssl
import requests


class HtmlDownloader(object):
	def download(self, url):
		if url is not None:
			
			try:
				ssl._create_default_https_context = ssl._create_unverified_context
				
				headers = {
					'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2'
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
