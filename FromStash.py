import pyautogui


pyautogui.FAILSAFE = False 
pyautogui.PAUSE = 0.06


#region Currency
class Currency:
    def __init__(self, base, InventoryLocation):
    
        self.base = base
        self.InventoryLocation = InventoryLocation

ChaosOrb = Currency(10, [725,370])
Divine = Currency(10, [800,435])
Alts = Currency(20, [150,360])
Exalts = Currency(10, [400,360])
Regals  = Currency(10, [580, 365])
Sextants = Currency(10,[575, 535])
Regrets = Currency(40, [585,605])
Unmaking = Currency(40, [660,600])
Fusings = Currency(20, [225,530])
Annuls = Currency(20, [225,365])
Jewellers = Currency(20, [150,525])
RequestCurrency = 10
Chromatics = Currency(20,[300,535])
Scours = Currency(30, [580,585])
VaalOrbs = Currency(10, [810,690])
#endregion
#region Essences
#endregion

RequestTypeCurrency = VaalOrbs
kolko = int(RequestCurrency/RequestTypeCurrency.base)

def Get_Currency():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=RequestTypeCurrency.InventoryLocation[0],y=RequestTypeCurrency.InventoryLocation[1])
    pyautogui.keyUp("ctrl")


for i in range (0, kolko):
   Get_Currency()
    
#print('Press Ctrl-C to quit.')
#try:
#    while True:
#        x, y = pyautogui.position()
#        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
#        print(positionStr, end='')
#        print('\b' * len(positionStr), end='', flush=True)
#except KeyboardInterrupt:
#    print('\n')
    


