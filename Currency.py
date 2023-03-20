import Pricing
class Currency:
    def __init__(self, name, base, StashLocation):
        self.name = name
        self.base = base
        self.StashLocation = StashLocation
        self.price  = 1

CurrencyList = [ Currency("ChaosOrb", 10, [725,370]),
         Currency("DivineOrb",10, [800,435]), Currency("OrbofAnnulment", 20, [225,365]), Currency ("ExaltedOrb", 10, [400,360]), Currency("OrbofAlteration", 20, [150,360]),
Currency("RegalOrb",  10,[580,535]), Currency("Jeweller'sOrb", 20, [150,525]), Currency("OrbofScouring", 30, [580,685]), Currency("OrbofUnmaking", 40,[660,600]),
Currency("AncientOrb", 20, [140,600]), Currency("VeiledChaosOrb",10,[810,370]), Currency("VaalOrb", 10,[810,690]), Currency("ChromaticOrb", 20, [300,535]),
Currency("SacredOrb",10,[650,685]), Currency("AwakenedSextant", 10,[575,535]), Currency("OrbofAlchemy", 10, [650,365]), Currency("OrbofFusing", 20, [225,530]), 
Currency("OrbofRegret", 40, [585,605])]

a = Pricing.POE("Sanctum", "Currency")
a = a.MyList()
for i in range (len(CurrencyList)):
    for j in a:
        if CurrencyList[i].name == j.replace(" ", ""):
            CurrencyList[i].price = a[j]
