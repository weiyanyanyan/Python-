import urllib.request
class HtmlDownLoader(object):
	"""docstring for Html_downLoader"""
	def downLoad(self,url):
		if url is None:
			return None
		print(url)
		res=urllib.request.urlopen(url)
		print(res.status)
		if res.status!=200:
			return None
		return res.read()