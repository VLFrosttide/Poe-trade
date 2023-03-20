import Pricing  
from Currency import *
import sys
import time
import pyautogui

while True:
    a = Pricing.POE("Sanctum", "Currency")
    a = a.MyList()
    for i in range (len(CurrencyList)):
        for j in a:
            if CurrencyList[i].name == j.replace(" ", "") and CurrencyList[i].price != a[j]:
                print(CurrencyList[i].name, a[j])
                CurrencyList[i].price = a[j]
    time.sleep(900)

