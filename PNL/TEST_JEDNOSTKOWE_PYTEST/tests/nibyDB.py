baza=[]
def loadDB():
    print("############## ŁADOWANIE BAZY ##############")
    global baza
    baza=[
        (1,"Marian"),
        (2,"Czesław"),
        (3,"Zenon"),
        (4,"Florian")
    ]

def getData():
    global baza
    return baza
def getOne(x):
    global baza
    return baza[x]