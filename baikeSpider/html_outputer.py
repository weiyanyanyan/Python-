import codecs
class HtmlOutputer(object):
	"""docstring for HtmlOutputer"""
	def __init__(self):
		self.datas=[]

	def collect_data(self,data):
		if data is None:
			return
		self.datas.append(data)

	def output_html(self):
		print("outS")
		font=codecs.open('output.html','w','utf-8')

		font.write("<html>")
		font.write("<head>")
		font.write("<meta charset='utf-8'>")
		font.write("</head>")
		font.write("<body>")
		font.write("<table>")

		for data in self.datas:
			font.write("<tr>")
			font.write("<td>%s</td>"%data['url'])
			font.write("<td>%s</td>"%data['title'].encode('utf-8').decode())
			font.write("<td>%s</td>"%data['summary'].encode('utf-8').decode())
			font.write("</tr>")

		font.write("</table>")
		font.write("</body>")
		font.write("</html>")
		font.close()
		
		