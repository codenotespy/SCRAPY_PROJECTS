# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    BRAND = scrapy.Field()
    PART_NO = scrapy.Field()
    DESCRIPTION = scrapy.Field()
    CROSS_REF = scrapy.Field()
    M_PRICE = scrapy.Field()
    REMAINDER = scrapy.Field()