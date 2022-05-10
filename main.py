import os, time, sys
from modules import *

netcheck()

clear()
os.system("mkdir ~/.rz-books")

def chx(cmd):
    if os.path.isfile(cmd) == True:
        pass
    elif os.path.isfile(cmd) == False:
        print(Kirmizi+'Please run setup.sh in "Etap-Yetkili" User ')
        sys.exit()


chx("/usr/bin/git")
chx("/usr/bin/curl")
chx("/usr/bin/wine")


banner="""

                                        RiseTo Z-Book Downloader
                                        [A RiseToDev Script]
                                        (Supported Fernus Base Z-Books)


                                        
""" 

yayinlar = []   

def setup(pubname):
    clear()
    os.system("curl --insecure https://manage.frns.in/"+yayinlar[pubname]+"Kutuphane.fernus -o "+yayinlar[pubname]+"Kutuphane.fernus")
    os.system("mv "+yayinlar[pubname]+"Kutuphane.fernus ~/.rz-books")
    os.system("chmod 777 ~/.rz-books/"+yayinlar[pubname]+"Kutuphane.fernus")
    os.system("link ~/.rz-books/"+yayinlar[pubname]+"Kitap ~/Masaüstü/"+yayinlar[pubname]+"Kutuphane.fernus")


print(AcikCamgobegi+banner)

file = open("pubname.py","r")
sayac = 0
for i in file:
    while True:
        txt = file.readline()
        name = txt.split(" =")
        yayinlar.append(name[0])
        print("[",sayac,"]"+name[0]+" Yayınları")
        sayac+=1
        if sayac == 19:
            break
publishing = int(input(Kirmizi+"Choose A Publishing ===> "))

value = 0

for i in yayinlar:
    value+=1


if publishing <= value:
    setup(publishing)
else: 
    print(Kirmizi+"Please! Type Correct Options")
    exit()
