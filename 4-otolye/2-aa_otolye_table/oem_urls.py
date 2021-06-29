import psycopg2
import os

# To go previous folder to import variables.py
# import sys
# sys.path.append('../')
from variables import *

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()



if os.path.exists("..\\2-aa_otolye_table\\0-URLS\\urls.txt"):
    os.remove("..\\2-aa_otolye_table\\0-URLS\\urls.txt")

    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_1.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_2.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_3.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_4.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_5.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_6.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_7.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_8.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_9.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_10.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_11.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_12.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_13.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_14.txt')
    os.remove('..\\2-aa_otolye_table\\0-URLS\\urls_15.txt')

'''
if os.path.exists("..\\%s\\OEM\\urls.txt" % (folder_name,)):
    os.remove("..\\%s\\OEM\\urls.txt" % (folder_name,))
'''

cursor.execute("DROP TABLE IF EXISTS aa_otolye")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_otolye (part_no TEXT, price TEXT, cross_part TEXT, cur_url TEXT)")
connection.commit()

#else:
#    print("Can not delete the file as it doesn't exists")

# cursor.execute("CREATE TEMPORARY TABLE tem_otolye_links_table (tem_link TEXT)")
cursor.execute("CREATE TABLE tem_otolye_links_table (tem_link TEXT)")
connection.commit()
#cursor.execute("DROP TABLE IF EXISTS tem_otolye_links_table")
#cursor.execute("CREATE TABLE IF NOT EXISTS tem_otolye_links_table (tem_link TEXT)")
cursor.execute("INSERT INTO tem_otolye_links_table SELECT DISTINCT tem_link FROM aa_otolye_links")
connection.commit()
cursor.execute("DELETE FROM aa_otolye_links")
connection.commit()
cursor.execute("INSERT INTO aa_otolye_links SELECT tem_link FROM tem_otolye_links_table")
connection.commit()
cursor.execute("DROP TABLE tem_otolye_links_table")
connection.commit()

# os.remove("urls.txt")
# cursor.execute("SELECT concat(f_cross_ref, cross_ref) FROM aloparca_alfaromeo")
#  cursor.execute("SELECT link FROM aloparca_bmw")
cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve 1000 rows starting from the 1000th
cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 1000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_1.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve 1000 rows starting from the 2000th
cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 2000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_2.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 3000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_3.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 4000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_4.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 5000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_5.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 6000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_6.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 7000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_7.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 8000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_8.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 9000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_9.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 10000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_10.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 11000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_11.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 12000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_12.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 13000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_13.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT tem_link FROM aa_otolye_links LIMIT 1000 OFFSET 14000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_14.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve all rows starting from the 15000th
cursor.execute("SELECT tem_link FROM aa_otolye_links OFFSET 15000")
with open("..\\2-aa_otolye_table\\0-URLS\\urls_15.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)




connection.close()