import scrapy
from dmoz.items import DmozItem

class DomzSpider(scrapy.Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/"
    ]

    def parse(self, response):
        for href in response.xpath('//section[@class="children"]/div/div[@class="cat-item"]/a/@href'):
            url = response.urljoin(href.extract())
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_as_file(self, response):
        filename = response.url.split("/")[-2] + '.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
            
    def parse_print(self, response):
        for sel in response.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]'):
            title = sel.xpath('a/div[@class="site-title"]/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('div[@class="site-descr "]/text()').extract()
            print title, link, desc

    def parse_contents(self, response):
        for sel in response.xpath('//div[@class="site-item "]/div[@class="title-and-desc"]'):
            item = DmozItem()
            item['title'] = sel.xpath('a/div[@class="site-title"]/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('div[@class="site-descr "]/text()').extract()
            yield item


