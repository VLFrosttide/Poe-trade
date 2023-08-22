import pyautogui
import sys
from Currency import CurrencyList
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