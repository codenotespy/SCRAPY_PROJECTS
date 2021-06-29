import os
from urllib.parse import urlparse

brand = urlparse(os.getcwd()).path.rpartition('\\')[2]
### brand = 'current_folder_name' ###

db_name_link = 'aa_otoyedekcim_links'


# paginate_link = the_link + '?sayfa='
