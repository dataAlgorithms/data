# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class ZhihuItem(scrapy.Item):

    title = scrapy.Field()
    answer = scrapy.Field()
    link = scrapy.Field()
