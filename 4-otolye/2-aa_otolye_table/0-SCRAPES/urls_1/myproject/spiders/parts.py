import scrapy
from myproject.items import MyprojectItem

import sys
sys.path.append('../../')
from variables import *

#from scrapy.contrib.loader import ItemLoader
#from scrapy.contrib.loader.processor import Join
#from scrapy.loader import ItemLoader

class PartsSpider(scrapy.Spider):
    name = 'parts'
    with open("../../0-URLS/" + brand + ".txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]
        print(start_urls)


    def parse(self, response):
        items = MyprojectItem()
        # BRAND = response.css('.breadcrumb li:nth-child(4) span::text').extract()
        PART_NO = response.css('.breadcrumb li:nth-child(4) span::text').extract()
        PRICE = response.css('.product-price::text')[0].getall()
        CROSS_PART = response.css('.product-info-list li:nth-last-child(3)::text').extract()

        # items['BRAND'] = BRAND
        items['PART_NO'] = PART_NO
        items['PRICE'] = PRICE
        items['CROSS_PART'] = CROSS_PART
        items['CUR_URL'] = [response.request.url]
        
        yield items