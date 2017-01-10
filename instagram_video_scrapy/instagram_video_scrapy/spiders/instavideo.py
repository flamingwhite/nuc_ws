# -*- coding: utf-8 -*-
import scrapy
from ..items import VideoItem

from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyvirtualdisplay import Display
import time
import string
import traceback
from datetime import datetime

from ..videoDao import VideoDao


class User:
	def __init__(self, name, folder = None):
		self.name = name
		self.folder = name if folder is None else folder
		self.url = 'http://www.instagram.com/' + self.name
		print(self.folder)


# users = [User('fun_bestvids')];
users = [User('fun_bestvids'), User('bestvines'), User('lol_vines'), User('bestvidsnow'), User('epicfunnypage'), User('factsdailyy'), User('clips')];

class InstavideoSpider(scrapy.Spider):
	name = "instavideo"
	allowed_domains = ["instagram.com"]
	base_url="instagram.com"
	start_urls = (u.url for u in users)

	def __init__(self):
		display = Display(visible=0, size=(1024, 768))
		display.start()
		self.driver = webdriver.Firefox()
		self.adriver = webdriver.Firefox()
		self.lastid = None
		self.videoDao = VideoDao()

	def parse(self, response):
		# d = self.driver
		d = webdriver.Firefox()
		print(response.url)
		d.get(response.url)

		more = d.find_element_by_class_name('_oidfu')
		more.click()

		print('\n\n get into parse fun')

		lastid = None

		nodup = True

		while nodup is True:
			print('======> has more item to crawl\n\n\n')
			d.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			time.sleep(4)

			print('----\n\n getinto process-page \n\n')
			selec = Selector(text=d.page_source)
			vids = selec.xpath('//a[contains(@class, "_8mlbc")]/@href').extract()
			print('--> size of vids before ', len(vids))
			# print('\n\n--->before lastid, vids', vids)

			print('\n\n lastid is before process is =====> ',lastid, )
			templast = vids[len(vids)-1]

			if lastid is not None:
				vids = vids[vids.index(lastid) + 1: ]
				print('--> size of vids after, ', len(vids))

			lastid = templast

			print('\n\n lastid is =====> ',lastid, )

			print('\n\nafter lastid, vids is ', vids)


			print('before link for loop \n')

			if len(vids) is 0:
				nohup = False
				break

			for link in vids:
				try:
					print('\n======link is ', link)
					videoid = link.split('/')[2]
					vpage = self.adriver.get('https://'+self.base_url + link)
					self.adriver.find_element_by_class_name('_c2kdw').click()
					source=Selector(text=self.adriver.page_source)
					videourl=source.xpath('//video/@src').extract_first()
					title = source.xpath('//li[@class="_nk46a"]//span/text()').extract_first()
					rawtime = source.xpath('//time[@class="_379kp"]/@datetime').extract_first()
					uploadtime = datetime.strptime(rawtime, "%Y-%m-%dT%H:%M:%S.%fZ")
					userid = source.xpath('//a[contains(@class, "_4zhc5")]/text()').extract_first()


					print(videourl, title, videoid, time, uploadtime)
					if self.videoDao.videoIdExists(videoid):
						print('\n\nthis videoid exist', id)
						nodup = False
						break
					else:
						print('------>\n\ndontfond this id', videoid)
						yield VideoItem(id=videoid, uploadtime=uploadtime, title=title, videourl=videourl, username=userid)

				except Exception as e:
					print('\n\n\n\nException happend', e, '\n\n\n\n')
					traceback.print_exc()
					# break


	def finished(self, ids):
		pass











