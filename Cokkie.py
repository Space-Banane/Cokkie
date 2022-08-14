"""
COKKIE
~~~~~~~~~~~~~~~~~~~

FUNCTIONS :
-Read()
-Write()
-Settings()

https://github.com/Space-Banane/Cokkie

This Programm can USED by anyone
but DONT do anything BAD with this programm
ANYWAY have fun :)

Cokkie© 2022 April 
"""
import random
debug = True

def Settings(settings,onoff):
    """Change settings"""
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


def Save(data,filename):
    """Save Data in a given file"""
    data = str(data)
    with open(filename,"w",encoding='utf-8') as f:
        f.write(data)
    if debug == True:
     print("Cokkie (Cokkie.py) : Data Saved")
    else:
     pass

def Read(filename):
    """Returns Data from a given file"""
    file = open(filename,'r')
    print(file.read())
    file.close()
    if debug == True:
     print("Cokkie (Cokkie.py) : Returnd data ")
    else:
     pass
    x = file.read
    return x
