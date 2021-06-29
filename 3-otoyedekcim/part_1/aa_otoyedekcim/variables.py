import os
from urllib.parse import urlparse

brand = urlparse(os.getcwd()).path.rpartition('\\')[2]
### brand = 'current_folder_name' ###

db_name = brand
db_name_link = 'aa_otoyedekcim_links'
the_link = 'https://www.otoyedekcim.com/oto-yedek-parcalari/' 
page_start_number = 2




folder_name = brand
oem_db_name= brand + '_oem'
start = 'https://www.otoyedekcim.com/oto-yedek-parcalari'
start_link = [start]
# paginate_link = the_link + '?sayfa='
