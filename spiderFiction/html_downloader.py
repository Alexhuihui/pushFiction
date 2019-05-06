from urllib import request
import ssl
import requests


class HtmlDownloader(object):
	def download(self, url):
		if url is not None:
			
			try:
				ssl._create_default_https_context = ssl._create_unverified_context
				
				headers = {
					'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36'
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
