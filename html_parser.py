from bs4 import BeautifulSoup
import urlparse
import re
class HtmlParser(object):
	"""docstring for html_parser"""
	def __init__(self):
		pass

	def _get_new_urls(self,page_url,soup):
		new_urls = set()
		links = soup.find_all('a',href=re.compile(r"^http.?://mp.weixin.qq.com/s.*$"))
		for link in links:
			new_url = link['href']
			new_full_url = urlparse.urljoin(page_url,new_url)
			new_urls.add(new_full_url)
		return new_urls

	def _get_new_data(self,page_url,soup):
		res_data = {}
		res_data['url'] = page_url
		try:
			title_node = soup.find('h2',class_='rich_media_title')
		except AttributeError as e:
			return None

		try:
			res_data['title'] = title_node.get_text()
		except AttributeError as e:
			return None
		summary_node = soup.find('a',class_='rich_media_meta rich_media_meta_link rich_media_meta_nickname')
		try:
			res_data['summary'] = summary_node.get_text()
		except AttributeError as e :
			return None
		return res_data


	
	def parse(self,page_url,html_cont):
		if page_url is None or html_cont is None:
			return 
		soup =BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
		new_urls = self._get_new_urls(page_url,soup)
		new_data = self._get_new_data(page_url,soup)
		return new_urls,new_data
		