import scrapy
from myproject.items import MyprojectItem

#from scrapy.contrib.loader import ItemLoader
#from scrapy.contrib.loader.processor import Join
#from scrapy.loader import ItemLoader

class PartsSpider(scrapy.Spider):
    name = 'parts'
    page_number = 2
    with open("../../urls/urls_2.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]
        #print(start_urls)
    

    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('li'):
            BRAND = response.css('.col-md-3 span::text')[1].getall()
            PART_NO = response.css('.col-md-4 strong::text').extract()
            CROSS_BRAND = post.css('label::text').getall()
            CROSS_PART = post.css('a::text').getall()
            CUR_URL = [response.request.url]

            items['BRAND'] = BRAND
            items['PART_NO'] = PART_NO
            items['CROSS_BRAND'] = CROSS_BRAND
            items['CROSS_PART'] = CROSS_PART
            items['CUR_URL'] = CUR_URL
            
            yield items






