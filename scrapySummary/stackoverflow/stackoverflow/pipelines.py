# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem
import json
from twisted.enterprise import adbapi    
from scrapy.utils.project import get_project_settings    
from scrapy import log
import pymongo
    
settings = get_project_settings() 

#MySql pipleline
'''
drop dabase if exists scrapy;
create databse scrapy;
use scrapy
CREATE TABLE items (title VARCHAR(10000),votes VARCHAR(100), body TEXT(4294967295), tag VARCHAR(100), link VARCHAR(10000));
'''
class MySqlPipeline(object):
    # The table you items.FundItem class map to, my table is named fund    
    insert_sql = """insert into items (%s) values ( %s )"""    
    
    def __init__(self):    
        dbargs = settings.get('DB_CONNECT')    
        db_server = settings.get('DB_SERVER')    

        dbpool = adbapi.ConnectionPool(db_server, **dbargs)    
        self.dbpool = dbpool 
    
    def __del__(self):    
        self.dbpool.close()    
    
    def process_item(self, item, spider):    
        self.insert_data(item, self.insert_sql)    
        return item    
    
    def insert_data(self, item, insert):    
        keys = item.fields.keys()    
        fields = u','.join(keys)    
        qm = u','.join([u'%s'] * len(keys))    
        sql = insert % (fields, qm)    
        data = [item[k] for k in keys]
        return self.dbpool.runOperation(sql, data)
    
# Drop pipeline
class DropPipeline:

    def process_item(self, item, spider):
        if item['link']:
            return item
        else:
            raise DropItem("Missing link in %s" % item)

# item modify pipleine, such, vote
class VotePipeline:
    
    vat_factor = 1.1
    def process_item(self, item, spider):
        if item['vote']:
            item['vote'] = item['vote'] * self.vat_factor
            return item
        else:
            raise DropItem("Missing vote in %s" % item)

# Json pipeline
class JsonWriterPipeline:

    def __init__(self):
        self.file = open('items.jl', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item
    
# Mongodb pipeline 
'''
mongod --dbpath "D:\MongoDB\data\db" --logpath "D:\MongoDB\data\log\MongoDB.log" --install --serviceName "MongoDB"
net start MongoDB
net stop MongoDB
mongod --dbpath "D:\Program Files\MongoDB\data\db" --logpath "D:\Program Files\MongoDB\data\log" --remove --serviceName "MongoDB"
'''
class MongoDBPipeline:
    def __init__(self):
        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )

        db = connection[settings.get('MONGODB_DB')]
        self.collection = db[settings.get('MONGODB_COLLECTION')]

    def process_item(self, item, spider):
        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))

        if valid:
            self.collection.insert(dict(item))
            log.msg("Question added to MongoDB database!",
                     level=log.DEBUG, spider=spider)
        return item        
    
# Duplicate pipeline 
class DuplicatesPipeline:

    def __init__(self):
        self.links_seen = set()

    def process_item(self, item, spider):
        if item['link'] in self.links_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.links_seen.add(item['link'])
            return item