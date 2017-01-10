# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .simplesqltool import SQLAccess
from .videoDao import VideoDao
import requests

class VideoSaveToDbPipeline(object):

	def open_spider(self, spider):
		self.videoDao = VideoDao()

	def process_item(self, item, spider):
	# def process_item(self, item, spider):
		print('===> received item ', item)
		id = item.get('id')
		self.videoDao.insertVideoToDb(item)
		return item


class DownloadVidePipeline(object):
	def process_item(self, item, spider):
		pass
