import scrapy
from myproject.items import MyprojectItem
#from scrapy.loader import ItemLoader

# To go previous folder to import variables.py
import sys
sys.path.append('../../')
from variables import *

class PartsSpider(scrapy.Spider):
    name = 'parts'
    page_number = 2
    start_urls = start_link

    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('.product-desc'):

            TEM_LINK = post.css('a::attr(href)').extract()

            items['TEM_LINK'] = TEM_LINK

            yield items

        # To bring datas from the other pages too.
        next_page = paginate_link + str(PartsSpider.page_number)
        if PartsSpider.page_number < 200:
            PartsSpider.page_number +=1
            yield response.follow(next_page, callback= self.parse)
        if PartsSpider.page_number > 199:
            yield response(callback= self.alert)


            
        '''
        next_page = response.css('.nav-links a:nth-last-child(1)::attr(href)').get()
        print('HEYHEY :' + next_page)
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
            # yield scrapy.Request(next_page, callback=self.parse)
            # So if next page is not none parse funtion will be colled back again and the data will be bringed from the next page.
        '''

