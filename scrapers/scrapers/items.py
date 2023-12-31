# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class ScrapersItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class WalmartScraperItem(Item):
    # define the fields for your item here like:
    keyword = Field()
    page = Field()
    position = Field()
    url = Field()
    id = Field()
    type = Field()
    name = Field()
    brand = Field()
    averageRating = Field()
    manufacturerName = Field()
    shortDescription = Field()
    thumbnailUrl = Field()
    price = Field()
    currencyUnit = Field()


class KohlScraperItem(Item):
    # define the fields for your item here like:
    keyword = Field()
    page = Field()
    name = Field()
    url = Field()
    price = Field()
    currencyUnit = Field()
    shortDescription = Field()
    position = Field()
    
    # id = Field()
    # type = Field()
    # brand = Field()
    # averageRating = Field()
    # manufacturerName = Field()
    # thumbnailUrl = Field()
    # price = Field()
    # currencyUnit = Field()

