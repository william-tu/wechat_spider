import requests

class HtmlDownloader(object):
	"""docstring for html_downloader"""
	def __init__(self):
		pass
	
	def download(self,url):
		if url is None:
			return 
		headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.113 Safari/537.36',
						'Referer':url}
		response = requests.get(url,headers=headers)

		if response.status_code!=200:
			return None
		return response.content

		