import os
from urllib.parse import urlparse

brand = urlparse(os.getcwd()).path.rpartition('\\')[2]
### brand = 'current_folder_name' ###


db_name = 'otolye_' + brand
db_name_link = 'aa_otolye_links'
the_link = 'https://otolye.com/yedek-parca/' + brand

#folder_name = brand
folder_name = brand
oem_db_name='otolye_' + brand + '_oem'
#oem_db_name='otolye_' + brand.replace('-', '_') + '_oem'
start_link = [the_link]
paginate_link = the_link + '?sayfa='

