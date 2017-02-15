
# coding:utf-8

class HtmlOutputer(object):
	"""docstring for html_outputer"""
	def __init__(self):
		self.datas = []
	def collect_data(self,data):
		if data is None:
			return 
		self.datas.append(data)

	def output_html(self):
		fout = open('output.html','w')
		fout.write("<html><head><meta charset='utf-8'></head>")
		fout.write('<body>')
		for data in self.datas:
			fout.write('公众号：<h3>  %s  </h3>' % data['summary'].encode('utf-8'))
			fout.write("标题：<p>  %s  </p><br><br>" % data['title'].encode('utf-8'))

		fout.write('</body>')


		fout.write('</html>')
		fout.close()


		