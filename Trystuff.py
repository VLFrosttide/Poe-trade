import pyautogui
import time
from Currency import *

args = ([725,370] , 12)
a = 270
def ChaosOrb(args, args2):
    pyautogui.write( f" 1/{args2}")
CurrencyList[0].price = 270
print(CurrencyList[0].price)
ChaosOrb([725,370], CurrencyList[0].price)


