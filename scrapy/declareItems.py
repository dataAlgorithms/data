# declare items
import scrapy
from scrapy.loader import ItemLoader

class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)
    
# extend items
class DiscountedProduct(Product):
    discount_percent = scrapy.Field(serialize=str)
    discount_expiration_date = scrapy.Field()

class SpecificProduct(Product):
    name = scrapy.Field(Product.fields['name'], serializer=my_serializer)
