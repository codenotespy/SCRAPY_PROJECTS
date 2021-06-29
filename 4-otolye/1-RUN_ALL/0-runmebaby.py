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



cursor.execute("DROP TABLE IF EXISTS aa_otolye_links")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_otolye_links (TEM_LINK TEXT)")

connection.commit()
connection.close()




def join1():
    os.system('alfa_romeo.bat')

def join2():
    os.system('anadol.bat')

def join3():
    os.system('audi.bat')

def join4():
    os.system('bmw.bat')

def join5():
    os.system('chery.bat')

def join6():
    os.system('chevrolet.bat')

def join7():
    os.system('chrysler.bat')

def join8():
    os.system('citroen.bat')

def join9():
    os.system('dacia.bat')

def join10():
    os.system('daewoo.bat')

def join11():
    os.system('daihatsu.bat')

def join12():
    os.system('dodge.bat')

def join13():
    os.system('ds.bat')

def join14():
    os.system('fiat.bat')

def join15():
    os.system('ford.bat')

def join16():
    os.system('geely.bat')

def join17():
    os.system('hyundai.bat')

def join18():
    os.system('infiniti.bat')

def join19():
    os.system('isuzu.bat')

def join20():
    os.system('iveco.bat')

def join21():
    os.system('jaguar.bat')

def join22():
    os.system('jeep.bat')

def join23():
    os.system('lada.bat')

def join24():
    os.system('lancia.bat')

def join25():
    os.system('land_rover.bat')

def join26():
    os.system('mazda.bat')

def join27():
    os.system('mercedes.bat')

def join28():
    os.system('mini.bat')

def join29():
    os.system('mitsubishi.bat')

def join30():
    os.system('nissan.bat')

def join31():
    os.system('opel.bat')

def join32():
    os.system('peugeot.bat')

def join33():
    os.system('porsche.bat')

def join34():
    os.system('proton.bat')

def join35():
    os.system('renault.bat')

def join36():
    os.system('saab.bat')

def join37():
    os.system('seat.bat')

def join38():
    os.system('skoda.bat')

def join39():
    os.system('smart.bat')

def join40():
    os.system('ssangyong.bat')

def join41():
    os.system('subaru.bat')

def join42():
    os.system('suzuki.bat')

def join43():
    os.system('tata.bat')

def join44():
    os.system('tofas.bat')

def join45():
    os.system('toyota.bat')

def join46():
    os.system('volkswagen.bat')

def join47():
    os.system('volvo.bat')

def join48():
    os.system('honda.bat')

def join49():
    os.system('kia.bat')



p1 = multiprocessing.Process(target=join1)
p2 = multiprocessing.Process(target=join2)
p3 = multiprocessing.Process(target=join3)
p4 = multiprocessing.Process(target=join4)
p5 = multiprocessing.Process(target=join5)
p6 = multiprocessing.Process(target=join6)
p7 = multiprocessing.Process(target=join7)
p8 = multiprocessing.Process(target=join8)
p9 = multiprocessing.Process(target=join9)
p10 = multiprocessing.Process(target=join10)
p11 = multiprocessing.Process(target=join11)
p12 = multiprocessing.Process(target=join12)
p13 = multiprocessing.Process(target=join13)
p14 = multiprocessing.Process(target=join14)
p15 = multiprocessing.Process(target=join15)
p16 = multiprocessing.Process(target=join16)
p17 = multiprocessing.Process(target=join17)
p18 = multiprocessing.Process(target=join18)
p19 = multiprocessing.Process(target=join19)
p20 = multiprocessing.Process(target=join20)
p21 = multiprocessing.Process(target=join21)
p22 = multiprocessing.Process(target=join22)
p23 = multiprocessing.Process(target=join23)
p24 = multiprocessing.Process(target=join24)
p25 = multiprocessing.Process(target=join25)
p26 = multiprocessing.Process(target=join26)
p27 = multiprocessing.Process(target=join27)
p28 = multiprocessing.Process(target=join28)
p29 = multiprocessing.Process(target=join29)
p30 = multiprocessing.Process(target=join30)
p31 = multiprocessing.Process(target=join31)
p32 = multiprocessing.Process(target=join32)
p33 = multiprocessing.Process(target=join33)
p34 = multiprocessing.Process(target=join34)
p35 = multiprocessing.Process(target=join35)
p36 = multiprocessing.Process(target=join36)
p37 = multiprocessing.Process(target=join37)
p38 = multiprocessing.Process(target=join38)
p39 = multiprocessing.Process(target=join39)
p40 = multiprocessing.Process(target=join40)
p41 = multiprocessing.Process(target=join41)
p42 = multiprocessing.Process(target=join42)
p43 = multiprocessing.Process(target=join43)
p44 = multiprocessing.Process(target=join44)
p45 = multiprocessing.Process(target=join45)
p46 = multiprocessing.Process(target=join46)
p47 = multiprocessing.Process(target=join47)
p48 = multiprocessing.Process(target=join48)
p49 = multiprocessing.Process(target=join49)



if __name__ == '__main__':
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()
    p7.start()
    p8.start()
    p9.start()
    p10.start()
    p11.start()
    p12.start()
    p13.start()
    p14.start()
    p15.start()
    p16.start()
    p17.start()
    p18.start()
    p19.start()
    p20.start()
    p21.start()
    p22.start()
    p23.start()
    p24.start()
    p25.start()
    p26.start()
    p27.start()
    p28.start()
    p29.start()
    p30.start()
    p31.start()
    p32.start()
    p33.start()
    p34.start()
    p35.start()
    p36.start()
    p37.start()
    p38.start()
    p39.start()
    p40.start()
    p41.start()
    p42.start()
    p43.start()
    p44.start()
    p45.start()
    p46.start()
    p47.start()
    p48.start()
    p49.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
    p7.join()
    p8.join()
    p9.join()
    p10.join()
    p11.join()
    p12.join()
    p13.join()
    p14.join()
    p15.join()
    p16.join()
    p17.join()
    p18.join()
    p19.join()
    p20.join()
    p21.join()
    p22.join()
    p23.join()
    p24.join()
    p25.join()
    p26.join()
    p27.join()
    p28.join()
    p29.join()
    p30.join()
    p31.join()
    p32.join()
    p33.join()
    p34.join()
    p35.join()
    p36.join()
    p37.join()
    p38.join()
    p39.join()
    p40.join()
    p41.join()
    p42.join()
    p43.join()
    p44.join()
    p45.join()
    p46.join()
    p47.join()
    p48.join()
    p49.join()




    
    os.system('1_runpy_2.bat')

    finish = time.perf_counter()
    print(f'Successfully finished in {round((finish-start)/60, 2)} minute(s) bro')
