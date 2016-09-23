#from http://snipplr.com/view/71354/pandora-for-food--crawl-yelp-for-personalized-recommendations/
# This is just a fun little script that acts like a Pandora for food.Its
# implementation is simplistic. You choose a set of restaurants on Yelp that you 
# like, and the script finds all reviewers that gave these restaurants 5 stars. You 
# trust these reviewers because they share your awesome taste in food. The script 
# then spits out all restaurants that these "trusted reviewers" also reviewed, and 
# their rating for each review.
 
# You would need a few additional lines of code to turn the scrapy output into a 
# sorted list of restaurants. For example, the code below will sort restaurants by 
# number 5 star reviews from "trusted reviewers":
# import pandas
# reviews = pandas.read_csv('scrapy_output.csv')
# fiveStarReviews = reviews[reviews['rating']==5]
# fiveStarReviews.restaurant.value_counts()
 
# There are countless ways you can improve on this. One obvious one is you would 
# want to normalize by total restaurant reviews. You would probably also want to 
# pull in restaurant category information.
 
# Happy food hunting!
 
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import re
 
from pandoraFood.items import Review
 
# url string components for reviewer pages
URL_BASE = 'http://www.yelp.com/user_details_reviews_self?userid='
FILTER_SETTINGS = '&review_filter=category&category_filter=restaurants'
 
# yelp unique url endings for each restaurant
RESTAURANTS = ['z-and-y-restaurant-san-francisco', \
               'koi-palace-daly-city', \
               'ino-sushi-san-francisco', \
               'blackwood-san-francisco-3']
 
def createRestaurantPageLinks(self, response):
   reviewsPerPage = 40
   hxs = HtmlXPathSelector(response)
   totalReviews = int(hxs.select('//h2[@id="total_reviews"]/text()').extract()[0].strip().split(' ')[0])
   pages = [Request(url=response.url + '?start=' + str(reviewsPerPage*(n+1)), \
                    callback=self.parse) \
            for n in range(totalReviews/reviewsPerPage)]
   return pages
 
def createReviewerPageLinks(self, response):
   reviewsPerPage = 10
   hxs = HtmlXPathSelector(response)
   totalReviews = int(hxs.select('//div[@id="review_lister_header"]/em/text()').extract()[0].split(' ')[0])
   pages = [Request(url=response.url + '&rec_pagestart=' + str(reviewsPerPage*(n+1)), \
                    callback=self.parseReviewer) \
            for n in range(totalReviews/reviewsPerPage)]
   return pages
 
class RestaurantSpider(BaseSpider):
   name = 'crawlRestaurants'
   allowed_domains = ['yelp.com']
   start_urls = [ 'http://www.yelp.com/biz/%s' % s for s in RESTAURANTS]
 
   # default parse used for the landing page for each start_url
   def parse(self, response):
      requests = []
 
      # extract all reviews from the page and return a list of requests for the 5 star reviewers' profiles
      hxs = HtmlXPathSelector(response)
      userIDs = [userUrl.split('?userid=')[1] for \
                 userUrl in hxs.select('//li[@class="user-name"]/a/@href').extract()]
      ratings = hxs.select('//div[@id="reviews-other"]//meta[@itemprop="ratingValue"]/@content').extract()
 
      for i in range(len(ratings)):
         if float(ratings[i]) == 5:
            requests.append(Request(url=URL_BASE + userIDs[i] + FILTER_SETTINGS, \
                                    callback=self.parseReviewer))
 
      # request additional pages if we are on page 1 of the restaurant
      if response.url.find('?start=') == -1:
         requests += createRestaurantPageLinks(self, response)
 
      return requests
 
   # parse a given reviewer
   def parseReviewer(self, response):
      hxs = HtmlXPathSelector(response)
      restaurantUrls = hxs.select('//div[@class="review clearfix"]/ \
                                  div[@class="biz_info"]/h4/a/@href').extract()
      restaurants = [re.search(r'(?<=/biz/)[^#]*', rest).group() for rest in restaurantUrls]
      reviewerName = hxs.select('//title/text()').extract()[0].split('|')[0].replace('\'s Profile','').strip()
      reviewerUserID = re.search(r'(?<=userid=)[^&]*', response.url).group()
      ratingText = hxs.select('//div[@class="rating"]/i/@title').extract()
      ratings = [s.replace(' star rating','') for s in ratingText]
 
      reviews = []
      for i in range(len(restaurants)):
         review = Review()
         review['restaurant'] = restaurants[i]
         review['reviewerName'] = reviewerName
         review['reviewerUserID'] = reviewerUserID
         review['rating'] = float(ratings[i])
         reviews.append(review)
 
      # request additional pages if we are on page 1 of the reviewer
      additionalPages = []
      if response.url.find('&rec_pagestart=') == -1:
         additionalPages = createReviewerPageLinks(self, response)
 
      return reviews + additionalPages
