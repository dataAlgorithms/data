#! *-* coding=utf-8 *-*

from scrapy.spiders import XMLFeedSpider
import scrapy 

class MySpider(XMLFeedSpider):
    name = 'example.com'
    allowed_domains = ['example.com']
    start_ursl = ['http://www.example.com/feed.xml']
    iterator = 'iternodes'
    itertag = 'item'

    def parse_node(self, response, node):
        self.logger.info('Hi, this is a <%s> node! %s', self.itertag, ''.join(node.extract()))

        item = scrapy.Item()
        item['id'] = node.xpath('@id').extract()
        item['name'] = node.xpath('name').extract()
        item['description'] = node.xpath('description').extract()
        return item
