# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .videoDao import VideoDao

class NineonePipeline(object):
    def process_item(self, item, spider):
        return item


class VideoSaveToDbPipeline(object):

	def open_spider(self, spider):
		self.videoDao = VideoDao()

	def process_item(self, item, spider):
		print('==> recieve item ', item)
		self.videoDao.insertVideoToDb(item)