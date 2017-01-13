# -*- coding: utf-8 -*-
import scrapy

from scrapy.selector import Selector
from scrapy.selector import Selector
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
import string
import traceback
from datetime import datetime
from browsermobproxy import Server
from subprocess import call
import os


class NineFavorSpider(scrapy.Spider):
	name = "ninefavor"
	allowed_domains = ["91porn.com"]
	start_urls = (
		'http://91porn.com/my_favour.php',
	)
	base_url = 'http://91porn.com//my_favour.php'
	cookies={'language':'cn_CN', '91username': 'ever0702', 'watch_times': 1, 'DUID': '67f7IczbX3rOJWM1%2BTJ1niTirxNnrgnCirQh9S2rZHO46qL7', '_cfduid': 'd397594c642c29164a9f574d83fee84071479932895', 'USERNAME': '0b6aKaCHUa4EDJinwvpiozEeCLj6XikgQebD3o6gfx%2FZI2LTpw', 'EMAILVERIFIED': 'yes'}

	def __init__(self):
		display = Display(visible=0, size=(1024, 768))
		display.start()
		self.driver = webdriver.Firefox()

	def start_requests(self):
		for url in self.start_urls:
			yield scrapy.Request(url, cookies=self.cookies)

	def parse(self, response):
		b=response.body

		videos = response.xpath('//div[@id="myvideo-content"]/div[contains(@class, "video")]')
		print(len(videos))
		for vid in videos:
			title = vid.xpath('.//strong/a/text()').extract_first()
			link = vid.xpath('.//strong/a/@href').extract_first()
			print(title, link)
			# yield scrapy.Request(link, callback=self.parse_page)
			self.download_video(link)


		next = response.xpath('//div[@id="paging"]//a[last()]/@href').extract_first()
		print(next)
		yield scrapy.Request(self.base_url + next, cookies=self.cookies)

	def download_video(self, url):
		os.chdir('/hdd/myporns/91favor');
		call(['youtube-dl', url])



		


