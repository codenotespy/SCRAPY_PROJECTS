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


cursor.execute("DROP TABLE IF EXISTS aa_otoyedekcim")
cursor.execute("CREATE TABLE IF NOT EXISTS aa_otoyedekcim (part_no TEXT, description TEXT, price TEXT, cur_url TEXT)")
connection.commit()
connection.close()





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

def urls_16():
    os.system('urls_16.bat')

def urls_17():
    os.system('urls_17.bat')

def urls_18():
    os.system('urls_18.bat')

def urls_19():
    os.system('urls_19.bat')

def urls_20():
    os.system('urls_20.bat')

def urls_20():
    os.system('urls_21.bat')

def urls_21():
    os.system('urls_22.bat')

def urls_22():
    os.system('urls_23.bat')

def urls_23():
    os.system('urls_23.bat')

def urls_24():
    os.system('urls_24.bat')

def urls_25():
    os.system('urls_25.bat')

def urls_26():
    os.system('urls_26.bat')

def urls_27():
    os.system('urls_27.bat')

def urls_28():
    os.system('urls_28.bat')

def urls_29():
    os.system('urls_29.bat')

def urls_29():
    os.system('urls_30.bat')

def urls_30():
    os.system('urls_31.bat')

def urls_31():
    os.system('urls_32.bat')

def urls_32():
    os.system('urls_32.bat')

def urls_33():
    os.system('urls_33.bat')

def urls_34():
    os.system('urls_34.bat')

def urls_35():
    os.system('urls_35.bat')

def urls_36():
    os.system('urls_36.bat')

def urls_37():
    os.system('urls_37.bat')

def urls_38():
    os.system('urls_38.bat')

def urls_38():
    os.system('urls_39.bat')

def urls_39():
    os.system('urls_40.bat')

def urls_40():
    os.system('urls_41.bat')

def urls_41():
    os.system('urls_41.bat')

def urls_42():
    os.system('urls_42.bat')

def urls_43():
    os.system('urls_43.bat')

def urls_44():
    os.system('urls_44.bat')

def urls_45():
    os.system('urls_45.bat')

def urls_46():
    os.system('urls_46.bat')

def urls_47():
    os.system('urls_47.bat')

def urls_47():
    os.system('urls_48.bat')

def urls_48():
    os.system('urls_49.bat')

def urls_49():
    os.system('urls_50.bat')

def urls_50():
    os.system('urls_50.bat')

def urls_51():
    os.system('urls_51.bat')

def urls_52():
    os.system('urls_52.bat')

def urls_53():
    os.system('urls_53.bat')

def urls_54():
    os.system('urls_54.bat')

def urls_55():
    os.system('urls_55.bat')

def urls_56():
    os.system('urls_56.bat')

def urls_56():
    os.system('urls_57.bat')

def urls_57():
    os.system('urls_58.bat')

def urls_58():
    os.system('urls_59.bat')

def urls_59():
    os.system('urls_59.bat')

def urls_60():
    os.system('urls_60.bat')

def urls_61():
    os.system('urls_61.bat')

def urls_62():
    os.system('urls_62.bat')

def urls_63():
    os.system('urls_63.bat')

def urls_64():
    os.system('urls_64.bat')

def urls_65():
    os.system('urls_65.bat')





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
u16 = multiprocessing.Process(target=urls_16)
u17 = multiprocessing.Process(target=urls_17)
u18 = multiprocessing.Process(target=urls_18)
u19 = multiprocessing.Process(target=urls_19)
u20 = multiprocessing.Process(target=urls_20)
u21 = multiprocessing.Process(target=urls_21)
u22 = multiprocessing.Process(target=urls_22)
u23 = multiprocessing.Process(target=urls_23)
u24 = multiprocessing.Process(target=urls_24)
u25 = multiprocessing.Process(target=urls_25)
u26 = multiprocessing.Process(target=urls_26)
u27 = multiprocessing.Process(target=urls_27)
u28 = multiprocessing.Process(target=urls_28)
u29 = multiprocessing.Process(target=urls_29)
u30 = multiprocessing.Process(target=urls_30)
u31 = multiprocessing.Process(target=urls_31)
u32 = multiprocessing.Process(target=urls_32)
u33 = multiprocessing.Process(target=urls_33)
u34 = multiprocessing.Process(target=urls_34)
u35 = multiprocessing.Process(target=urls_35)
u36 = multiprocessing.Process(target=urls_36)
u37 = multiprocessing.Process(target=urls_37)
u38 = multiprocessing.Process(target=urls_38)
u39 = multiprocessing.Process(target=urls_39)
u40 = multiprocessing.Process(target=urls_40)
u41 = multiprocessing.Process(target=urls_41)
u42 = multiprocessing.Process(target=urls_42)
u43 = multiprocessing.Process(target=urls_43)
u44 = multiprocessing.Process(target=urls_44)
u45 = multiprocessing.Process(target=urls_45)
u46 = multiprocessing.Process(target=urls_46)
u47 = multiprocessing.Process(target=urls_47)
u48 = multiprocessing.Process(target=urls_48)
u49 = multiprocessing.Process(target=urls_49)
u50 = multiprocessing.Process(target=urls_50)
u51 = multiprocessing.Process(target=urls_51)
u52 = multiprocessing.Process(target=urls_52)
u53 = multiprocessing.Process(target=urls_53)
u54 = multiprocessing.Process(target=urls_54)
u55 = multiprocessing.Process(target=urls_55)
u56 = multiprocessing.Process(target=urls_56)
u57 = multiprocessing.Process(target=urls_57)
u58 = multiprocessing.Process(target=urls_58)
u59 = multiprocessing.Process(target=urls_59)
u60 = multiprocessing.Process(target=urls_60)
u61 = multiprocessing.Process(target=urls_61)
u62 = multiprocessing.Process(target=urls_62)
u63 = multiprocessing.Process(target=urls_63)
u64 = multiprocessing.Process(target=urls_64)
u65 = multiprocessing.Process(target=urls_65)


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
    u17.start()
    u18.start()
    u19.start()
    u20.start()
    u21.start()
    u22.start()

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
    u17.join()
    u18.join()
    u19.join()
    u20.join()
    u21.join()
    u22.join()

    os.system('1_runmebaby_3.bat')

'''
if __name__ == '__main__':
    u23.start()
    u24.start()
    u25.start()
    u26.start()
    u27.start()
    u28.start()
    u29.start()
    u30.start()
    u31.start()
    u32.start()
    u33.start()
    u34.start()
    u35.start()
    u36.start()
    u37.start()
    u38.start()
    u39.start()
    u40.start()
    u41.start()
    u42.start()
    u43.start()
    u44.start()

    u23.join()
    u24.join()
    u25.join()
    u26.join()
    u27.join()
    u28.join()
    u29.join()
    u30.join()
    u31.join()
    u32.join()
    u33.join()
    u34.join()
    u35.join()
    u36.join()
    u37.join()
    u38.join()
    u39.join()
    u40.join()
    u41.join()
    u42.join()
    u43.join()
    u44.join()



if __name__ == '__main__':
    u45.start()
    u46.start()
    u47.start()
    u48.start()
    u49.start()
    u50.start()
    u51.start()
    u52.start()
    u53.start()
    u54.start()
    u55.start()
    u56.start()
    u57.start()
    u58.start()
    u59.start()
    u60.start()
    u61.start()
    u62.start()
    u63.start()
    u64.start()
    u65.start()

    u45.join()
    u46.join()
    u47.join()
    u48.join()
    u49.join()
    u50.join()
    u51.join()
    u52.join()
    u53.join()
    u54.join()
    u55.join()
    u56.join()
    u57.join()
    u58.join()
    u59.join()
    u60.join()
    u61.join()
    u62.join()
    u63.join()
    u64.join()
    u65.join()

    # finish = time.perf_counter()
    # print(f'Successfully finished in {round((finish-start)/60, 2)} minute(s) bro')

'''