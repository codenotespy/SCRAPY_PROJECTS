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



#To organise
cursor.execute("ALTER TABLE %s ADD IF NOT EXISTS LINK TEXT" % (db_name_link,))
cursor.execute("UPDATE %s SET link = concat('https://www.otoyedekcim.com/oto-yedek-parcalari', TEM_LINK)" % (db_name_link,))
connection.commit()



if os.path.exists('0-URLS/urls.txt'):
    os.remove('0-URLS/urls.txt')

    os.remove('0-URLS/urls_1.txt')
    os.remove('0-URLS/urls_2.txt')
    os.remove('0-URLS/urls_3.txt')
    os.remove('0-URLS/urls_4.txt')
    os.remove('0-URLS/urls_5.txt')
    os.remove('0-URLS/urls_6.txt')
    os.remove('0-URLS/urls_7.txt')
    os.remove('0-URLS/urls_8.txt')
    os.remove('0-URLS/urls_9.txt')
    os.remove('0-URLS/urls_10.txt')
    os.remove('0-URLS/urls_11.txt')
    os.remove('0-URLS/urls_12.txt')
    os.remove('0-URLS/urls_13.txt')
    os.remove('0-URLS/urls_14.txt')
    os.remove('0-URLS/urls_15.txt')
    os.remove('0-URLS/urls_16.txt')
    os.remove('0-URLS/urls_17.txt')
    os.remove('0-URLS/urls_18.txt')
    os.remove('0-URLS/urls_19.txt')
    os.remove('0-URLS/urls_20.txt')
    os.remove('0-URLS/urls_21.txt')
    os.remove('0-URLS/urls_22.txt')
    os.remove('0-URLS/urls_23.txt')
    os.remove('0-URLS/urls_24.txt')
    os.remove('0-URLS/urls_25.txt')
    os.remove('0-URLS/urls_26.txt')
    os.remove('0-URLS/urls_27.txt')
    os.remove('0-URLS/urls_28.txt')
    os.remove('0-URLS/urls_29.txt')
    os.remove('0-URLS/urls_30.txt')
    os.remove('0-URLS/urls_31.txt')
    os.remove('0-URLS/urls_32.txt')
    os.remove('0-URLS/urls_33.txt')
    os.remove('0-URLS/urls_34.txt')
    os.remove('0-URLS/urls_35.txt')
    os.remove('0-URLS/urls_36.txt')
    os.remove('0-URLS/urls_37.txt')
    os.remove('0-URLS/urls_38.txt')
    os.remove('0-URLS/urls_39.txt')
    os.remove('0-URLS/urls_40.txt')
    os.remove('0-URLS/urls_41.txt')
    os.remove('0-URLS/urls_42.txt')
    os.remove('0-URLS/urls_43.txt')
    os.remove('0-URLS/urls_44.txt')
    os.remove('0-URLS/urls_45.txt')
    os.remove('0-URLS/urls_46.txt')
    os.remove('0-URLS/urls_47.txt')
    os.remove('0-URLS/urls_48.txt')
    os.remove('0-URLS/urls_49.txt')
    os.remove('0-URLS/urls_50.txt')
    os.remove('0-URLS/urls_51.txt')
    os.remove('0-URLS/urls_52.txt')
    os.remove('0-URLS/urls_53.txt')
    os.remove('0-URLS/urls_54.txt')
    os.remove('0-URLS/urls_55.txt')
    os.remove('0-URLS/urls_56.txt')
    os.remove('0-URLS/urls_57.txt')
    os.remove('0-URLS/urls_58.txt')
    os.remove('0-URLS/urls_59.txt')
    os.remove('0-URLS/urls_60.txt')
    os.remove('0-URLS/urls_61.txt')
    os.remove('0-URLS/urls_62.txt')
    os.remove('0-URLS/urls_63.txt')
    os.remove('0-URLS/urls_64.txt')
    os.remove('0-URLS/urls_65.txt')


#else:
#    print("Can not delete the file as it doesn't exists")
'''
cursor.execute("DROP TABLE IF EXISTS aa_otoyedekcim")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_otoyedekcim (part_no TEXT, price TEXT, cross_part TEXT)")
connection.commit()

cursor.execute("CREATE TEMPORARY TABLE tem_otoyedekcim_links_table (link TEXT)")
cursor.execute("INSERT INTO tem_otoyedekcim_links_table SELECT DISTINCT link FROM aa_otoyedekcim_links")
cursor.execute("DELETE FROM aa_otoyedekcim_links")
cursor.execute("INSERT INTO aa_otoyedekcim_links SELECT link FROM tem_otoyedekcim_links_table")
connection.commit()
'''
# os.remove("urls.txt")
# cursor.execute("SELECT concat(f_cross_ref, cross_ref) FROM aloparca_alfaromeo")
#cursor.execute("SELECT link FROM %s" % (db_name_link,))
cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000")
with open("0-URLS/urls.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve 1000 rows starting from the 1000th
cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 1000")
with open("0-URLS/urls_1.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve 1000 rows starting from the 2000th
cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 2000")
with open("0-URLS/urls_2.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 3000")
with open("0-URLS/urls_3.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 4000")
with open("0-URLS/urls_4.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 5000")
with open("0-URLS/urls_5.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 6000")
with open("0-URLS/urls_6.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 7000")
with open("0-URLS/urls_7.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 8000")
with open("0-URLS/urls_8.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 9000")
with open("0-URLS/urls_9.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 10000")
with open("0-URLS/urls_10.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 11000")
with open("0-URLS/urls_11.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 12000")
with open("0-URLS/urls_12.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 13000")
with open("0-URLS/urls_13.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 14000")
with open("0-URLS/urls_14.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 15000")
with open("0-URLS/urls_15.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 16000")
with open("0-URLS/urls_16.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 17000")
with open("0-URLS/urls_17.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 18000")
with open("0-URLS/urls_18.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 19000")
with open("0-URLS/urls_19.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 20000")
with open("0-URLS/urls_20.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 21000")
with open("0-URLS/urls_21.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 22000")
with open("0-URLS/urls_22.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 23000")
with open("0-URLS/urls_23.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 24000")
with open("0-URLS/urls_24.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 25000")
with open("0-URLS/urls_25.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 26000")
with open("0-URLS/urls_26.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 27000")
with open("0-URLS/urls_27.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 28000")
with open("0-URLS/urls_28.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 29000")
with open("0-URLS/urls_29.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 30000")
with open("0-URLS/urls_30.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 31000")
with open("0-URLS/urls_31.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 32000")
with open("0-URLS/urls_32.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 33000")
with open("0-URLS/urls_33.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 34000")
with open("0-URLS/urls_34.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 35000")
with open("0-URLS/urls_35.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 36000")
with open("0-URLS/urls_36.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 37000")
with open("0-URLS/urls_37.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 38000")
with open("0-URLS/urls_38.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 39000")
with open("0-URLS/urls_39.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 40000")
with open("0-URLS/urls_40.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 41000")
with open("0-URLS/urls_41.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 42000")
with open("0-URLS/urls_42.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 43000")
with open("0-URLS/urls_43.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 44000")
with open("0-URLS/urls_44.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 45000")
with open("0-URLS/urls_45.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 46000")
with open("0-URLS/urls_46.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 47000")
with open("0-URLS/urls_47.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 48000")
with open("0-URLS/urls_48.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 49000")
with open("0-URLS/urls_49.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 50000")
with open("0-URLS/urls_50.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 51000")
with open("0-URLS/urls_51.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 52000")
with open("0-URLS/urls_52.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 53000")
with open("0-URLS/urls_53.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 54000")
with open("0-URLS/urls_54.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 55000")
with open("0-URLS/urls_55.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 56000")
with open("0-URLS/urls_56.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 57000")
with open("0-URLS/urls_57.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 58000")
with open("0-URLS/urls_58.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 59000")
with open("0-URLS/urls_59.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 60000")
with open("0-URLS/urls_60.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 61000")
with open("0-URLS/urls_61.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 62000")
with open("0-URLS/urls_62.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 63000")
with open("0-URLS/urls_63.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_otoyedekcim_links LIMIT 1000 OFFSET 64000")
with open("0-URLS/urls_64.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve all rows starting from the 65000th
cursor.execute("SELECT link FROM aa_otoyedekcim_links OFFSET 65000")
with open("0-URLS/urls_65.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)



connection.commit()
connection.close()