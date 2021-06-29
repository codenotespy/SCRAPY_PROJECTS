import psycopg2

connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()


#To remove duplicates
cursor.execute("CREATE TEMPORARY TABLE temp_table AS SELECT DISTINCT part_no, brand, description, cross_ref, m_price, remainder FROM aloparca_alfaromeo")
connection.commit()
cursor.execute("DELETE FROM aloparca_alfaromeo")
cursor.execute("INSERT INTO aloparca_alfaromeo SELECT brand, part_no, description, cross_ref, m_price, remainder FROM temp_table")
connection.commit()
#To organise
cursor.execute("ALTER TABLE aloparca_alfaromeo ADD IF NOT EXISTS LINK TEXT")
cursor.execute("ALTER TABLE aloparca_alfaromeo ADD IF NOT EXISTS PRICE TEXT")
cursor.execute("UPDATE aloparca_alfaromeo SET link = concat('https://www.aloparca.com', cross_ref)")
cursor.execute("UPDATE aloparca_alfaromeo SET PRICE = concat(m_price, '.', remainder)")
# cursor.execute("UPDATE aloparca_alfaromeo SET link = f_cross_ref || cross_ref")
connection.commit()

cursor.execute("ALTER TABLE aloparca_alfaromeo DROP COLUMN m_price, DROP COLUMN remainder, DROP COLUMN cross_ref")
connection.commit()







connection.close()