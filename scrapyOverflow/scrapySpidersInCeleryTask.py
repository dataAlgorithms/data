'''

accepted
Okay here is how I got Scrapy working with my Django project that uses Celery for queuing up what to crawl. The actual workaround came primarily from joehillen's code located here http://snippets.scrapy.org/snippets/13/

First the tasks.py file

from celery import task

@task()
def crawl_domain(domain_pk):
    from crawl import domain_crawl
    return domain_crawl(domain_pk)
Then the crawl.py file

from multiprocessing import Process
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings
from spider import DomainSpider
from models import Domain

class DomainCrawlerScript():

    def __init__(self):
        self.crawler = CrawlerProcess(settings)
        self.crawler.install()
        self.crawler.configure()

    def _crawl(self, domain_pk):
        domain = Domain.objects.get(
            pk = domain_pk,
        )
        urls = []
        for page in domain.pages.all():
            urls.append(page.url())
        self.crawler.crawl(DomainSpider(urls))
        self.crawler.start()
        self.crawler.stop()

    def crawl(self, domain_pk):
        p = Process(target=self._crawl, args=[domain_pk])
        p.start()
        p.join()

crawler = DomainCrawlerScript()

def domain_crawl(domain_pk):
    crawler.crawl(domain_pk)
The trick here is the "from multiprocessing import Process" this gets around the "ReactorNotRestartable" issue in the Twisted framework. So basically the Celery task calls the "domain_crawl" function which reuses the "DomainCrawlerScript" object over and over to interface with your Scrapy spider. (I am aware that my example is a little redundant but I did do this for a reason in my setup with multiple versions of python [my django webserver is actually using python2.4 and my worker servers use python2.7])

In my example here "DomainSpider" is just a modified Scrapy Spider that takes a list of urls in then sets them as the "start_urls".

Hope this helps!

http://stackoverflow.com/questions/11528739/running-scrapy-spiders-in-a-celery-task
'''
