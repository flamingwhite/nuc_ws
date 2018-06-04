# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
import string
import traceback
from datetime import datetime
from urllib.parse import urlparse
from ..items import NineoneItem

class NineSpider(scrapy.Spider):
	name = "nine"
	allowed_domains = ["91porn.com"]
	start_urls = (
		'http://91porn.com/v.php?category=mf&viewtype=basic',
	)
	page_count = 0
	base_url = 'http://91porn.com/v.php'
	cookies={'language':'cn_CN'}

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url, cookies=self.cookies, meta={'cookiejar': 1})

	def getviewkey(self, url):
		o = urlparse(url).query.split('&')
		return [i.split('=')[1] for i in o if 'viewkey' in i][0]


	def parse(self, response):
		videos = response.xpath('//div[@class="listchannel"]')
		for vid in videos:
			url = vid.xpath('./a[@target="blank"]/@href').extract_first()
			title = vid.xpath('./a[@target="blank"]/@title').extract_first()
			viewkey = self.getviewkey(url)

			yield NineoneItem(viewkey=viewkey, title=title, url=url, done=False)

			print(title, url, viewkey)

		next = response.xpath('//div[@id="paging"]//a[last()]/@href').extract_first()
		print(next)
		self.page_count += 1
		if(self.page_count < 150):
			yield scrapy.Request(self.base_url + next, cookies=self.cookies)
