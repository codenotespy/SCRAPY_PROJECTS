import os
from urllib.parse import urlparse

brand = urlparse(os.getcwd()).path.rpartition('\\')[2]
### brand = 'current_folder_name' ###


db_name = brand
the_link = 'https://www.parcafilosu.com.tr/yedek-parcalari'
proxy_url = 'https://131.72.69.14:8080'


folder_name = brand
oem_db_name= 'aa_parcafilosu_oem'
start_link = [the_link]
# paginate_link = the_link + '?sayfa='
