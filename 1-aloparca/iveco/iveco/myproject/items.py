# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    BRAND = scrapy.Field()
    PART_NO = scrapy.Field()
    CROSS_BRAND = scrapy.Field()
    CROSS_PART = scrapy.Field()
    LINK = scrapy.Field()