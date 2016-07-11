#1. run a single spider from a script
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider(scrapy.Spider):
    # Spider definition
    pass

process = CrawlerProcess({
    'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
})
process.crawl(MySpider)
process.start()

#2. run a single spider from a script (inside a Scrapy project)
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

process = CrawlerProcess(get_project_settings())

# followall is the name of one of the spiders of the project
process.crawl('followall', domain='scrapinghub.com')
process.start() # the script will block here until the crawling is finished

#3. manually stop the reactor after MySpider has finished running
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider(scrapy.Spider):
    # Spider definition
    pass

configure_logging({'LOG_FORMAT': '%(levelname)s: %(message)s'})
runner = CrawlerRunner()

d = runner.crawl(MySpider)
d.addBoth(lambda _: reactor.stop())
reactor.run()

#4. run multiple spider simultaneously
import scrapy
from scrapy.crawler import CrawlerProcess

class MySpider1(scrapy.Spider):
    pass

class MySpider2(scrapy.Spider):
    pass

process = CrawlerProcess()
process.crawl(MySpider1)
process.crawl(MySpider2)
process.start()

#5. run multiple spiders simultaneouly (using crawlerRunner)
import scrapy
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider1(scrapy.Spider):
    pass

class MySpider2(scrapy.Spider):
    pass

configure_logging()
runner = CrawlerRunner()
runner.crawl(MySpider1)
runner.crawl(MySpider2)
d = runner.join()
d.addBoth(lambda _: reactor.stop()

reactor.run()

#6 running spiders sequentially by chaining the deferreds
from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

class MySpider1(scrapy.Spider):
    pass

class MySpider2(scrapy.Spider):
    pass

configure_logging()
runner = CrawlerRunner()

@defer.inlineCallbacks
def crawl():
    yield runner.crawl(MySpider1)
    yield runner.crawl(MySpider2)
    reactor.stop()

crawl()
reactor.run()

#7. avoid getting ban
'''
Here are some tips to keep in mind when dealing with these kinds of sites:
• rotate your user agent from a pool of well-known ones from browsers (google around to get a list of them)
• disable cookies (see COOKIES_ENABLED) as some sites may use cookies to spot bot behaviour
• use download delays (2 or higher). See DOWNLOAD_DELAY setting.
128 Chapter 5. Solving specific problems
Scrapy Documentation, Release 1.1.0
• if possible, use Google cache to fetch pages, instead of hitting the sites directly
• use a pool of rotating IPs. For example, the free Tor project or paid services like ProxyMesh
• use a highly distributed downloader that circumvents bans internally, so you can just focus on parsing clean
pages. One example of such downloaders is Crawlera
'''
