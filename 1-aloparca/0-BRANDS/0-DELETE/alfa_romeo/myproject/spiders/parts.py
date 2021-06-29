import scrapy
from myproject.items import MyprojectItem

#from scrapy.contrib.loader import ItemLoader
#from scrapy.contrib.loader.processor import Join
#from scrapy.loader import ItemLoader

class PartsSpider(scrapy.Spider):
    name = 'parts'
    page_number = 2
    start_urls = ['https://www.aloparca.com/oto-yedek-parca/ALFA_ROMEO?sayfa=4']
    

    def parse(self, response):
        items = MyprojectItem()
        for post in response.css('.crvvuQ'):
            BRAND = post.css('b::text').extract()
            PART_NO = post.css('b::text')[1].getall()
            DESCRIPTION = post.css('b::text')[3].getall()
            M_PRICE = post.css('.fiyat div::text').extract()
            REMAINDER = post.css('.fiyat div span::text')[1].getall()
            #PRICE = str(post.css('.fiyat div::text').extract()) + '.' + str(post.css('.fiyat div span::text')[1].getall())
            # F_CROSS_REF = ['https://www.aloparca.com']
            CROSS_REF = post.css('a.title::attr(href)').getall()

            items['BRAND'] = BRAND
            items['PART_NO'] = PART_NO
            items['DESCRIPTION'] = DESCRIPTION
            items['CROSS_REF'] = CROSS_REF
            items['M_PRICE'] = M_PRICE
            items['REMAINDER'] = REMAINDER
            
            yield items

        # To bring datas from the other pages too.
        next_page = 'https://www.aloparca.com/oto-yedek-parca/ALFA_ROMEO?sayfa=' + str(PartsSpider.page_number) + '/'
        if PartsSpider.page_number < 50:
            PartsSpider.page_number +=1
            yield response.follow(next_page, callback= self.parse)
        if PartsSpider.page_number > 51:
            yield response(callback= self.alert)

'''
        next_page = response.css('a.icon-caret-right::attr(href)').get()
        if next_page is not None: # To make sure there isn't next page.
            next_page = response.urljoin(next_page) # If it is not none.
            yield scrapy.Request(next_page, callback=self.parse) # So if next page is not none parse funtion will be colled back again and the data will be bringed from the next page.
'''



