from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').extract_first(),
                'author': quote.css('span small::text').extract_first(),
                'tags': quote.css('div.tags a.tag::text').extract(),
           }

        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
            
configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(QuotesSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished

'''
Result:
INFO: Enabled extensions: CloseSpider, TelnetConsole, LogStats, CoreStats, SpiderState
INFO: Enabled downloader middlewares: HttpAuthMiddleware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultHeadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMiddleware, CookiesMiddleware, ChunkedTransferMiddleware, DownloaderStats
INFO: Enabled spider middlewares: HttpErrorMiddleware, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
INFO: Enabled item pipelines: 
INFO: Spider opened
INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
DEBUG: Telnet console listening on 127.0.0.1:6023
DEBUG: Crawled (200) <GET http://quotes.toscrape.com/page/1/> (referer: None)
DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>

{'text': u'\u201cThe world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.\u201d', 'tags': [u'change', u'deep-thoughts', u'thinking', u'world'], 'author': u'Albert Einstein'}
DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>

{'text': u'\u201cIt is our choices, Harry, that show what we truly are, far more than our abilities.\u201d', 'tags': [u'abilities', u'choices'], 'author': u'J.K. Rowling'}
DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>

{'text': u'\u201cThere are only two ways to live your life. One is as though nothing is a miracle. The other is as though everything is a miracle.\u201d', 'tags': [u'inspirational', u'life', u'live', u'miracle', u'miracles'], 'author': u'Albert Einstein'}
DEBUG: Scraped from <200 http://quotes.toscrape.com/page/1/>


{'text': u'\u201c... a mind needs books as a sword needs a whetstone, if it is to keep its edge.\u201d', 'tags': [u'books', u'mind'], 'author': u'George R.R. Martin'}
INFO: Closing spider (finished)
INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 2646,
 'downloader/request_count': 10,
 'downloader/request_method_count/GET': 10,
 'downloader/response_bytes': 24492,
 'downloader/response_count': 10,
 'downloader/response_status_count/200': 10,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2016, 11, 1, 6, 26, 19, 747000),
 'item_scraped_count': 100,
 'log_count/DEBUG': 111,
 'log_count/INFO': 7,
 'request_depth_max': 9,
 'response_received_count': 10,
 'scheduler/dequeued': 10,
 'scheduler/dequeued/memory': 10,
 'scheduler/enqueued': 10,
 'scheduler/enqueued/memory': 10,
 'start_time': datetime.datetime(2016, 11, 1, 6, 26, 13, 968000)}
INFO: Spider closed (finished)

'''
