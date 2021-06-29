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



os.system('1_organise.bat')

def urls():
    os.system('urls.bat')

def urls_1():
    os.system('urls_1.bat')

def urls_2():
    os.system('urls_2.bat')

def urls_3():
    os.system('urls_3.bat')

def urls_4():
    os.system('urls_4.bat')

def urls_5():
    os.system('urls_5.bat')

def urls_6():
    os.system('urls_6.bat')

def urls_7():
    os.system('urls_7.bat')

def urls_8():
    os.system('urls_8.bat')

def urls_9():
    os.system('urls_9.bat')

def urls_10():
    os.system('urls_10.bat')

def urls_11():
    os.system('urls_11.bat')

def urls_12():
    os.system('urls_12.bat')

def urls_13():
    os.system('urls_13.bat')

def urls_14():
    os.system('urls_14.bat')

def urls_15():
    os.system('urls_15.bat')





u1 = multiprocessing.Process(target=urls)
u2 = multiprocessing.Process(target=urls_1)
u3 = multiprocessing.Process(target=urls_2)
u4 = multiprocessing.Process(target=urls_3)
u5 = multiprocessing.Process(target=urls_4)
u6 = multiprocessing.Process(target=urls_5)
u7 = multiprocessing.Process(target=urls_6)
u8 = multiprocessing.Process(target=urls_7)
u9 = multiprocessing.Process(target=urls_8)
u10 = multiprocessing.Process(target=urls_9)
u11 = multiprocessing.Process(target=urls_10)
u12 = multiprocessing.Process(target=urls_11)
u13 = multiprocessing.Process(target=urls_12)
u14 = multiprocessing.Process(target=urls_13)
u15 = multiprocessing.Process(target=urls_14)
u16 = multiprocessing.Process(target=urls_15)


if __name__ == '__main__':
    u1.start()
    u2.start()
    u3.start()
    u4.start()
    u5.start()
    u6.start()
    u7.start()
    u8.start()
    u9.start()
    u10.start()
    u11.start()
    u12.start()
    u13.start()
    u14.start()
    u15.start()
    u16.start()
    
    u1.join()
    u2.join()
    u3.join()
    u4.join()
    u5.join()
    u6.join()
    u7.join()
    u8.join()
    u9.join()
    u10.join()
    u11.join()
    u12.join()
    u13.join()
    u14.join()
    u15.join()
    u16.join()


    cursor.execute("UPDATE aa_otolye SET cross_part = REPLACE(cross_part, ' orijinal parça numaraları ile uyumlu olacak şekilde üretilmiştir.', '')")
    cursor.execute("UPDATE aa_otolye SET price = REPLACE(price, '                        ', '')")
    connection.commit()
    connection.close()

    # finish = time.perf_counter()
    # print(f'Successfully finished in {round((finish-start)/60, 2)} minute(s) bro')
