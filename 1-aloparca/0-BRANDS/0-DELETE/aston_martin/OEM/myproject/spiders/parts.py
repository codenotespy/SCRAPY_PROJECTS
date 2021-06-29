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
    # start_urls = ['https://www.aloparca.com/oto-yedek-parca/ALFA_ROMEO?sayfa=4']
    

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



'''
        next_page = response.css('a.icon-caret-right::attr(href)').get()
        if next_page is not None: # To make sure there isn't next page.
            next_page = response.urljoin(next_page) # If it is not none.
            yield scrapy.Request(next_page, callback=self.parse) # So if next page is not none parse funtion will be colled back again and the data will be bringed from the next page.
'''



