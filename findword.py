#Import Something
import os
import time

#For "Coloring" Text
Noco = '\033[0m'
Redco = '\033[91m'
Greco = '\033[92m'
Bluco = '\033[94m'
Yelco = '\033[93m'
WGrecoCo = '\033[42m'

#List "Folder"(Name & Location)
folderloc = []
foldernm = []


#List "File"(Name & Location)
fileloc = []
filenm = []

#List File That "Contain" Word(Name & Location)
filefound = []
locfound = []

#List File That "Not Contain" Word(Name & Location)
filenotfound = []
fileskipped = []

#Used For "Counting" While Scanning Folder
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
answer = input('Wich Folder?')
foldernm.append(answer)
folderloc.append(os.getcwd())

search = input("What Word You Search?:")

#Scan "Inside of Folder"
while count<len(folderloc):
    os.chdir(folderloc[count])
    print()
    print("checking" + Bluco,foldernm[count] + Noco + ":")
    try:
        inside = os.listdir(foldernm[count])
    except PermissionError:
        print("*skip")
    
    for i in range(len(inside)):
        if os.path.isdir(folderloc[count]+"/"+foldernm[count]+"/"+inside[i]):
            folderloc.append(folderloc[count]+"/"+foldernm[count])
            foldernm.append(inside[i])
            
        elif os.path.isfile(folderloc[count]+"/"+foldernm[count]+"/"+inside[i]):
            
            filenm.append(inside[i])
            fileloc.append(folderloc[count]+"/"+foldernm[count]+"/"+inside[i])
            
            os.chdir(folderloc[count]+"/"+foldernm[count])
            
            with open(inside[i],'r') as fp:
                try:
                    print("Scan" + Greco,inside[i] + Noco + ":")
                    baca = fp.read()
                    
                    if baca.find(search)!= -1:
                        filefound.append(inside[i])
                        locfound.append(folderloc[count]+"/"+foldernm[count]+"/"+inside[i])
                        print(WGrecoCo + "Found In" + Noco + Greco,inside[i] + Noco)
                    else:
                        filenotfound.append(inside[i])
                        print(Redco + "Not Found In" + Noco + Greco,inside[i] + Noco)
                except UnicodeDecodeError:
                    fileskipped.append(inside[i])
                    print("*Skip",inside[i])
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
#Last Answer
pause = 0
def seeloc():
    global pause
    if len(locfound)>5:
        for s in range(len(locfound)):
            print(Greco + filefound[s] + Noco)
            print(locfound[s])
            time.sleep(pause)
    else:
        for p in range(len(locfound)):
            print()
            print(Greco + filefound[p] + Noco)
            print(locfound[p])
def theseconds():
    global pause
    while pause==0:
        try:
            pause = float(input("Per what Seconds?"))
        except ValueError:
            pause = 0
def asking():
    global pause
    choose = ""
    while choose!="y" and choose!="n":
        choose = input("Want To Use Timer(Location/Seconds)?(y/n):")
    if choose=="y":
        theseconds()
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
theanswer = ""
while theanswer!="n" and theanswer!="y":
    theanswer = input("Want To Know The Location?(y/n):")
if theanswer == "y":
    if len(locfound)>5:
        asking()
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