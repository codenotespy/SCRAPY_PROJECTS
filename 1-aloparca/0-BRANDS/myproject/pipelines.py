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
        self.curr.execute("""DROP TABLE IF EXISTS BRAND_LINKS""")
        self.curr.execute("""CREATE TABLE IF NOT EXISTS BRAND_LINKS (LINK TEXT)""")
        self.conn.commit()

    def process_item(self, items, spider):
        self.store_db(items)
#        print("pipeline :" + items['title'][0])
        return items


    def process_item(self, items, spider):
        self.store_db(items)
        return items
        
    def store_db(self, items):
        self.curr.execute("""insert into BRAND_LINKS values(%s)""",(
            items['LINK'][0],
        ))

        self.conn.commit()



