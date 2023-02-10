#import sesuatu
import os
import time

#buat ngubah warna text
Noco = '\033[0m'
Redco = '\033[91m'
Greco = '\033[92m'
Bluco = '\033[94m'
Yelco = '\033[93m'
WGrecoCo = '\033[42m'

#variable:lokasi dimana suatu folder & daftar nama folder
folderloc = []
foldernm = []

#variable:lokasi dimana suatu file & daftar nama file
fileloc = []
filenm = []

#daftar file yang terdeteksi kata yang dicari(nama file & lokasi file)
filefound = []
locfound = []
filenotfound = []
fileskipped = []

#untuk digunakan sebagai hitungan saat scan folder
count = 0

def line():
    print(Yelco + "--------------------------------------------------" + Noco)

def ender():
    print()
    print()
    line()
    print("OK,THANK YOU")
    line()
    print()
    print()

print()
print()
print(Yelco + "--------------------------------------------------" + Noco)
jawab = input('Wich Folder?')
foldernm.append(jawab)
folderloc.append(os.getcwd())

nyari = input("What Word You Search?:")

#scan isi folder
while count<len(folderloc):
    os.chdir(folderloc[count])
    print()
    print("checking" + Bluco,foldernm[count] + Noco + ":")
    #print(os.getcwd())
    try:
        isinya = os.listdir(foldernm[count])
    except PermissionError:
        print("*skip")
    #print()
    #print(foldernm[count],":")#infodoang
    #print(isinya)#infodoang
    #print("countnya:",count)
    for i in range(len(isinya)):
        if os.path.isdir(folderloc[count]+"/"+foldernm[count]+"/"+isinya[i]):
            folderloc.append(folderloc[count]+"/"+foldernm[count])
            foldernm.append(isinya[i])
            #print(Bluco + isinya[i] + Noco,"itu direktori")#infodoang
        elif os.path.isfile(folderloc[count]+"/"+foldernm[count]+"/"+isinya[i]):
            #print()
            #print(Greco + isinya[i] + Noco,"itu file")#infodoang
            filenm.append(isinya[i])
            fileloc.append(folderloc[count]+"/"+foldernm[count]+"/"+isinya[i])
            #print("countnya:",count)
            #print("filelocnya:",len(fileloc))
            #print("jumlah i:",i)
            #print("lokasi file:",fileloc)
            os.chdir(folderloc[count]+"/"+foldernm[count])
            #os.rename(isinya[i],'text.txt')
            with open(isinya[i],'r') as fp:
                try:
                    print("Scan" + Greco,isinya[i] + Noco + ":")
                    baca = fp.read()
                    #print(baca)#infodoang
                    if baca.find(nyari)!= -1:
                        filefound.append(isinya[i])
                        locfound.append(folderloc[count]+"/"+foldernm[count]+"/"+isinya[i])
                        print(WGrecoCo + "Found In" + Noco + Greco,isinya[i] + Noco)
                    else:
                        filenotfound.append(isinya[i])
                        print(Redco + "Not Found In" + Noco + Greco,isinya[i] + Noco)
                except UnicodeDecodeError:
                    fileskipped.append(isinya[i])
                    print("*Skip",isinya[i])
    count += 1
print()
print()
print(Bluco + f'{len(foldernm)}' + Noco,"Folder has been checked")
print(Greco + f'{len(filenm)}' + Noco,"File is detected")
print(Redco + f'{len(fileskipped)}' + Noco,"File cant read by program")
print(Yelco + f'{len(filenotfound)}' + Noco,"File not contain the word")
line()
print(Greco + f'{len(filefound)}' + Noco,"File contain the word:")
for a in range(len(filefound)):
    print(Greco + filefound[a] + Noco)
line()
print()
#jawaban akhir
jeda = 0
def seeloc():
    global jeda
    if len(locfound)>5:
        for s in range(len(locfound)):
            print(Greco + filefound[s] + Noco)
            print(locfound[s])
            time.sleep(jeda)
    else:
        for p in range(len(locfound)):
            print()
            print(Greco + filefound[p] + Noco)
            print(locfound[p])
def detiknya():
    global jeda
    while jeda==0:
        try:
            jeda = float(input("Per what Seconds?"))
        except ValueError:
            jeda = 0
def nanya():
    global jeda
    pilih = ""
    while pilih!="y" and pilih!="n":
        pilih = input("Want To Use Timer(Location/Seconds)?(y/n):")
    if pilih=="y":
        detiknya()
        print()
        line()
        seeloc()
        line()
        print()
        print()
        line()
        input("click enter to out")
        line()
        ender()
        exit()
    else:
        print()
        line()
        seeloc()
        line()
        print()
        print()
        line()
        input("click enter to out")
        line()
        ender()
        exit()
jawaban = ""
while jawaban!="n" and jawaban!="y":
    jawaban = input("Want To Know The Location?(y/n):")
if jawaban == "y":
    if len(locfound)>5:
        nanya()
    else:
        print()
        line()
        seeloc()
        line()
        print()
        print()
        line()
        input("clik enter to out")
        line()
        ender()
        exit()
else:
    ender()
    exit()