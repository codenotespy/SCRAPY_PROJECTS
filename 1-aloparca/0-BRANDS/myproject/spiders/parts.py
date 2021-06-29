import scrapy
from myproject.items import MyprojectItem

#from scrapy.contrib.loader import ItemLoader
#from scrapy.contrib.loader.processor import Join
#from scrapy.loader import ItemLoader

class PartsSpider(scrapy.Spider):
    name = 'parts'
    page_number = 2
    start_urls = ['https://www.aloparca.com/yedek-parca-marka']
    

    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('.brand'):
            LINK = post.css('a::attr(href)').getall()


            items['LINK'] = LINK


        
            yield items







