# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class VideoItem(Item):
    id = Field()
    uploadtime = Field()
    username = Field()
    title = Field()
    scrapytime = Field()
    videourl = Field()
