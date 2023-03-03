import pyautogui
import sys
def Hover_1():
    pyautogui.moveTo(445,300)
    pyautogui.moveTo(445,590,duration=0.6)

def Hover_2():
    pyautogui.moveTo(515,300)
    pyautogui.moveTo(515,590,duration=0.6)
    
def Hover_3():
    pyautogui.moveTo(585,300)
    pyautogui.moveTo(585,590,duration=0.6)

def Hover_4():
    pyautogui.moveTo(660,300)
    pyautogui.moveTo(660,590,duration=0.6)

def Hover_5():
    pyautogui.moveTo(735,300)
    pyautogui.moveTo(735,590,duration=0.6)

def Hover_6():
    pyautogui.moveTo(800,300)
    pyautogui.moveTo(800,590,duration=0.6)

def Hover_7():
    pyautogui.moveTo(870,300)
    pyautogui.moveTo(870,590,duration=0.6)

def Hover_8():
    pyautogui.moveTo(940,300)
    pyautogui.moveTo(940,590,duration=0.6)

def Hover_9():
    pyautogui.moveTo(1010,300)
    pyautogui.moveTo(1010,590,duration=0.6)
    
def Hover_10():
    pyautogui.moveTo(1080,300)
    pyautogui.moveTo(1080,590,duration=0.6)
    
def Hover_11():
    pyautogui.moveTo(1150,300)
    pyautogui.moveTo(1150,590,duration=0.6)
    
def Hover_12():
    pyautogui.moveTo(1220,300)
    pyautogui.moveTo(1220,590,duration=0.6)


Function_List = [Hover_1,Hover_2,Hover_3,Hover_4,Hover_5,Hover_6,Hover_7,Hover_8,Hover_9,Hover_10,Hover_11,Hover_12]

class Currency:
    def __init__(self, name, base, InventoryLocation):
        self.name = name
        self.base = base
        self.InventoryLocation = InventoryLocation

CurrencyList = [ Currency("ChaosOrb", 10, [725,370]),
         Currency("DivineOrb",10, [800,435]), Currency("OrbofAnnulment", 20, [225,365]), Currency ("ExaltedOrb", 10, [400,360]), Currency("OrbofAlteration", 20, [150,360]),
Currency("RegalOrb",  10,[580,535]), Currency("Jeweller'sOrb", 20, [150,525]), Currency("OrbofScouring", 30, [580,685]), Currency("OrbofUnmaking", 40,[660,600]),
Currency("AncientOrb", 20, [140,600]), Currency("VeiledChaosOrb",10,[810,370]), Currency("VaalOrb", 10,[810,690]), Currency("ChromaticOrb", 20, [300,535]),
Currency("SacredOrb",10,[650,685]), Currency("AwakenedSextant", 10,[575,535]), Currency("OrbofAlchemy", 10, [650,365]), Currency("OrbofFusing", 20, [225,530]), 
Currency("OrbofRegret", 40, [585,605])]

OfferCurrencyQuant = int(sys.argv[1])
OfferCurrencyType = None
for i in CurrencyList:
    if i.name == sys.argv[2]:
        OfferCurrencyType=i
        break
    
# OfferCurrencyQuant = 55
# OfferCurrencyType = CurrencyList[0]
    
kolko = float(OfferCurrencyQuant/OfferCurrencyType.base)

print(kolko)
Columns = int(kolko/5)
print(Columns)
Leftover = kolko%5
print(Leftover)
CalcIndex = 0

for i in range(0,Columns):
    Function_List[i]()
    CalcIndex +=1
    
if Leftover>0 and Leftover<6:
    Function_List[CalcIndex]()

print("awd")
sys.stdout.flush()