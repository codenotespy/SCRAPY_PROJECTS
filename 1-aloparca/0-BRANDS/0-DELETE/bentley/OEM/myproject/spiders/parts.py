import scrapy
from myproject.items import MyprojectItem

#from scrapy.contrib.loader import ItemLoader
#from scrapy.contrib.loader.processor import Join
#from scrapy.loader import ItemLoader

class PartsSpider(scrapy.Spider):
    name = 'parts'
    page_number = 2
    with open("urls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]
        print(start_urls)
    

    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('tr'):
            BRAND = response.css('.marka a::text').extract()
            PART_NO = response.css('.marka::text')[2].getall()
            CROSS_BRAND = post.css('td::text').getall()
            CROSS_PART = post.css('td a::text').getall()

            items['BRAND'] = BRAND
            items['PART_NO'] = PART_NO
            items['CROSS_BRAND'] = CROSS_BRAND
            items['CROSS_PART'] = CROSS_PART
            
            yield items






