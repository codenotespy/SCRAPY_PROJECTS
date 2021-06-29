# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import mysql.connector
import psycopg2

# To go previous folder to import variables.py
import sys
sys.path.append('../')
from variables import *

class MyprojectPipeline(object):

    def __init__(self):
        self.create_connection()
        self.alter_table()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            database="SCRAPY_DB",
            password="yolo12",
        )
        self.curr = self.conn.cursor()

    def alter_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS {0}""".format(oem_db_name))
        self.curr.execute("""CREATE TABLE IF NOT EXISTS {0} (BRAND TEXT, PART_NO TEXT, CROSS_BRAND TEXT, CROSS_REF TEXT, link TEXT)""".format(oem_db_name))
        self.conn.commit()

    def process_item(self, items, spider):
        self.store_db(items)
#        print("pipeline :" + aloparca_ford_items['title'][0])
        return items


    def process_item(self, items, spider):
        self.store_db(items)
        return items
        
    def store_db(self, items):
        self.curr.execute("""insert into {0} values(%s,%s,%s,%s,%s)""".format(oem_db_name) ,(
            items['BRAND'][0],
            items['PART_NO'][0],
            items['CROSS_BRAND'][0],
            items['CROSS_PART'][0],
            items['LINK'][0],
        ))

        self.conn.commit()



