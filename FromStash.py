import pyautogui
import sys
import time
from pynput.mouse import Button, Controller

mouse = Controller()


# pyautogui.FAILSAFE = False
pyautogui.PAUSE = 0.1


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

RequestCurrency = int(sys.argv[1])
RequestTypeCurrency = None
for i in CurrencyList:
    if i.name == sys.argv[2]:
        RequestTypeCurrency=i
        break
     

kolko = int(RequestCurrency/RequestTypeCurrency.base)
print(kolko)
sys.stdout.flush()
remain = RequestCurrency%RequestTypeCurrency.base 
def Get_Currency():
    pyautogui.keyDown("ctrl")   
    pyautogui.moveTo(x=RequestTypeCurrency.InventoryLocation[0],y=RequestTypeCurrency.InventoryLocation[1])
    pyautogui.click(x=RequestTypeCurrency.InventoryLocation[0],y=RequestTypeCurrency.InventoryLocation[1])
    pyautogui.keyUp("ctrl")

def Get_Remaining(remain):
    pyautogui.keyDown("shift")   
    pyautogui.click(x=RequestTypeCurrency.InventoryLocation[0],y=RequestTypeCurrency.InventoryLocation[1])
    pyautogui.keyUp("shift")
    for i in str(remain):
        pyautogui.press(i, interval=0.1)

    pyautogui.press("enter")
    pyautogui.moveTo(x=2505, y=1100)

    pyautogui.click(x=2505, y=1100)

if RequestCurrency<=RequestTypeCurrency.base:
    print("remain")
    sys.stdout.flush()
    pyautogui.keyDown("shift")   
    pyautogui.moveTo(x=RequestTypeCurrency.InventoryLocation[0],y=RequestTypeCurrency.InventoryLocation[1]
                     
                     )
    pyautogui.click(x=RequestTypeCurrency.InventoryLocation[0],y=RequestTypeCurrency.InventoryLocation[1])
    pyautogui.keyUp("shift")
    
    time.sleep(0.2)
    for i in str (RequestCurrency):
        pyautogui.press(i, interval=0.1)
    time.sleep(0.2)
    # pyautogui.press("enter")
    pyautogui.press("enter")
    pyautogui.moveTo(x=2505, y=1100)
    pyautogui.click(x=2505, y=1100)



if RequestCurrency>RequestTypeCurrency.base:
    for i in range(0,kolko):
        Get_Currency()
      
        
if remain != 0 and RequestCurrency>RequestTypeCurrency.base:
    #time.sleep(1)
    Get_Remaining(remain)
    print("remain")
    sys.stdout.flush()


    


