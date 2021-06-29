import os
import psycopg2
# import sqlalchemy
from sqlalchemy import create_engine
import pandas as pd


connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()



# cursor.execute("ALTER TABLE aa_aloparca ADD COLUMN cross_part TEXT AFTER description)")

cursor.execute("DROP TABLE IF EXISTS aa_all")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_all (brand TEXT, part_no TEXT, description TEXT, cross_part TEXT, price TEXT, url TEXT, supplier TEXT)")
connection.commit()





# FROM aa_aloparca
cursor.execute("ALTER TABLE aa_aloparca ADD COLUMN IF NOT EXISTS cross_part TEXT, ADD COLUMN IF NOT EXISTS supplier TEXT")
cursor.execute("UPDATE aa_aloparca SET supplier = 'ALOPARCA'")

cursor.execute("DROP TABLE IF EXISTS tem_aa_aloparca")
cursor.execute("CREATE TABLE IF NOT EXISTS tem_aa_aloparca (brand TEXT, part_no TEXT, description TEXT, price TEXT, link TEXT, cross_part TEXT, supplier TEXT)")
connection.commit()

cursor.execute("DROP TABLE IF EXISTS tem_parcafilosu_oem_parts")
cursor.execute("CREATE TABLE IF NOT EXISTS tem_parcafilosu_oem_parts (link TEXT, cross_parts TEXT)")
connection.commit()
cursor.execute("INSERT INTO tem_parcafilosu_oem_parts SELECT link, string_agg(cross_ref, ', ') FROM aa_aloparca_oem GROUP BY link")
connection.commit()

cursor.execute("INSERT INTO tem_aa_aloparca SELECT aa_aloparca.brand, aa_aloparca.part_no, aa_aloparca.description, aa_aloparca.price, aa_aloparca.link, tem_parcafilosu_oem_parts.cross_parts, aa_aloparca.supplier FROM aa_aloparca LEFT JOIN tem_parcafilosu_oem_parts ON aa_aloparca.link=tem_parcafilosu_oem_parts.link")
connection.commit()
cursor.execute("DROP TABLE IF EXISTS aa_aloparca")
connection.commit()
cursor.execute("ALTER TABLE tem_aa_aloparca RENAME TO aa_aloparca")
connection.commit()

cursor.execute("INSERT INTO aa_all SELECT DISTINCT ON (part_no) brand, part_no, description, cross_part, price, link, supplier FROM aa_aloparca")
connection.commit()


# FROM aa_otolye
cursor.execute("ALTER TABLE aa_otolye ADD COLUMN IF NOT EXISTS brand TEXT, ADD COLUMN IF NOT EXISTS description TEXT, ADD COLUMN IF NOT EXISTS supplier TEXT")
cursor.execute("UPDATE aa_otolye SET supplier = 'OTOLYE'")
cursor.execute("INSERT INTO aa_all SELECT DISTINCT ON (part_no) brand, part_no, description, cross_part, price, cur_url, supplier FROM aa_otolye")
connection.commit()


# FROM aa_otoyedekcim
cursor.execute("ALTER TABLE aa_otoyedekcim ADD COLUMN IF NOT EXISTS brand TEXT, ADD COLUMN IF NOT EXISTS cross_part TEXT, ADD COLUMN IF NOT EXISTS supplier TEXT")
cursor.execute("UPDATE aa_otoyedekcim SET supplier = 'OTOYEDEKCIM'")
cursor.execute("INSERT INTO aa_all SELECT DISTINCT ON (part_no) brand, part_no, description, cross_part, price, CUR_URL, supplier FROM aa_otoyedekcim")
connection.commit()


# FROM aa_parcafilosu
cursor.execute("ALTER TABLE aa_parcafilosu ADD COLUMN IF NOT EXISTS cross_part TEXT, ADD COLUMN IF NOT EXISTS supplier TEXT")
cursor.execute("UPDATE aa_parcafilosu SET supplier = 'PARCAFILOSU'")

cursor.execute("DROP TABLE IF EXISTS tem_aa_parcafilosu")
cursor.execute("CREATE TABLE IF NOT EXISTS tem_aa_parcafilosu (brand TEXT, part_no TEXT, description TEXT, price TEXT, link TEXT, cross_part TEXT, supplier TEXT)")
connection.commit()

cursor.execute("DROP TABLE IF EXISTS tem_parcafilosu_oem_parts")
cursor.execute("CREATE TABLE IF NOT EXISTS tem_parcafilosu_oem_parts (cur_url TEXT, cross_parts TEXT)")
connection.commit()
cursor.execute("INSERT INTO tem_parcafilosu_oem_parts SELECT cur_url, string_agg(cross_ref, ', ') FROM aa_parcafilosu_oem GROUP BY cur_url")
connection.commit()

cursor.execute("INSERT INTO tem_aa_parcafilosu SELECT aa_parcafilosu.brand, aa_parcafilosu.part_no, aa_parcafilosu.description, aa_parcafilosu.price, aa_parcafilosu.link, tem_parcafilosu_oem_parts.cross_parts, aa_parcafilosu.supplier FROM aa_parcafilosu LEFT JOIN tem_parcafilosu_oem_parts ON aa_parcafilosu.link=tem_parcafilosu_oem_parts.cur_url")
connection.commit()
cursor.execute("DROP TABLE IF EXISTS aa_parcafilosu")
connection.commit()
cursor.execute("ALTER TABLE tem_aa_parcafilosu RENAME TO aa_parcafilosu")
connection.commit()

cursor.execute("INSERT INTO aa_all SELECT DISTINCT ON (part_no) brand, part_no, description, cross_part, price, link, supplier FROM aa_parcafilosu")
connection.commit()


# To add integer not null id column:
cursor.execute("ALTER TABLE aa_all ADD COLUMN IF NOT EXISTS id SERIAL")
connection.commit()









connection_dj = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="COMPARISION",
    password="yolo12",
)
cursor_dj = connection_dj.cursor()

cursor_dj.execute("DROP TABLE IF EXISTS myapp_main_table")
cursor_dj.execute("CREATE TABLE IF NOT EXISTS myapp_main_table (id SERIAL, brand TEXT, part_no TEXT, description TEXT, cross_part TEXT, price TEXT, url TEXT, supplier TEXT)")
connection_dj.commit()






# Transfer from scrapy database to django database:
db1 = create_engine("postgresql://postgres:yolo12@localhost/SCRAPY_DB")
db2 = create_engine("postgresql://postgres:yolo12@localhost/COMPARISION")

query_df = pd.read_sql_query('SELECT id, brand, part_no, description, cross_part, price, url, supplier FROM aa_all', con=db1)
# print(query_df)
# Below is also creating table named myapp_anhk_price_list if doesn't exists
query_df.to_sql('myapp_main_table', con=db2, index=False, if_exists='replace')






cursor_dj.execute("ALTER TABLE myapp_main_table ADD COLUMN IF NOT EXISTS part_no_form TEXT, ADD COLUMN IF NOT EXISTS cross_part_form TEXT")

cursor_dj.execute("UPDATE myapp_main_table SET part_no_form = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(part_no, '-', ''), ',', ''), ' ', ''), '.', ''), '/', ''), '\\\\', ''), '|', ''), '*', ''), '+', ''), ':', ''), ';', ''), '?', '')")
connection_dj.commit()

cursor_dj.execute("UPDATE myapp_main_table SET cross_part_form = REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(REPLACE(cross_part, '-', ''), ',', ''), ' ', ''), '.', ''), '/', ''), '\\\\', ''), '|', ''), '*', ''), '+', ''), ':', ''), ';', ''), '?', '')")
connection_dj.commit()












connection.close()
connection_dj.close()




















# cursor.execute("SELECT cross_ref FROM aa_parcafilosu_oem WHERE cur_url = 'https://www.parcafilosu.com.tr/11354-cey-motor-radyatoru-ust-hortum'")

# INSERT INTO tem_aa_parcafilosu
# cursor.execute("SELECT aa_parcafilosu.brand, aa_parcafilosu.part_no, aa_parcafilosu.description, aa_parcafilosu.price, aa_parcafilosu.link, string_agg(aa_parcafilosu_oem.cross_ref, ', ' ORDER BY aa_parcafilosu_oem.cross_ref), aa_parcafilosu.link, aa_parcafilosu.supplier FROM aa_parcafilosu LEFT JOIN aa_parcafilosu_oem ON aa_parcafilosu.link=aa_parcafilosu_oem.cur_url")

'''
cursor.execute("ALTER TABLE aa_parcafilosu_oem DROP COLUMN IF EXISTS cross_parts")
connection.commit()
'''

'''
cursor.execute("INSERT INTO tem_aa_parcafilosu SELECT cur_url, string_agg(cross_ref, ', ') FROM aa_parcafilosu_oem GROUP BY cur_url LIMIT 10")
items = cursor.fetchall()
for item in items:
    print(item)
'''

'''
SELECT country, STRING_AGG (email, ';') email_list FROM customer INNER JOIN address USING (address_id)
INNER JOIN city USING (city_id)
INNER JOIN country USING (country_id)
GROUP BY
    country
ORDER BY
    country;
'''

'''
cursor.execute("INSERT INTO tem_aa_parcafilosu SELECT * FROM aa_parcafilosu string_agg(aa_parcafilosu_oem.cross_ref, ', ') FROM aa_parcafilosu_oem LEFT JOIN aa_parcafilosu ON aa_parcafilosu.link=aa_parcafilosu_oem.cur_url")
connection.commit()
'''

'''
cursor.execute("SELECT string_agg(cross_ref, ', ') FROM aa_parcafilosu_oem WHERE cur_url = 'https://www.parcafilosu.com.tr/11354-cey-motor-radyatoru-ust-hortum'")
items = cursor.fetchall()
print(items)
'''


# print(items)
'''
for item in items:
    print(item, end=',')
'''
# print(list(range(len(items))))
'''
for i in range(len(items)):
    item = items[i][0].format(end='; ')
    print(item)
'''