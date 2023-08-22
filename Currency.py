import Pricing
import numpy as np
class Currency:
    def __init__(self, name, base, StashLocation, side):
        self.name = name
        self.base = base
        self.StashLocation = StashLocation
        self.price  = 1
        self.side = side
    def __str__(self):
        return f"Name: {self.name}, Base: {self.base}, StashLocation: {self.StashLocation}, Price: {self.price}, Side: {self.side}"


CurrencyList = [

            Currency("ChaosOrb", 20, [735, 368], "left"),
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
            Currency("OrbofAlchemy", 20, [659, 368], "right"),
            Currency("OrbofFusing", 20, [228, 537], "left"),
            Currency("OrbofRegret", 40, [582, 612], "mid")]

a = Pricing.POE("Crucible", "Currency")
a = a.MyList()
for i in range (len(CurrencyList)):
    for j in a:
        if CurrencyList[i].name == j.replace(" ", ""):
            CurrencyList[i].price = a[j]
