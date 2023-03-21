import pyautogui
import time
import sys
import Pricing
from Essence import *
print("awd")

def ClickingStuff(args):
    pyautogui.click(args[0])
EssenceList[0].price = 1
Clickthis = ()
while True:
    a = Pricing.POE("Sanctum", sys.argv[1])
    a = a.get_all_essence_values()
    
    for i in range (len(EssenceList)):
        for j in a:
            if EssenceList[i].name == j.replace(" ", "") and EssenceList[i].price != a[j]:
                Clickthis = (EssenceList[i].StashLocation, a[j])
                ClickingStuff(Clickthis)
                EssenceList[i].price = a[j]
    time.sleep(900)
            

    
    
