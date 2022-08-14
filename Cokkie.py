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

https://github.com/Space-Banane/Cokkie

This Programm can USED by anyone
but DONT do anything BAD with this programm
ANYWAY have fun :)

Cokkie© 2022 April 
"""


from CokkieBase import *
import random







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
    
    """Settings
    """
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
    if allowsaving == True:
        with open(filename,"w",encoding='utf-8') as f:
            f.write(data)
        if debug == True:
         print("Cokkie (Cokkie.py) : Data Saved")
        else:
         pass
    else:
        print("Sorry Saveing is not allowed by your script")

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
        x = file.read
        return x
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



    
