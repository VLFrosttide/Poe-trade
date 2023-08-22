import pyautogui
import sys
# print(sys.argv[1])
# sys.stdout.flush()
# kolko = int(sys.argv[1])
# Remainder = sys.argv[2]
import time
from Currency import CurrencyList



# OfferCurrencyQuant = int(sys.argv[1])
# OfferCurrencyType = None
# for i in CurrencyList:
#     if i.name == sys.argv[2]:
#         OfferCurrencyType=i
#         break
OfferCurrencyQuant = 200
OfferCurrencyType = CurrencyList[4]

kolko = float(OfferCurrencyQuant/OfferCurrencyType.base)
Columns = int(kolko/5)
Leftover = kolko%5
if Columns <= 0:
    Columns = 1
if Leftover > 0:
    Columns = Columns+1
print( f"Kolko {kolko}, Kolonki {Columns}, Ostatuk {Leftover}")




pyautogui.FAILSAFE = True 
pyautogui.PAUSE = 0.06
# XCoords = 1720
# YCoords = 810

def From_Inv_1(X, Y):
    for i in range(5):
        pyautogui.moveTo(X, Y)
        pyautogui.click(X, Y)
        Y = Y + 70
        

def Clicker(X, Y):
    for i in range(12):
        pyautogui.keyDown("ctrl")
        From_Inv_1(X, Y)
        X = X + 70
        Y = 810
        pyautogui.keyUp("ctrl")
        

Clicker(1720, 810)


    

