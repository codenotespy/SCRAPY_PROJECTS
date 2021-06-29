import psycopg2
from variables import *

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()


#To remove duplicates
cursor.execute("CREATE TEMPORARY TABLE temp_table AS SELECT DISTINCT part_no, brand, description, cross_ref, m_price, remainder FROM %s" % (db_name,))
connection.commit()
cursor.execute("DELETE FROM %s" % (db_name,))
cursor.execute("INSERT INTO %s SELECT brand, part_no, description, cross_ref, m_price, remainder FROM temp_table" % (db_name,))
connection.commit()
#To organise
cursor.execute("ALTER TABLE %s ADD IF NOT EXISTS LINK TEXT" % (db_name,))
cursor.execute("ALTER TABLE %s ADD IF NOT EXISTS PRICE TEXT" % (db_name,))
cursor.execute("UPDATE %s SET link = concat('https://www.aloparca.com', cross_ref)" % (db_name,))
cursor.execute("UPDATE %s SET PRICE = concat(m_price, '.', remainder)" % (db_name,))
# cursor.execute("UPDATE %s SET link = f_cross_ref || cross_ref" % (db_name,))
connection.commit()

cursor.execute("ALTER TABLE %s DROP COLUMN m_price, DROP COLUMN remainder, DROP COLUMN cross_ref" % (db_name,))
connection.commit()


cursor.execute("INSERT INTO aa_aloparca SELECT * FROM {0}".format(db_name))
connection.commit()



connection.close()