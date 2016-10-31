from scrapy.spider import Spider
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

'''
Running history

D:\eclipse\workspace\LearnScrapy\spiders>scrapy runspider getFailedUrl.py
2016-10-31 18:10:19 [scrapy] INFO: Scrapy 1.0.3 started (bot: scrapybot)
2016-10-31 18:10:19 [scrapy] INFO: Optional features available: ssl, http11
2016-10-31 18:10:19 [scrapy] INFO: Overridden settings: {}
2016-10-31 18:10:19 [py.warnings] WARNING: D:\eclipse\workspace\LearnScrapy\spid
ers\getFailedUrl.py:1: ScrapyDeprecationWarning: Module `scrapy.spider` is depre
cated, use `scrapy.spiders` instead
  from scrapy.spider import Spider

2016-10-31 18:10:19 [scrapy] INFO: Enabled extensions: CloseSpider, TelnetConsol
e, LogStats, CoreStats, SpiderState
2016-10-31 18:10:19 [scrapy] INFO: Enabled downloader middlewares: HttpAuthMiddl
eware, DownloadTimeoutMiddleware, UserAgentMiddleware, RetryMiddleware, DefaultH
eadersMiddleware, MetaRefreshMiddleware, HttpCompressionMiddleware, RedirectMidd
leware, CookiesMiddleware, ChunkedTransferMiddleware, DownloaderStats
2016-10-31 18:10:19 [scrapy] INFO: Enabled spider middlewares: HttpErrorMiddlewa
re, OffsiteMiddleware, RefererMiddleware, UrlLengthMiddleware, DepthMiddleware
2016-10-31 18:10:19 [scrapy] INFO: Enabled item pipelines:
2016-10-31 18:10:19 [scrapy] INFO: Spider opened
2016-10-31 18:10:19 [scrapy] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 i
tems (at 0 items/min)
2016-10-31 18:10:19 [scrapy] DEBUG: Telnet console listening on 127.0.0.1:6023
2016-10-31 18:10:20 [scrapy] DEBUG: Crawled (200) <GET http://www.example.com> (
referer: None)
2016-10-31 18:10:20 [scrapy] DEBUG: Crawled (404) <GET http://www.example.com/th
isurldoesnotexist.html> (referer: None)
2016-10-31 18:10:29 [scrapy] DEBUG: Crawled (404) <GET http://www.example.com/ne
itherdoesthisone.html> (referer: None)
2016-10-31 18:10:29 [scrapy] INFO: Closing spider (finished)
2016-10-31 18:10:29 [scrapy] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 686,
 'downloader/request_count': 3,
 'downloader/request_method_count/GET': 3,
 'downloader/response_bytes': 2863,
 'downloader/response_count': 3,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/404': 2,
 'failed_url_count': 2,
 'failed_urls': 'http://www.example.com/thisurldoesnotexist.html,http://www.exam
ple.com/neitherdoesthisone.html',
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2016, 10, 31, 10, 10, 29, 229000),
 'log_count/DEBUG': 4,
 'log_count/INFO': 7,
 'response_received_count': 3,
 'scheduler/dequeued': 3,
 'scheduler/dequeued/memory': 3,
 'scheduler/enqueued': 3,
 'scheduler/enqueued/memory': 3,
 'start_time': datetime.datetime(2016, 10, 31, 10, 10, 19, 399000)}
2016-10-31 18:10:29 [scrapy] INFO: Spider closed (finished)
'''
class MySpider(Spider):
    handle_httpstatus_list = [404] 
    name = "myspider"
    allowed_domains = ["example.com"]
    start_urls = [
        'http://www.example.com',
        'http://www.example.com/thisurldoesnotexist.html',
        'http://www.example.com/neitherdoesthisone.html'
    ]

    def __init__(self, category=None):
        self.failed_urls = []
        # the dispatcher is now called in init
        dispatcher.connect(self.handle_spider_closed,signals.spider_closed) 

    def parse(self, response):
        if response.status == 404:
            self.crawler.stats.inc_value('failed_url_count')
            self.failed_urls.append(response.url)

    def handle_spider_closed(self, spider, reason): # added self 
        self.crawler.stats.set_value('failed_urls',','.join(spider.failed_urls))

    def process_exception(self, response, exception, spider):
        ex_class = "%s.%s" % (exception.__class__.__module__,  exception.__class__.__name__)
        self.crawler.stats.inc_value('downloader/exception_count', spider=spider)
        self.crawler.stats.inc_value('downloader/exception_type_count/%s' % ex_class, spider=spider)
