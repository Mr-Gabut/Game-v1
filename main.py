import os,sys,time,random

#Warna
h="\33[0;32m"
m="\33[31;1m"
p="\33[37;1m"
k="\33[1;33m"

nyawa = 10
level = 1

banner = f"""
{p}==============================
{h}TEBAK ANGKA {p}==> {k}By {p}: {k}Mr Gabut
{p}==============================
{m}MASUKAN {p}ANGKA {m}YANG
SESUAI DENGAN {p}RANDOM
{p}========================="""
ka = random.randint(1,100)
while True:
    print (banner)
    print (f"{h}Nyawa kamu saat ini{m}", nyawa)
    print (f"{p}=========================")
    kontol = int(input(f"{k}Angka Keberuntungan : {p}"))
    if kontol > ka:
        time.sleep(2)
        nyawa -= 1
        print (f"{m}\n--------------------\n{p}Angka kamu kebesaran{m}\n--------------------")
    elif kontol < ka:
        time.sleep(2)
        nyawa -= 1
        print(f"{m}\n--------------------\n{p}Angka kamu kekecilan{m}\n--------------------")
    else:
        time.sleep(3)
        print (f"{h}\n-----------------------------\n{k}Angka kamu sesuai harapan\n{h}-----------------------------\n{p}Semoga apa yang kamu inginkan \nbisa tercapai Amiin....\n{h}-----------------------------{p}")
        input(f"{m}ENTER{p}")
        break
    if nyawa == 0:
        print (f"""{h}=============\n{m}  GAME OVER\n{h}=============""")
        time.sleep(3)
        input(f"{m}Enter {k}jika mau bermain lagi\n\n{m}CTRL + c {k}Untuk keluar :)")
        nyawa = 10
        os.system('python main.py')
