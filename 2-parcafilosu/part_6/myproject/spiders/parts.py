import scrapy
from myproject.items import MyprojectItem
#from scrapy.loader import ItemLoader

# To go previous folder to import variables.py
# import sys
# sys.path.append('../../')
from variables import *

class PartsSpider(scrapy.Spider):
    name = 'parts'
    page_number = page_start_number
    start_urls = start_link

    CUSTOM_PROXY = proxy_url
    # https://free-proxy-list.com/
    '''
    def start_requests(self):
        for url in self.start_urls:
            request_parse = scrapy.Request(url, callback=self.parse)
            request_parse.meta['proxy'] = self.CUSTOM_PROXY
            yield request_parse
    '''
    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('.product-item-holder'):
            BRAND = post.css('.no-padding-left span::text').extract_first(),
            PART_NO = post.css('.brand span::text')[3].getall()
            DESCRIPTION = post.css('.urunListeH3::text').extract_first(),
            PRICE = post.css('.price-current::text').extract_first(),
            LINK = post.css('a::attr(href)').get(),


            items['BRAND'] = BRAND
            items['PART_NO'] = PART_NO
            items['DESCRIPTION'] = DESCRIPTION
            items['PRICE'] = PRICE
            items['LINK'] = LINK

            yield items


        # To bring datas from the other pages too.
        next_page = 'https://www.parcafilosu.com.tr/yedek-parcalari?p=' + str(PartsSpider.page_number)
        if PartsSpider.page_number < 60001:
            PartsSpider.page_number += 20
            yield response.follow(next_page, callback= self.parse)
        if PartsSpider.page_number > 60000:
            yield response(callback= self.alert)


        '''
        next_page = response.css('.pagination li:nth-last-child(1) a::attr(href)').get()
        # print(next_page)
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)
            # yield scrapy.Request(next_page, callback=self.parse)
            # So if next page is not none parse funtion will be colled back again and the data will be bringed from the next page.
        '''
        

        