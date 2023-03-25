import Pricing
import numpy as np
class Currency:
    def __init__(self, name, base, StashLocation, side):
        self.name = name
        self.base = base
        self.StashLocation = StashLocation
        self.price  = 1
        self.side = side

# CurrencyList = [ 
#                 Currency("ChaosOrb", 10, [725,370], "left"),
#                 Currency("DivineOrb",10, [800,435], "left"), 
#                 Currency("OrbofAnnulment", 20, [225,365], "right"), 
#                 Currency ("ExaltedOrb", 10, [400,360], "mid"), 
#                 Currency("OrbofAlteration", 20, [150,360],"left"),
#                 Currency("RegalOrb",  10,[580,360],"right"), 
#                 Currency("OrbofScouring", 30, [580,685],",mid"), 
#                 Currency("OrbofUnmaking", 40,[660,600],"right"),
#                 Currency("AncientOrb", 20, [140,600],"left"), 
#                 Currency("VeiledChaosOrb",10,[810,370],"right"), 
#                 Currency("VaalOrb", 10,[810,690],"right"), 
#                 Currency("ChromaticOrb", 20, [300,535],"left"),
#                 Currency("AwakenedSextant", 10,[575,535],"mid"), 
#                 Currency("OrbofAlchemy", 10, [650,365],"right"), 
#                 Currency("OrbofFusing", 20, [225,530],"left"), 
#                 Currency("OrbofRegret", 40, [585,605],"mid")]

CurrencyList = [

            Currency("ChaosOrb", 10, [735, 368], "left"),
            Currency("DivineOrb", 10, [811, 445], "left"),
            Currency("OrbofAnnulment", 20, [228, 368], "right"),
            Currency("ExaltedOrb", 10, [404, 368], "mid"),
            Currency("OrbofAlteration", 20, [152, 368], "left"),
            Currency("RegalOrb", 10, [582, 368], "right"),
            Currency("OrbofScouring", 30, [582, 688], ",mid"),
            Currency("OrbofUnmaking", 40, [659, 612], "right"),
            Currency("AncientOrb", 20, [152, 688], "left"),
            Currency("VeiledChaosOrb", 10, [811, 368], "right"),
            Currency("VaalOrb", 10, [811, 688], "right"),
            Currency("ChromaticOrb", 20, [304, 537], "left"),
            Currency("AwakenedSextant", 10, [582, 537], "mid"),
            Currency("OrbofAlchemy", 10, [659, 368], "right"),
            Currency("OrbofFusing", 20, [228, 537], "left"),
            Currency("OrbofRegret", 40, [582, 612], "mid")]

a = Pricing.POE("Sanctum", "Currency")
a = a.MyList()
for i in range (len(CurrencyList)):
    for j in a:
        if CurrencyList[i].name == j.replace(" ", ""):
            CurrencyList[i].price = a[j]
