

class Essence:
    def __init__(self, name, base, StashLocation, price, side):
        self.name = name
        self.base = base
        self.StashLocation = StashLocation
        self.price = price
        self.side = side
    def __str__(self):
        return f"{self.name}, {self.base},  {self.StashLocation}, {self.price},{self.side}"



EssenceList = [ Essence("DeafeningEssenceofGreed", 9, [80,244],1,0),
         Essence("DeafeningEssenceofContempt",9, [80,300],1,0), Essence("DeafeningEssenceofHatred", 9, [80,365],1,0), Essence ("DeafeningEssenceofWoe", 9, [80,434],1,0), Essence("DeafeningEssenceofFear", 20, [80,508],1,0),
Essence("DeafeningEssenceofAnger",  9,[80,570],1,0), Essence("DeafeningEssenceofTorment", 9, [80,635],1,0), Essence("DeafeningEssenceofSorrow", 9, [80,690],1,0), Essence("DeafeningEssenceofRage", 9,[80,760],1,0),
Essence("DeafeningEssenceofSuffering", 9, [80,830],1,0), Essence("DeafeningEssenceofWrath",9,[80,900],1,0), Essence("DeafeningEssenceofDoubt", 9,[80,960],1,0), Essence("DeafeningEssenceofLoathing", 9, [790,240],1,1),
Essence("DeafeningEssenceofZeal",9,[795,300],1,1), Essence("DeafeningEssenceofAnguish", 9,[790,365],1,1), Essence("DeafeningEssenceofSpite", 9, [790,435],1,1), Essence("DeafeningEssenceofScorn", 9, [790,500],1,1), 
Essence("DeafeningEssenceofEnvy", 9, [790,570],1,1),Essence("DeafeningEssenceofMisery", 9, [790,633],1,1),Essence("DeafeningEssenceofDread", 9, [790,690],1,1),Essence("EssenceofInsanity", 9, [790,765],1,1),
Essence("EssenceofHorror", 9, [790,830],1,1),Essence("EssenceofDelirium", 9, [790,890],1,1),Essence("EssenceofHysteria", 9, [790,960],1,1),]

# a = Pricing.POE("Crucible", "Essence")
# a = a.get_all_essence_values()
# for i in range (len(EssenceList)):
#     for j in a:
#         if EssenceList[i].name == j.replace(" ", ""):
#             EssenceList[i].price = a[j]
            # print(a[j])
