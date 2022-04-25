import os, time, sys

def clear():
    os.system("clear")


clear()

if os.getuid() != 0:
    print("Try with sudo !!")
    sys.exit()


banner="""

                                        RiseTo Z-Book Downloader
                                        [A RiseToDev Script]


[1] Model Yayınları
[2] Günay Yayınları
                                        
""" 


branch_banner="""

[1] Turkish (Comming Soon)
[2] Maths
[3] Science


"""


print(banner)

publishing = int(input("Choose A Publishing ===> "))

while True:
    if publishing != int:
        print("Invalid Options Try Again !!")
    elif publishing == 1:
        os.system('curl --insecure https://gitlab.com/RiseToDev751/rise_to_z-book_downloader/-/raw/main/ModelKutuphane.fernus -o kitap_model.fernus')
        os.system("mv ./kitap_model.fernus ~/")
        os.system("link ~/kitap_model.fernus ~/Masaüstü")
        break
    elif publishing == 2:
        clear()
        print(branch_banner)
        branch = int(input("Choose A Branch ===> "))
        if branch != int:
            print("Invalid Options Try Again !!")
        elif branch == 2:
            os.system('curl --insecure https://gitlab.com/RiseToDev751/rise_to_z-book_downloader/-/raw/main/matgunay.fernus -o kitap_matgunay.fernus')
            os.system("mv ./kitap_matgunay.fernus ~/")
            os.system("link ~/kitap_matgunay.fernus ~/Masaüstü")
            break
        elif branch == 3:
            os.system('curl --insecure https://gitlab.com/RiseToDev751/rise_to_z-book_downloader/-/raw/main/GunayKutuphane.fernus -o kitap_fengunay.fernus')
            os.system("mv ./kitap_fengunay.fernus ~/")
            os.system("link ~/kitap_fengunay.fernus ~/Masaüstü")
            break
            


