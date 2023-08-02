import pyautogui
import sys
# print(sys.argv[1])
# sys.stdout.flush()
# kolko = int(sys.argv[1])
# Remainder = sys.argv[2]
import time

class Currency:
    def __init__(self, name, base, InventoryLocation):
        self.name = name
        self.base = base
        self.InventoryLocation = InventoryLocation

CurrencyList = [ Currency("ChaosOrb", 20, [725,370]),
         Currency("DivineOrb",10, [800,435]), Currency("OrbofAnnulment", 20, [225,365]), Currency ("ExaltedOrb", 10, [400,360]), Currency("OrbofAlteration", 20, [150,360]),
Currency("RegalOrb",  10,[580,535]), Currency("Jeweller'sOrb", 20, [150,525]), Currency("OrbofScouring", 30, [580,685]), Currency("OrbofUnmaking", 40,[660,600]),
Currency("AncientOrb", 20, [140,600]), Currency("VeiledChaosOrb",10,[810,370]), Currency("VaalOrb", 10,[810,690]), Currency("ChromaticOrb", 20, [300,535]),
Currency("SacredOrb",10,[650,685]), Currency("AwakenedSextant", 10,[575,535]), Currency("OrbofAlchemy", 10, [650,365]), Currency("OrbofFusing", 20, [225,530]), 
Currency("OrbofRegret", 40, [585,605])]

OfferCurrency = int(sys.argv[1])
OfferCurrencyType = None
for i in CurrencyList:
    if i.name == sys.argv[2]:
        OfferCurrencyType=i
        break
# OfferCurrency = 322
# OfferCurrencyType = CurrencyList[4]

kolko = float(OfferCurrency/OfferCurrencyType.base)
Columns = int(kolko/5)
Leftover = kolko%5
CalcIndex = 0


# print(kolko, CalcIndex, Columns, Remainder)




pyautogui.FAILSAFE = False 
pyautogui.PAUSE = 0.06


def From_Inv_1():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1720,y=810,duration=0.1)
    pyautogui.click(x=1720,y=880,duration=0.1)
    pyautogui.click(x=1720,y=940,duration=0.1)
    pyautogui.click(x=1720,y=1010,duration=0.1)
    pyautogui.click(x=1720,y=1080,duration=0.1)
##
    pyautogui.click(x=1721,y=810)
    pyautogui.click(x=1721,y=880)
    pyautogui.click(x=1721,y=940)
    pyautogui.click(x=1721,y=1010)
    pyautogui.click(x=1721,y=1080)
    pyautogui.keyUp("ctrl")

#  
def From_Inv_2():  
    pyautogui.keyDown("ctrl")

    pyautogui.click(x=1800,y=810,duration=0.1)
    pyautogui.click(x=1800,y=880,duration=0.1)
    pyautogui.click(x=1800,y=940,duration=0.1)
    pyautogui.click(x=1800,y=1010,duration=0.1)
    pyautogui.click(x=1800,y=1080,duration=0.1)
##
    pyautogui.click(x=1801,y=810)
    pyautogui.click(x=1801,y=880)
    pyautogui.click(x=1801,y=940)
    pyautogui.click(x=1801,y=1010)
    pyautogui.click(x=1801,y=1080)
    pyautogui.keyUp("ctrl")

#
def From_Inv_3():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1870,y=810,duration=0.1)
    pyautogui.click(x=1870,y=880,duration=0.1)
    pyautogui.click(x=1870,y=940,duration=0.1)
    pyautogui.click(x=1870,y=1010,duration=0.1)
    pyautogui.click(x=1870,y=1080,duration=0.1)
##
    pyautogui.click(x=1871,y=810)
    pyautogui.click(x=1871,y=880)
    pyautogui.click(x=1871,y=940)
    pyautogui.click(x=1871,y=1010)
    pyautogui.click(x=1871,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_4():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1940,y=810,duration=0.1)
    pyautogui.click(x=1940,y=880,duration=0.1)
    pyautogui.click(x=1940,y=940,duration=0.1)
    pyautogui.click(x=1940,y=1010,duration=0.1)
    pyautogui.click(x=1940,y=1080,duration=0.1)
##
    pyautogui.click(x=1941,y=810)
    pyautogui.click(x=1941,y=880)
    pyautogui.click(x=1941,y=940)
    pyautogui.click(x=1941,y=1010)
    pyautogui.click(x=1941,y=1080)
    pyautogui.keyUp("ctrl")
#  
def From_Inv_5():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2010,y=810,duration=0.1)
    pyautogui.click(x=2010,y=880,duration=0.1)
    pyautogui.click(x=2010,y=940,duration=0.1)
    pyautogui.click(x=2010,y=1010,duration=0.1)
    pyautogui.click(x=2010,y=1080,duration=0.1)
##
    
    pyautogui.click(x=2011,y=810)
    pyautogui.click(x=2011,y=880)
    pyautogui.click(x=2011,y=940)
    pyautogui.click(x=2011,y=1010)
    pyautogui.click(x=2011,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_6():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2080,y=810,duration=0.1)
    pyautogui.click(x=2080,y=880,duration=0.1)
    pyautogui.click(x=2080,y=940,duration=0.1)
    pyautogui.click(x=2080,y=1010,duration=0.1)
    pyautogui.click(x=2080,y=1080,duration=0.1)
#
    pyautogui.click(x=2081,y=810)
    pyautogui.click(x=2081,y=880)
    pyautogui.click(x=2081,y=940)
    pyautogui.click(x=2081,y=1010)
    pyautogui.click(x=2081,y=1080)
    pyautogui.keyUp("ctrl")
##
def From_Inv_7():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2150,y=810,duration=0.1)
    pyautogui.click(x=2150,y=880,duration=0.1)
    pyautogui.click(x=2150,y=940,duration=0.1)
    pyautogui.click(x=2150,y=1010,duration=0.1)
    pyautogui.click(x=2150,y=1080,duration=0.1)
##
    pyautogui.click(x=2151,y=810)
    pyautogui.click(x=2151,y=880)
    pyautogui.click(x=2151,y=940)
    pyautogui.click(x=2151,y=1010)
    pyautogui.click(x=2151,y=1080)
    pyautogui.keyUp("ctrl")

#
def From_Inv_8():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2220,y=810,duration=0.1)
    pyautogui.click(x=2220,y=880,duration=0.1)
    pyautogui.click(x=2220,y=940,duration=0.1)
    pyautogui.click(x=2220,y=1010,duration=0.1)
    pyautogui.click(x=2220,y=1080,duration=0.1)
##
    pyautogui.click(x=2221,y=810)
    pyautogui.click(x=2221,y=880)
    pyautogui.click(x=2221,y=940)
    pyautogui.click(x=2221,y=1010)
    pyautogui.click(x=2221,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_9():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2290,y=810,duration=0.1)
    pyautogui.click(x=2290,y=880,duration=0.1)
    pyautogui.click(x=2290,y=940,duration=0.1)
    pyautogui.click(x=2290,y=1010,duration=0.1)
    pyautogui.click(x=2290,y=1080,duration=0.1)
##
    pyautogui.click(x=2291,y=810)
    pyautogui.click(x=2291,y=880)
    pyautogui.click(x=2291,y=940)
    pyautogui.click(x=2291,y=1010)
    pyautogui.click(x=2291,y=1080)
    pyautogui.keyUp("ctrl")

#
def From_Inv_10():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2360,y=810,duration=0.1)
    pyautogui.click(x=2360,y=880,duration=0.1)
    pyautogui.click(x=2360,y=940,duration=0.1)
    pyautogui.click(x=2360,y=1010,duration=0.1)
    pyautogui.click(x=2360,y=1080,duration=0.1)
##
    pyautogui.click(x=2361,y=810)
    pyautogui.click(x=2361,y=880)
    pyautogui.click(x=2361,y=940)
    pyautogui.click(x=2361,y=1010)
    pyautogui.click(x=2361,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_11():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2430,y=810,duration=0.1)
    pyautogui.click(x=2430,y=880,duration=0.1)
    pyautogui.click(x=2430,y=940,duration=0.1)
    pyautogui.click(x=2430,y=1010,duration=0.1)
    pyautogui.click(x=2430,y=1080,duration=0.1)
##
    pyautogui.click(x=2431,y=810)
    pyautogui.click(x=2431,y=880)
    pyautogui.click(x=2431,y=940)
    pyautogui.click(x=2431,y=1010)
    pyautogui.click(x=2431,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_12():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2500,y=810,duration=0.1)
    pyautogui.click(x=2500,y=880,duration=0.1)
    pyautogui.click(x=2500,y=940,duration=0.1)
    pyautogui.click(x=2500,y=1010,duration=0.1)
    pyautogui.click(x=2500,y=1080,duration=0.1)
##
    pyautogui.click(x=2501,y=810)
    pyautogui.click(x=2501,y=880)
    pyautogui.click(x=2501,y=940)
    pyautogui.click(x=2501,y=1010)
    pyautogui.click(x=2501,y=1080)
    pyautogui.keyUp("ctrl")

Function_List = [From_Inv_1, From_Inv_2, From_Inv_3,From_Inv_4,From_Inv_5,From_Inv_6,From_Inv_7,From_Inv_8,From_Inv_9,From_Inv_10,From_Inv_11,From_Inv_12]
time.sleep(1)
for i in range(0,Columns):
    Function_List[i]()
    CalcIndex +=1
    
if Leftover>0 and Leftover<6:
    Function_List[CalcIndex]()
        



    

