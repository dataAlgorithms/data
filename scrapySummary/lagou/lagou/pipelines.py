# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json
import codecs
from collections import OrderedDict
from scrapy.conf import settings
import pymongo
import logging

class JsonWithEncodingPipeline(object):

    def __init__(self):
        self.file = codecs.open('lagouPosition.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(OrderedDict(item), ensure_ascii=False, sort_keys=False) + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        self.file.close()

class MongoDBPipeline:
    def __init__(self):
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )

        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_TABLE')]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        logging.warning("Insert successfully!")
        #log.msg("Question added to MongoDB database!", level=log.DEBUG, spider=spider)
        return item     