"""
COKKIE
~~~~~~~~~~~~~~~~~~~

FUNCTIONS :
-Read()
-Write()
-Settings()
-About()
-Version()
-Trigger()

https://github.com/Bigboi-Python/Cokkie

This Programm can USED by anyone
but DONT do anything BAD with this programm
ANYWAY have fun :)

Cokkie© 2022 April 
"""


from CokkieBase import *
import random
Live_Lizenz = ''.join(random.choice([chr(i) for i in range(ord('a'),ord('z'))]) for _ in range(35))

if __name__ == "Cokkie":
    pass 
else:
    print("Please rename the file to Cokkie.py")
    print("You have 0 Seconds to end the programm")
    quit()




def About(what):
    if what == "func":
        print("there some Funtions that u can use")
        print("1. Saving a data/varible")
        print("2. Reading a data/varible")
        print("3. Settings Settings")
        print("4. Version tells u the current version or lets u print out a own version")
        print("5. About this boi here")
        print("6. Trigger trigger an action")
    if what == "Cokkie":
        print("Cokkie is a varrible saving way to store data over python restarts")
    if what == "timesused":
        print("Read:",timesusedread)
        print("Write:",timesusedwrite)
    

def Settings(settings,onoff):
    if settings == "startmessages":
        if onoff == "off":
            startmessages = False
        if onoff == "on":
            startmessages = True
    if settings == "allowSaving":
        if onoff == "on":
            allowsaving = True
        if onoff == "off":
            allowsaving = False
    if settings == "allowreading":
        if onoff == "on":
            allowreading = True
        if onoff == "off":
            allowreading = False
    if settings == "Where : Text":
        if onoff == "on":
            thing1 = True
        if onoff == "off":
            thing1 = False
    if settings == "debug":
        if onoff == "on":
            debug = True
        if onoff == "off":
            debug = False

def Version(ver):
    if ver == "":
        print("This is currently version 1.8")
    else:
        print("This is currenty version",ver)
    
def CokkieClear():
    for i in range(100):
        print("")
    timesusedwrite = 0
    timesusedread = 0

def Save(data,filename):
    data = str(data)
    timesusedwrite =+ 1
    if timesusedwrite > 100:
        print("You used Cokkie now over 100 Times time to clean up some Data")
    if allowsaving == True:
        file = open(filename,'w')
        file.write(data)
        file.close()
        if debug == True:
         print("Cokkie (Cokkie.py) : Data Saved")
        else:
         pass
    else:
        print("Sorry Reading is not allowed by your script")

def Read(filename):
    timesusedread =+ 1
    if timesusedread > 100:
        print("You used Cokkie now over 100 Times time to clean up some Data")
    if allowreading == True:
        file = open(filename,'r')
        print(file.read())
        file.close()
        if debug == True:
         print("Cokkie (Cokkie.py) : Data Read")
        else:
         pass
    else:
        print("Sorry Reading is not allowed by your script")

def Savevar(filename):
    file = open(filename,'r')
    file.read()
    file.close()
    print("Cokkie (Cokkie.py) : Saved in a var")
    
def Clear():
    CokkieClear()
    print("Cokkie (Cokkie.py) : Clear Triggert")

def Triger(type):
    if type == "reconnect":
        print("Cokkie is now up and reconnected :)")
    if type == "clear":
        Clear()



    
######## START NORMAL STUFF ########
if thing1 == True:
    print("Cokkie : please always use as fileending .txt \n -Cokkie 2022")
else:
 print("please always use as fileending .txt \n -Cokkie 2022")
 
print("")

if startmessages == True:
    print("you can disable this and the next messages by putting under the imports of your programm settings(thetypeoffsetting,on/off) :) ")
