#! coding=utf-8 

import scrapy
from datetime import timedelta, date
from nos.items import NosItem

def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)

start_date = date(2015, 8, 19)
end_date = date(2015, 8, 20)
nos_urls = []
for single_date in daterange(start_date, end_date):
    nos_urls.append(single_date.strftime("http://nos.nl/nieuws/archief/%Y-%m-%d"))


class NosSpider(scrapy.Spider):
    name = "nos"
    allowed_domains = ["nos.nl"]

    start_urls = nos_urls

    def parse(self, response):
        for sel in response.xpath('//*[@id="archief"]/ul/li'):
            item = NosItem()
            item['name'] = sel.xpath('a/@href').extract()[0]
            item['date'] = sel.xpath('a/div[1]/time/@datetime').extract()[0]
            item['desc'] = sel.xpath('a/div[@class="list-time__title link-hover"]/text()').extract()[0]
            url = response.urljoin(item['name'])
            request = scrapy.Request(url, callback=self.parse_dir_contents)
            request.meta['item'] = item
            yield request


    def parse_dir_contents(self, response):
        for sel in response.xpath('//*[@id="content"]/article'):
            item = response.meta['item']
            textdata = sel.xpath('section//text()').extract()
            #textdata = " ".join(textdata)
            #textdata = textdata.replace("\n", "")
            #textdata = textdata.strip(' \t\n\r\\n')
            textdata = " ".join(map(unicode.strip,textdata)) # remove \t\n\r and space
            item['article'] = textdata
            yield item