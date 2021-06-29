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

cursor.execute("DROP TABLE IF EXISTS aa_aloparca")
cursor.execute("DROP TABLE IF EXISTS aa_aloparca_oem")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_aloparca (brand TEXT, part_no TEXT, description TEXT, link TEXT, price TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_aloparca_oem (brand TEXT, part_no TEXT, cross_brand TEXT, cross_ref TEXT, link TEXT)")

connection.commit()
connection.close()








def join1():
    os.system('alfa_romeo\\0-run.bat')
    os.system('alfa_romeo\\1-run.bat')
    os.system('alfa_romeo\\2-run.bat')
    os.system('alfa_romeo\\3-run.bat')
    os.system('alfa_romeo\\4-run.bat')

def join2():
    os.system('aston_martin\\0-run.bat')
    os.system('aston_martin\\1-run.bat')
    os.system('aston_martin\\2-run.bat')
    os.system('aston_martin\\3-run.bat')
    os.system('aston_martin\\4-run.bat')

def join3():
    os.system('audi\\0-run.bat')
    os.system('audi\\1-run.bat')
    os.system('audi\\2-run.bat')
    os.system('audi\\3-run.bat')
    os.system('audi\\4-run.bat')

def join4():
    os.system('bentley\\0-run.bat')
    os.system('bentley\\1-run.bat')
    os.system('bentley\\2-run.bat')
    os.system('bentley\\3-run.bat')
    os.system('bentley\\4-run.bat')

def join5():
    os.system('bmw\\0-run.bat')
    os.system('bmw\\1-run.bat')
    os.system('bmw\\2-run.bat')
    os.system('bmw\\3-run.bat')
    os.system('bmw\\4-run.bat')

def join6():
    os.system('cadillac\\0-run.bat')
    os.system('cadillac\\1-run.bat')
    os.system('cadillac\\2-run.bat')
    os.system('cadillac\\3-run.bat')
    os.system('cadillac\\4-run.bat')

def join7():
    os.system('chevrolet\\0-run.bat')
    os.system('chevrolet\\1-run.bat')
    os.system('chevrolet\\2-run.bat')
    os.system('chevrolet\\3-run.bat')
    os.system('chevrolet\\4-run.bat')

def join8():
    os.system('chrysler\\0-run.bat')
    os.system('chrysler\\1-run.bat')
    os.system('chrysler\\2-run.bat')
    os.system('chrysler\\3-run.bat')
    os.system('chrysler\\4-run.bat')

def join9():
    os.system('citroen\\0-run.bat')
    os.system('citroen\\1-run.bat')
    os.system('citroen\\2-run.bat')
    os.system('citroen\\3-run.bat')
    os.system('citroen\\4-run.bat')

def join10():
    os.system('dacia\\0-run.bat')
    os.system('dacia\\1-run.bat')
    os.system('dacia\\2-run.bat')
    os.system('dacia\\3-run.bat')
    os.system('dacia\\4-run.bat')

def join11():
    os.system('daewoo\\0-run.bat')
    os.system('daewoo\\1-run.bat')
    os.system('daewoo\\2-run.bat')
    os.system('daewoo\\3-run.bat')
    os.system('daewoo\\4-run.bat')

def join12():
    os.system('daihatsu\\0-run.bat')
    os.system('daihatsu\\1-run.bat')
    os.system('daihatsu\\2-run.bat')
    os.system('daihatsu\\3-run.bat')
    os.system('daihatsu\\4-run.bat')

def join13():
    os.system('dodge\\0-run.bat')
    os.system('dodge\\1-run.bat')
    os.system('dodge\\2-run.bat')
    os.system('dodge\\3-run.bat')
    os.system('dodge\\4-run.bat')

def join14():
    os.system('ferrari\\0-run.bat')
    os.system('ferrari\\1-run.bat')
    os.system('ferrari\\2-run.bat')
    os.system('ferrari\\3-run.bat')
    os.system('ferrari\\4-run.bat')

def join15():
    os.system('fiat\\0-run.bat')
    os.system('fiat\\1-run.bat')
    os.system('fiat\\2-run.bat')
    os.system('fiat\\3-run.bat')
    os.system('fiat\\4-run.bat')

def join16():
    os.system('ford\\0-run.bat')
    os.system('ford\\1-run.bat')
    os.system('ford\\2-run.bat')
    os.system('ford\\3-run.bat')
    os.system('ford\\4-run.bat')

def join17():
    os.system('honda\\0-run.bat')
    os.system('honda\\1-run.bat')
    os.system('honda\\2-run.bat')
    os.system('honda\\3-run.bat')
    os.system('honda\\4-run.bat')

def join18():
    os.system('hyundai\\0-run.bat')
    os.system('hyundai\\1-run.bat')
    os.system('hyundai\\2-run.bat')
    os.system('hyundai\\3-run.bat')
    os.system('hyundai\\4-run.bat')

def join19():
    os.system('isuzu\\0-run.bat')
    os.system('isuzu\\1-run.bat')
    os.system('isuzu\\2-run.bat')
    os.system('isuzu\\3-run.bat')
    os.system('isuzu\\4-run.bat')

def join20():
    os.system('iveco\\0-run.bat')
    os.system('iveco\\1-run.bat')
    os.system('iveco\\2-run.bat')
    os.system('iveco\\3-run.bat')
    os.system('iveco\\4-run.bat')

def join21():
    os.system('jaguar\\0-run.bat')
    os.system('jaguar\\1-run.bat')
    os.system('jaguar\\2-run.bat')
    os.system('jaguar\\3-run.bat')
    os.system('jaguar\\4-run.bat')

def join22():
    os.system('jeep\\0-run.bat')
    os.system('jeep\\1-run.bat')
    os.system('jeep\\2-run.bat')
    os.system('jeep\\3-run.bat')
    os.system('jeep\\4-run.bat')

def join23():
    os.system('kia\\0-run.bat')
    os.system('kia\\1-run.bat')
    os.system('kia\\2-run.bat')
    os.system('kia\\3-run.bat')
    os.system('kia\\4-run.bat')

def join24():
    os.system('lada\\0-run.bat')
    os.system('lada\\1-run.bat')
    os.system('lada\\2-run.bat')
    os.system('lada\\3-run.bat')
    os.system('lada\\4-run.bat')

def join25():
    os.system('lamborghini\\0-run.bat')
    os.system('lamborghini\\1-run.bat')
    os.system('lamborghini\\2-run.bat')
    os.system('lamborghini\\3-run.bat')
    os.system('lamborghini\\4-run.bat')

def join26():
    os.system('lancia\\0-run.bat')
    os.system('lancia\\1-run.bat')
    os.system('lancia\\2-run.bat')
    os.system('lancia\\3-run.bat')
    os.system('lancia\\4-run.bat')

def join27():
    os.system('land_rover\\0-run.bat')
    os.system('land_rover\\1-run.bat')
    os.system('land_rover\\2-run.bat')
    os.system('land_rover\\3-run.bat')
    os.system('land_rover\\4-run.bat')

def join28():
    os.system('maserati\\0-run.bat')
    os.system('maserati\\1-run.bat')
    os.system('maserati\\2-run.bat')
    os.system('maserati\\3-run.bat')
    os.system('maserati\\4-run.bat')

def join29():
    os.system('mazda\\0-run.bat')
    os.system('mazda\\1-run.bat')
    os.system('mazda\\2-run.bat')
    os.system('mazda\\3-run.bat')
    os.system('mazda\\4-run.bat')

def join30():
    os.system('mercedes_benz\\0-run.bat')
    os.system('mercedes_benz\\1-run.bat')
    os.system('mercedes_benz\\2-run.bat')
    os.system('mercedes_benz\\3-run.bat')
    os.system('mercedes_benz\\4-run.bat')

def join31():
    os.system('mini\\0-run.bat')
    os.system('mini\\1-run.bat')
    os.system('mini\\2-run.bat')
    os.system('mini\\3-run.bat')
    os.system('mini\\4-run.bat')

def join32():
    os.system('mitsubishi\\0-run.bat')
    os.system('mitsubishi\\1-run.bat')
    os.system('mitsubishi\\2-run.bat')
    os.system('mitsubishi\\3-run.bat')
    os.system('mitsubishi\\4-run.bat')

def join33():
    os.system('nissan\\0-run.bat')
    os.system('nissan\\1-run.bat')
    os.system('nissan\\2-run.bat')
    os.system('nissan\\3-run.bat')
    os.system('nissan\\4-run.bat')

def join34():
    os.system('opel\\0-run.bat')
    os.system('opel\\1-run.bat')
    os.system('opel\\2-run.bat')
    os.system('opel\\3-run.bat')
    os.system('opel\\4-run.bat')

def join35():
    os.system('peugeot\\0-run.bat')
    os.system('peugeot\\1-run.bat')
    os.system('peugeot\\2-run.bat')
    os.system('peugeot\\3-run.bat')
    os.system('peugeot\\4-run.bat')

def join36():
    os.system('porsche\\0-run.bat')
    os.system('porsche\\1-run.bat')
    os.system('porsche\\2-run.bat')
    os.system('porsche\\3-run.bat')
    os.system('porsche\\4-run.bat')

def join37():
    os.system('renault\\0-run.bat')
    os.system('renault\\1-run.bat')
    os.system('renault\\2-run.bat')
    os.system('renault\\3-run.bat')
    os.system('renault\\4-run.bat')

def join38():
    os.system('renault_trucks\\0-run.bat')
    os.system('renault_trucks\\1-run.bat')
    os.system('renault_trucks\\2-run.bat')
    os.system('renault_trucks\\3-run.bat')
    os.system('renault_trucks\\4-run.bat')

def join39():
    os.system('rolls_royce\\0-run.bat')
    os.system('rolls_royce\\1-run.bat')
    os.system('rolls_royce\\2-run.bat')
    os.system('rolls_royce\\3-run.bat')
    os.system('rolls_royce\\4-run.bat')

def join40():
    os.system('seat\\0-run.bat')
    os.system('seat\\1-run.bat')
    os.system('seat\\2-run.bat')
    os.system('seat\\3-run.bat')
    os.system('seat\\4-run.bat')

def join41():
    os.system('skoda\\0-run.bat')
    os.system('skoda\\1-run.bat')
    os.system('skoda\\2-run.bat')
    os.system('skoda\\3-run.bat')
    os.system('skoda\\4-run.bat')

def join42():
    os.system('smart\\0-run.bat')
    os.system('smart\\1-run.bat')
    os.system('smart\\2-run.bat')
    os.system('smart\\3-run.bat')
    os.system('smart\\4-run.bat')

def join43():
    os.system('subaru\\0-run.bat')
    os.system('subaru\\1-run.bat')
    os.system('subaru\\2-run.bat')
    os.system('subaru\\3-run.bat')
    os.system('subaru\\4-run.bat')

def join44():
    os.system('suzuki\\0-run.bat')
    os.system('suzuki\\1-run.bat')
    os.system('suzuki\\2-run.bat')
    os.system('suzuki\\3-run.bat')
    os.system('suzuki\\4-run.bat')

def join45():
    os.system('tata\\0-run.bat')
    os.system('tata\\1-run.bat')
    os.system('tata\\2-run.bat')
    os.system('tata\\3-run.bat')
    os.system('tata\\4-run.bat')

def join46():
    os.system('tofas\\0-run.bat')
    os.system('tofas\\1-run.bat')
    os.system('tofas\\2-run.bat')
    os.system('tofas\\3-run.bat')
    os.system('tofas\\4-run.bat')

def join47():
    os.system('toyata\\0-run.bat')
    os.system('toyata\\1-run.bat')
    os.system('toyata\\2-run.bat')
    os.system('toyata\\3-run.bat')
    os.system('toyata\\4-run.bat')

def join48():
    os.system('volvo\\0-run.bat')
    os.system('volvo\\1-run.bat')
    os.system('volvo\\2-run.bat')
    os.system('volvo\\3-run.bat')
    os.system('volvo\\4-run.bat')

def join49():
    os.system('vw\\0-run.bat')
    os.system('vw\\1-run.bat')
    os.system('vw\\2-run.bat')
    os.system('vw\\3-run.bat')
    os.system('vw\\4-run.bat')

def join50():
    os.system('rover\\0-run.bat')
    os.system('rover\\1-run.bat')
    os.system('rover\\2-run.bat')
    os.system('rover\\3-run.bat')
    os.system('rover\\4-run.bat')



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
p50 = multiprocessing.Process(target=join50)

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
    p50.start()

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
    p50.join()
    
    finish = time.perf_counter()
    print(f'Successfully finished in {round(finish-start, 2)} second(s) bro')
