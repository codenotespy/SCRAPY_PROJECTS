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



if os.path.exists("..\\..\\{0}\\{0}\\urls.txt".format(folder_name)):
    os.remove("..\\..\\{0}\\{0}\\urls.txt".format(folder_name))

'''
if os.path.exists("..\\%s\\OEM\\urls.txt" % (folder_name,)):
    os.remove("..\\%s\\OEM\\urls.txt" % (folder_name,))
'''


#else:
#    print("Can not delete the file as it doesn't exists")


# os.remove("urls.txt")
# cursor.execute("SELECT concat(f_cross_ref, cross_ref) FROM aloparca_alfaromeo")
#  cursor.execute("SELECT link FROM aloparca_bmw")
cursor.execute("SELECT link FROM {0}".format(db_name))
with open("..\\..\\{0}\\{0}\\urls.txt".format(folder_name), "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)


cursor.execute("INSERT INTO aa_aloparca_oem SELECT * FROM {0}".format(oem_db_name))
connection.commit()

connection.close()