#!/usr/bin/env python
# coding: utf-8
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import re
class HtmlParser(object):
    def _get_new_urls(self,page_url,soup):
    	print("ParserUrlS")
    	new_urls=set()
    	links = soup.find_all('a',href=re.compile(r'^/item/'))
    	print("ParserUrlM")
    	print(links)
    	for link in links: 
    		new_url=link['href']
    		print("urlS")
    		#ptint(link)
    		new_full_url=urljoin(page_url,new_url)
    		print(new_full_url)
    		print("urlE")
    		new_urls.add(new_full_url)
    	print("parserUrlOver")
    	return new_urls

    def _get_new_data(self,page_url,soup):
    	res_data={}
    	res_data['url']=page_url
    	title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find("h1")
    	res_data['title'] = title_node.get_text()
    	print(res_data)
    	summary_node = soup.find('div',class_='lemma-summary')
    	res_data['summary'] = summary_node.get_text()
    	#if summary_node is None:
    	#	print('ssssss')
    	#print(res_data)
    	return res_data


    def parser(self, page_url,html_cont):
    	print("parser")
    	print(page_url)
    	if page_url is None or html_cont is None:
    		return
    	print("soupS")
    	soup=BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')
    	print("soupE")
    	#print(page_url)
    	new_urls=self._get_new_urls(page_url,soup)
    	new_data=self._get_new_data(page_url,soup)
    	return new_urls,new_data
		