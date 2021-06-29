import os

os.system("scrapy crawl quotes")

print('Great It works')
f= open("afterscrapy.txt","w+")
