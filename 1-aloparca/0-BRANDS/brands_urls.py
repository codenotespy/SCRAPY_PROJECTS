import psycopg2
import os

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()



cursor.execute("ALTER TABLE brand_links ADD IF NOT EXISTS links TEXT")
cursor.execute("UPDATE brand_links SET links = concat('https://www.aloparca.com', link)")
connection.commit()


if os.path.exists('urls.txt'):
    os.remove('urls.txt')
#else:
#    print("Can not delete the file as it doesn't exists")

# os.remove("urls.txt")
# cursor.execute("SELECT concat(f_cross_ref, cross_ref) FROM brand_links")
cursor.execute("SELECT links FROM brand_links")
with open("urls.txt", "w", newline='') as f:
    for row in cursor:
        print(row[0], file=f)



connection.close()