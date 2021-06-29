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
        # BRAND = response.css('span::text')[1].getall()
        PART_NO = response.css('.sku span::text').extract()
        DESCRIPTION = response.css('h1::text').extract()
        PRICE = response.css('div .fiyat span::text')[0].getall()

        # items['BRAND'] = BRAND
        items['PART_NO'] = PART_NO
        items['DESCRIPTION'] = DESCRIPTION
        items['PRICE'] = PRICE
        items['CUR_URL'] = [response.request.url]
        
        yield items