import requests
import json
import sys

# CurrencyType = sys.argv[1]

CurrencyList = [
    "Exalted Orb", "Divine Orb", "Orb of Annulment", "Orb of Alteration",
    "Regal Orb", "Orb of Scouring", "Orb of Unmaking",
    "Ancient Orb","Veiled Chaos Orb","Vaal Orb", "Chromatic Orb","Awakened Sextant",
    "Orb of Alchemy", "Orb of Fusing","Orb of Regret" 
]


# print(CurrencyList)

class POE:
    def __init__(self, league, type):
        if type == "Essence":
            url = f"https://poe.ninja/api/data/itemoverview?league={league}&type={type}"
        if type == "Currency":
            url = f"https://poe.ninja/api/data/currencyoverview?league={league}&type={type}"
        
        req_data = requests.get(url)
        self.json_data = req_data.json()

    def get_all_essence_values(self, mapTier_thrushold=6):
        result = {}
        for i in range(len(self.json_data['lines'])):
            if 'mapTier' not in self.json_data['lines'][i]:
                continue
            name = self.json_data['lines'][i]['name']
            mapTier = self.json_data['lines'][i]['mapTier']
            chaosValue = self.json_data['lines'][i]['chaosValue']
            if mapTier < mapTier_thrushold:
                continue
            result[name] = {'mapTier':mapTier, 'chaosValue':chaosValue}
        return result



    def MyList (self):
        result = {}
        for i in range(len(self.json_data['lines'])):
            if 'receive' not in self.json_data['lines'][i]:
                continue
            item_name = self.json_data['lines'][i]['currencyTypeName']
            price = self.json_data['lines'][i]['receive']['value']
            if item_name in CurrencyList:
                
                result[item_name] = price
        
        return result

    def get_all_currency_values(self):
        result = {}
        for i in range(len(self.json_data['lines'])):
            if 'receive' not in self.json_data['lines'][i]:
                continue
            item_name = self.json_data['lines'][i]['currencyTypeName']
            price = self.json_data['lines'][i]['receive']['value']
            result[item_name] = price
        
        return result

    def get_essence_value(self, name):
        result = self.get_all_currency_values()
        if name in result:
            return result[name]

    def get_currency_value(self, name):
        result = self.get_all_currency_values()
        if name in result:
            return result[name]


a = POE("Sanctum", "Currency")
# print(a.get_all_essence_values())
# print(a.get_essence_value("Essence of Insanity"))

# print( a.get_currency_value(f"{CurrencyType}"))
print(a.MyList())
sys.stdout.flush()