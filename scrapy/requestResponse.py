1. cookies concerned
//Using a dict
request_with_cookies = Request(url="http://www.example.com",
                               cookies={'currency':'USD', 'country': 'UY'})

//Using a list of dicts
request_with_cookies = Request(url="http://www.example.com",
                               cookies=[{'name': 'currency',
                                         'value': 'USD',
                                         'domain': 'example.com',
                                         'path': '/currency'}])

//Request without merging cookies
request_with_cookies = Request(url="http://www.example.com",
                               cookies={'currency':'USD', 'country':'UY'},
                               meta={'dont_merge_cookies': True})

2. Pass additional data to callback functions
//default use
def parse_page1(self, response):
    return scrapy.Request("http://www.example.com/some_page.html",
                          callback=self.parse_page2)

def parse_page2(self, response):
    self.logger.info("Visited %s", response.url)

//pass argument to callback
def parse_page1(self, response):
    item = MyItem()
    item['main_url'] = response.url
    request = scrapy.Request("http://www.example.com/some_page.html",
                             callback=self.parse_page2)
    request.meta['item'] = item
    return request

def parse_page2(self, response):
    item = response.meta['item']
    item['other_url'] = response.url
    return item

3. Using errbacks to catch exceptions in request processing
import scrapy

from scrapy.spidermiddlewares.httperror import HttpError
from twisted.internet.error import DNSLookupError
from twisted.internet.error import TimeoutError, TCPTimedOutError

class ErrbackSpider(scrapy.Spider):
    name = "errback_example"
    start_urls = [
        "http://www.httpbin.org/",
        "http://www.httpbin.org/status/404",
        "http://www.httpbin.org/status/500",
        "http://www.httpbin.org:12345",
        "http://www.httphttpbinbin.org",
    ]

    def start_requests(self):
        for u in self.start_urls:
            yield scrapy.Request(u, callback=self.parse_httpbin,
                                    errback=self.errback_httpbin,
                                    dont_filter=True)

    def parse_httpbin(self, response):
        self.logger.info('Got successful response from {}'.format(response.url))

    def errback_httpbin(self, failure):
        # log all failures
        self.logger.error(repr(failure))

        # in case you want do something special for some errors
        # you may need the failure's type
        if failure.check(HttpError):
            response = failure.value.response
            self.logger.error('HttpError on %s', response.url)

        elif failure.check(DNSLookupError):
            request = failure.request
            self.logger.error("DNSLookupError on %s', request.url)

        elif failure.check(TimeoutError, TCPTimedOutError):
            request = failure.request
            self.logger.error('TimeoutError on %s', request.url)

4. Using FormRequest to send data via HTTP POST
return [FormRequest(url="http://www.example.com/post/action",
                    formdata={'name':"John Doe', 'age': '27'},
                    callback=self.after_post)]

5. Using FormRequest to simulate a user login
import scrapy

class LoginSpider(scrapy.Spider):
    name = 'example.com'
    start_urls = ['http://www.example.com/users/login.php']

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata={'username':'john', 'password':'secret'},
            callback=self.after_login
        )

    def after_login(self, response):
        if "authentication failed" in response.body:
            self.logger.error("login failed")
            return

        # continue scraping with authenticated session

