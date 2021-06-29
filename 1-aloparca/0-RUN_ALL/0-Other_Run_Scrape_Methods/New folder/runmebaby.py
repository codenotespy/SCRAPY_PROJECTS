import os
import multiprocessing
#os.system("myproject1\\runscrapy2.py")

#from scrapy import cmdline
#os.system("scrapy crawl parts")
#cmdline.execute("cd myproject1".split())
#cmdline.execute("myproject1\\runscrapy.bat".split())


def join1():
    os.system('ford.bat')

def join2():
    os.system('alfa_romeo.bat')

def join3():
    os.system('aston_martin.bat')

def join4():
    os.system('audi.bat')

p1 = multiprocessing.Process(target=join1)
p2 = multiprocessing.Process(target=join2)
p3 = multiprocessing.Process(target=join3)
p4 = multiprocessing.Process(target=join4)

if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
