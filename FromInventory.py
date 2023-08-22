import pyautogui
import sys
from Currency import CurrencyList
import math 
import time

Quant = int(sys.argv[1])
Type = sys.argv[2]


def CurrencyBase(Type, CurrencyList):
    
    for currency in CurrencyList:
        if currency.name.lower() == Type.lower():
            return currency.base
    return None


Base = int(CurrencyBase(Type, CurrencyList))

Clicks = Quant / Base
Clicks = math.floor(Clicks)
Clicks = Clicks / 5
Clicks = math.ceil(Clicks)
Remain = Quant%Base




pyautogui.PAUSE = 0.06
XCoords = 1720
YCoords = 810

def From_Inv_1(XCoords, YCoords):
    for i in range(5):
        pyautogui.moveTo(XCoords, YCoords)
        pyautogui.click(XCoords, YCoords)
        YCoords = YCoords + 70


if Remain > 0 and Quant < Base :
    pyautogui.keyDown("ctrl")
    pyautogui.moveTo(2500,1100)
    pyautogui.click(2500,1100)
    pyautogui.keyUp("ctrl")

if  Quant > Base:
    for i in range(Clicks):
        pyautogui.keyDown("ctrl")
        From_Inv_1(XCoords, YCoords)
        XCoords = XCoords + 70
        YCoords = 810
        pyautogui.keyUp("ctrl")
        
        

time.sleep(0.2)
print("FromInventory Executed", flush=True)