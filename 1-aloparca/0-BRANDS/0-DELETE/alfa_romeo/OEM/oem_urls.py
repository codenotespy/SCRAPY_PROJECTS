import psycopg2
import os

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()


if os.path.exists('..\\alfa_romeo\\OEM\\urls.txt'):
    os.remove('..\\alfa_romeo\\OEM\\urls.txt')
#else:
#    print("Can not delete the file as it doesn't exists")


# os.remove("urls.txt")
# cursor.execute("SELECT concat(f_cross_ref, cross_ref) FROM aloparca_alfaromeo")
cursor.execute("SELECT link FROM aloparca_alfaromeo")
with open("urls.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)



connection.close()