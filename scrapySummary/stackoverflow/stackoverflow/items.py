# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class StackoverflowItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    votes = scrapy.Field()
    body = scrapy.Field()
    tag = scrapy.Field()
    link = scrapy.Field()
