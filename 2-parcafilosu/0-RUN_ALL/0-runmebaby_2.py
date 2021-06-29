import os
import multiprocessing
import time
import psycopg2
#os.system("myproject1\\runscrapy2.py")

#from scrapy import cmdline
#os.system("scrapy crawl parts")
#cmdline.execute("cd myproject1".split())
#cmdline.execute("myproject1\\runscrapy.bat".split())

# start = time.perf_counter()



connection = psycopg2.connect(
    host="localhost",
    user="postgres",
    database="SCRAPY_DB",
    password="yolo12",
)
cursor = connection.cursor()


# For url_oem table:
cursor.execute("DROP TABLE IF EXISTS aa_parcafilosu_oem")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_parcafilosu_oem (BRAND TEXT, PART_NO TEXT, CROSS_BRAND TEXT, CROSS_REF TEXT, CUR_URL TEXT)")
connection.commit()
connection.close()





def url_oem():
    os.system('url_oem.bat')

def url_oem_1():
    os.system('url_oem_1.bat')

def url_oem_2():
    os.system('url_oem_2.bat')

def url_oem_3():
    os.system('url_oem_3.bat')

def url_oem_4():
    os.system('url_oem_4.bat')

def url_oem_5():
    os.system('url_oem_5.bat')

def url_oem_6():
    os.system('url_oem_6.bat')

def url_oem_7():
    os.system('url_oem_7.bat')







u1 = multiprocessing.Process(target=url_oem)
u2 = multiprocessing.Process(target=url_oem_1)
u3 = multiprocessing.Process(target=url_oem_2)
u4 = multiprocessing.Process(target=url_oem_3)
u5 = multiprocessing.Process(target=url_oem_4)
u6 = multiprocessing.Process(target=url_oem_5)
u7 = multiprocessing.Process(target=url_oem_6)



if __name__ == '__main__':
    u1.start()
    u2.start()
    u3.start()
    u4.start()
    u5.start()
    u6.start()
    u7.start()


    u1.join()
    u2.join()
    u3.join()
    u4.join()
    u5.join()
    u6.join()
    u7.join()


    # finish = time.perf_counter()
    # print(f'Successfully finished in {round((finish-start)/60, 2)} minute(s) bro')