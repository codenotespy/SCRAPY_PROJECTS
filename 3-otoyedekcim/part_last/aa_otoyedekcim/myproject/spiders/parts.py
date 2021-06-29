import scrapy
from myproject.items import MyprojectItem
#from scrapy.loader import ItemLoader

# To go previous folder to import variables.py
import sys
sys.path.append('../../')
from variables import *

class PartsSpider(scrapy.Spider):
    name = 'parts'
    # page_number = page_start_number
    start_urls = start_link

    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('.urungrid'):
            TEM_LINK = post.css('a::attr(href)').get(),

            items['TEM_LINK'] = TEM_LINK

            yield items


        next_page = response.css('.sayfalama li:nth-last-child(1) a::attr(href)').get()
        # print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
            # yield scrapy.Request(next_page, callback=self.parse)
            # So if next page is not none parse funtion will be colled back again and the data will be bringed from the next page.

        '''
        # To bring datas from the other pages too.
        next_page = the_link + str(PartsSpider.page_number) + '?'
        if PartsSpider.page_number < 251:
            PartsSpider.page_number +=1
            yield response.follow(next_page, callback= self.parse)
        if PartsSpider.page_number > 250:
            yield response(callback= self.alert)
        '''  