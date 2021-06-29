import psycopg2
import sys
sys.path.append('../')
from variables import *

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()

cursor.execute("INSERT INTO aa_aloparca_oem SELECT * FROM {0}".format(oem_db_name))
connection.commit()




connection.close()