import url_manager,html_downLoader,html_parser,html_outputer
class SpiderMain(object):
	def __init__(self):
		print ("value")
		self.urls=url_manager.UrlManager()
		self.downloader=html_downLoader.HtmlDownLoader()
		self.parser=html_parser.HtmlParser()
		self.outputer=html_outputer.HtmlOutputer()

	def craw(self,root_url):

		count =1
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				new_url=self.urls.get_new_url()
				print ('craw %d: %s' % (count,new_url))
				print("overOne")
				html_cont=self.downloader.downLoad(new_url)
				print("overTwo")
				new_urls,new_data=self.parser.parser(new_url,html_cont)
				print("overThree")
				#print(new_data)
				self.urls.add_new_urls(new_urls)
				print("ddddd")
				self.outputer.collect_data(new_data)
				print("overFour")
				if count==10:
					break
				count=count+1
			except:
			    print ('craw failed')
		self.outputer.output_html()
		print(count)

if __name__=="__main__":
	print('vvv')
	root_url="https://baike.baidu.com/item/Python/407313"
	obj_spider=SpiderMain()
	obj_spider.craw(root_url)