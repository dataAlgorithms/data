# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class hacker_newsItem(Item):
    # define the fields for your item here like:
    res = Field()
    url = Field()
    title = Field()
    points = Field()
    people = Field()
    age = Field()
    comments = Field()
