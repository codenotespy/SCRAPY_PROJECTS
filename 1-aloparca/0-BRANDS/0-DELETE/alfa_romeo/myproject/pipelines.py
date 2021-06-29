# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# import mysql.connector
import psycopg2

class MyprojectPipeline(object):

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.conn = psycopg2.connect(
            host="localhost",
            user="postgres",
            database="SCRAPY_DB",
            password="yolo12",
        )
        self.curr = self.conn.cursor()

    def create_table(self):
        self.curr.execute("""DROP TABLE IF EXISTS ALOPARCA_ALFAROMEO""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS ALOPARCA_ALFAROMEO (BRAND TEXT, PART_NO TEXT, DESCRIPTION TEXT, CROSS_REF TEXT, M_PRICE TEXT, REMAINDER TEXT)""")
        self.conn.commit()
    def process_item(self, items, spider):
        self.store_db(items)
#        print("pipeline :" + aloparca_ford_items['title'][0])
        return items


    def process_item(self, items, spider):
        self.store_db(items)
        return items
        
    def store_db(self, items):
        self.curr.execute("""insert into ALOPARCA_ALFAROMEO values(%s,%s,%s,%s,%s,%s)""",(
            items['BRAND'][0],
            items['PART_NO'][0],
            items['DESCRIPTION'][0],
            items['CROSS_REF'][0],
            items['M_PRICE'][0],
            items['REMAINDER'][0],
        ))
        
        self.conn.commit()



