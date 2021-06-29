import psycopg2
import os

# To go previous folder to import variables.py
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





if os.path.exists("../aa_parcafilosu/urls/urls.txt"):
    os.remove("../aa_parcafilosu/urls/urls.txt")
    os.remove("../aa_parcafilosu/urls/urls_1.txt")
    os.remove("../aa_parcafilosu/urls/urls_2.txt")
    os.remove("../aa_parcafilosu/urls/urls_3.txt")
    os.remove("../aa_parcafilosu/urls/urls_4.txt")
    os.remove("../aa_parcafilosu/urls/urls_5.txt")
    os.remove("../aa_parcafilosu/urls/urls_6.txt")
    os.remove("../aa_parcafilosu/urls/urls_7.txt")


'''
if os.path.exists("../aa_parcafilosu/urls/urls.txt" % (folder_name,)):
    os.remove("../aa_parcafilosu/urls/urls.txt" % (folder_name,))
'''


#else:
#    print("Can not delete the file as it doesn't exists")


# os.remove("urls.txt")
# cursor.execute("SELECT concat(f_cross_ref, cross_ref) FROM aloparca_alfaromeo")
#  cursor.execute("SELECT link FROM aloparca_bmw")

# To retrieve first 1000 rows :
cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000")
with open("../aa_parcafilosu/urls/urls.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

# To retrieve 1000 rows starting from the 1000th
cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000 OFFSET 10000")
with open("../aa_parcafilosu/urls/urls_1.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000 OFFSET 20000")
with open("../aa_parcafilosu/urls/urls_2.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000 OFFSET 30000")
with open("../aa_parcafilosu/urls/urls_3.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000 OFFSET 40000")
with open("../aa_parcafilosu/urls/urls_4.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000 OFFSET 50000")
with open("../aa_parcafilosu/urls/urls_5.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)

cursor.execute("SELECT link FROM aa_parcafilosu LIMIT 10000 OFFSET 60000")
with open("../aa_parcafilosu/urls/urls_6.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)


# To retrieve all rows starting from the 65000th
cursor.execute("SELECT link FROM aa_parcafilosu OFFSET 70000")
with open("../aa_parcafilosu/urls/urls_7.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)




connection.close()