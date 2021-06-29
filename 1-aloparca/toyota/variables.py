import os
from urllib.parse import urlparse

brand = urlparse(os.getcwd()).path.rpartition('\\')[2]
### brand = 'current_folder_name' ###


db_name = 'aloparca_' + brand
the_link = 'https://www.aloparca.com/oto-yedek-parca/' + brand

folder_name = brand
oem_db_name='aloparca_' + brand + '_oem'
start_link = [the_link]
paginate_link = the_link + '?sayfa='
