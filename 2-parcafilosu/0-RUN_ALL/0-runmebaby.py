import os
import multiprocessing
import time
import psycopg2
#os.system("myproject1\\runscrapy2.py")

#from scrapy import cmdline
#os.system("scrapy crawl parts")
#cmdline.execute("cd myproject1".split())
#cmdline.execute("myproject1\\runscrapy.bat".split())

start = time.perf_counter()



connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()

# For main table:
cursor.execute("DROP TABLE IF EXISTS aa_parcafilosu")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_parcafilosu (BRAND TEXT, PART_NO TEXT, DESCRIPTION TEXT, PRICE TEXT, LINK TEXT)")
connection.commit()
connection.close()


def part_1():
    os.system('part_1.bat')

def part_2():
    os.system('part_2.bat')

def part_3():
    os.system('part_3.bat')

def part_4():
    os.system('part_4.bat')

def part_5():
    os.system('part_5.bat')

def part_6():
    os.system('part_6.bat')

def part_7():
    os.system('part_7.bat')
    
def part_last():
    os.system('part_last.bat')





p1 = multiprocessing.Process(target=part_1)
p2 = multiprocessing.Process(target=part_2)
p3 = multiprocessing.Process(target=part_3)
p4 = multiprocessing.Process(target=part_4)
p5 = multiprocessing.Process(target=part_5)
p6 = multiprocessing.Process(target=part_5)
p7 = multiprocessing.Process(target=part_5)
p8 = multiprocessing.Process(target=part_last)


if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
 
    os.system('url_oem_organise.bat')
    os.system('1_runmebaby_2.bat')



    finish = time.perf_counter()
    print(f'Successfully finished in {round((finish-start)/60, 2)} minute(s) bro')




