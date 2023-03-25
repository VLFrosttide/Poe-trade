import Pricing


class Essence:
    def __init__(self, name, base, StashLocation, price):
        self.name = name
        self.base = base
        self.StashLocation = StashLocation
        self.price = price
    def __str__(self):
        return f"{self.name}, {self.base},  {self.StashLocation}, {self.price}"



EssenceList = [ Essence("DeafeningEssenceofGreed", 9, [80,244],1),
         Essence("DeafeningEssenceofContempt",9, [80,300],1), Essence("DeafeningEssenceofHatred", 9, [80,365],1), Essence ("DeafeningEssenceofWoe", 9, [80,434],1), Essence("DeafeningEssenceofFear", 20, [80,508],1),
Essence("DeafeningEssenceofAnger",  9,[80,570],1), Essence("DeafeningEssenceofTorment", 9, [80,635],1), Essence("DeafeningEssenceofSorrow", 9, [80,690],1), Essence("DeafeningEssenceofRage", 9,[80,760],1),
Essence("DeafeningEssenceofSuffering", 9, [80,830],1), Essence("DeafeningEssenceofWrath",9,[80,900],1), Essence("DeafeningEssenceofDoubt", 9,[80,960],1), Essence("DeafeningEssenceofLoathing", 9, [790,240],1),
Essence("DeafeningEssenceofZeal",9,[790,300],1), Essence("DeafeningEssenceofAnguish", 9,[790,365],1), Essence("DeafeningEssenceofSpite", 9, [790,435],1), Essence("DeafeningEssenceofScorn", 9, [790,500],1), 
Essence("DeafeningEssenceofEnvy", 9, [790,570],1),Essence("DeafeningEssenceofMisery", 9, [790,633],1),Essence("DeafeningEssenceofDread", 9, [790,690],1),Essence("EssenceofInsanity", 9, [790,765],1),
Essence("EssenceofHorror", 9, [790,830],1),Essence("EssenceofDelirium", 9, [790,890],1),Essence("EssenceofHysteria", 9, [790,960],1),]

a = Pricing.POE("Sanctum", "Essence")
a = a.get_all_essence_values()
for i in range (len(EssenceList)):
    for j in a:
        if EssenceList[i].name == j.replace(" ", ""):
            EssenceList[i].price = a[j]
            # print(a[j])
