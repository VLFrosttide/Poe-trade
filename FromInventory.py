import pyautogui
import sys
print(sys.argv[1])
sys.stdout.flush()
kolko = int(sys.argv[1])
Remainder = sys.argv[2]
# kolko = 10
# Remainder = False
CalcIndex = 0
Columns = int(kolko/5)
Leftover = kolko%5

# print(kolko, CalcIndex, Columns, Remainder)




pyautogui.FAILSAFE = False 
pyautogui.PAUSE = 0.06


def From_Inv_1():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1720,y=810,duration=0.2)
    pyautogui.click(x=1720,y=880,duration=0.2)
    pyautogui.click(x=1720,y=940,duration=0.2)
    pyautogui.click(x=1720,y=1010,duration=0.2)
    pyautogui.click(x=1720,y=1080,duration=0.2)
##
    pyautogui.click(x=1721,y=810)
    pyautogui.click(x=1721,y=880)
    pyautogui.click(x=1721,y=940)
    pyautogui.click(x=1721,y=1010)
    pyautogui.click(x=1721,y=1080)
    pyautogui.keyUp("ctrl")

#  
def From_Inv_2():  
    pyautogui.keyDown("ctrl")

    pyautogui.click(x=1800,y=810,duration=0.2)
    pyautogui.click(x=1800,y=880,duration=0.2)
    pyautogui.click(x=1800,y=940,duration=0.2)
    pyautogui.click(x=1800,y=1010,duration=0.2)
    pyautogui.click(x=1800,y=1080,duration=0.2)
##
    pyautogui.click(x=1801,y=810)
    pyautogui.click(x=1801,y=880)
    pyautogui.click(x=1801,y=940)
    pyautogui.click(x=1801,y=1010)
    pyautogui.click(x=1801,y=1080)
    pyautogui.keyUp("ctrl")

#
def From_Inv_3():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1870,y=810,duration=0.2)
    pyautogui.click(x=1870,y=880,duration=0.2)
    pyautogui.click(x=1870,y=940,duration=0.2)
    pyautogui.click(x=1870,y=1010,duration=0.2)
    pyautogui.click(x=1870,y=1080,duration=0.2)
##
    pyautogui.click(x=1871,y=810)
    pyautogui.click(x=1871,y=880)
    pyautogui.click(x=1871,y=940)
    pyautogui.click(x=1871,y=1010)
    pyautogui.click(x=1871,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_4():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=1940,y=810,duration=0.2)
    pyautogui.click(x=1940,y=880,duration=0.2)
    pyautogui.click(x=1940,y=940,duration=0.2)
    pyautogui.click(x=1940,y=1010,duration=0.2)
    pyautogui.click(x=1940,y=1080,duration=0.2)
##
    pyautogui.click(x=1941,y=810)
    pyautogui.click(x=1941,y=880)
    pyautogui.click(x=1941,y=940)
    pyautogui.click(x=1941,y=1010)
    pyautogui.click(x=1941,y=1080)
    pyautogui.keyUp("ctrl")
#  
def From_Inv_5():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2010,y=810,duration=0.2)
    pyautogui.click(x=2010,y=880,duration=0.2)
    pyautogui.click(x=2010,y=940,duration=0.2)
    pyautogui.click(x=2010,y=1010,duration=0.2)
    pyautogui.click(x=2010,y=1080,duration=0.2)
##
    
    pyautogui.click(x=2011,y=810)
    pyautogui.click(x=2011,y=880)
    pyautogui.click(x=2011,y=940)
    pyautogui.click(x=2011,y=1010)
    pyautogui.click(x=2011,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_6():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2080,y=810,duration=0.2)
    pyautogui.click(x=2080,y=880,duration=0.2)
    pyautogui.click(x=2080,y=940,duration=0.2)
    pyautogui.click(x=2080,y=1010,duration=0.2)
    pyautogui.click(x=2080,y=1080,duration=0.2)
#
    pyautogui.click(x=2081,y=810)
    pyautogui.click(x=2081,y=880)
    pyautogui.click(x=2081,y=940)
    pyautogui.click(x=2081,y=1010)
    pyautogui.click(x=2081,y=1080)
    pyautogui.keyUp("ctrl")
##
def From_Inv_7():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2150,y=810,duration=0.2)
    pyautogui.click(x=2150,y=880,duration=0.2)
    pyautogui.click(x=2150,y=940,duration=0.2)
    pyautogui.click(x=2150,y=1010,duration=0.2)
    pyautogui.click(x=2150,y=1080,duration=0.2)
##
    pyautogui.click(x=2151,y=810)
    pyautogui.click(x=2151,y=880)
    pyautogui.click(x=2151,y=940)
    pyautogui.click(x=2151,y=1010)
    pyautogui.click(x=2151,y=1080)
    pyautogui.keyUp("ctrl")

#
def From_Inv_8():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2220,y=810,duration=0.2)
    pyautogui.click(x=2220,y=880,duration=0.2)
    pyautogui.click(x=2220,y=940,duration=0.2)
    pyautogui.click(x=2220,y=1010,duration=0.2)
    pyautogui.click(x=2220,y=1080,duration=0.2)
##
    pyautogui.click(x=2221,y=810)
    pyautogui.click(x=2221,y=880)
    pyautogui.click(x=2221,y=940)
    pyautogui.click(x=2221,y=1010)
    pyautogui.click(x=2221,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_9():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2290,y=810,duration=0.2)
    pyautogui.click(x=2290,y=880,duration=0.2)
    pyautogui.click(x=2290,y=940,duration=0.2)
    pyautogui.click(x=2290,y=1010,duration=0.2)
    pyautogui.click(x=2290,y=1080,duration=0.2)
##
    pyautogui.click(x=2291,y=810)
    pyautogui.click(x=2291,y=880)
    pyautogui.click(x=2291,y=940)
    pyautogui.click(x=2291,y=1010)
    pyautogui.click(x=2291,y=1080)
    pyautogui.keyUp("ctrl")

#
def From_Inv_10():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2360,y=810,duration=0.2)
    pyautogui.click(x=2360,y=880,duration=0.2)
    pyautogui.click(x=2360,y=940,duration=0.2)
    pyautogui.click(x=2360,y=1010,duration=0.2)
    pyautogui.click(x=2360,y=1080,duration=0.2)
##
    pyautogui.click(x=2361,y=810)
    pyautogui.click(x=2361,y=880)
    pyautogui.click(x=2361,y=940)
    pyautogui.click(x=2361,y=1010)
    pyautogui.click(x=2361,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_11():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2430,y=810,duration=0.2)
    pyautogui.click(x=2430,y=880,duration=0.2)
    pyautogui.click(x=2430,y=940,duration=0.2)
    pyautogui.click(x=2430,y=1010,duration=0.2)
    pyautogui.click(x=2430,y=1080,duration=0.2)
##
    pyautogui.click(x=2431,y=810)
    pyautogui.click(x=2431,y=880)
    pyautogui.click(x=2431,y=940)
    pyautogui.click(x=2431,y=1010)
    pyautogui.click(x=2431,y=1080)
    pyautogui.keyUp("ctrl")
#
def From_Inv_12():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2500,y=810,duration=0.2)
    pyautogui.click(x=2500,y=880,duration=0.2)
    pyautogui.click(x=2500,y=940,duration=0.2)
    pyautogui.click(x=2500,y=1010,duration=0.2)
    pyautogui.click(x=2500,y=1080,duration=0.2)
##
    pyautogui.click(x=2501,y=810)
    pyautogui.click(x=2501,y=880)
    pyautogui.click(x=2501,y=940)
    pyautogui.click(x=2501,y=1010)
    pyautogui.click(x=2501,y=1080)
    pyautogui.keyUp("ctrl")

Function_List = [From_Inv_1, From_Inv_2, From_Inv_3,From_Inv_4,From_Inv_5,From_Inv_6,From_Inv_7,From_Inv_8,From_Inv_9,From_Inv_10,From_Inv_11,From_Inv_12]

for i in range(0,Columns):
    Function_List[i]()
    CalcIndex +=1
    
if Leftover>0 and Leftover<6:
    Function_List[CalcIndex]()
        


    #for i in range(5):
     #   for j in range(12):
    #        v = [start_y+add*i, start_y+add*(i+1)]
   #         h = [start_x+add*j, start_x+add*(j+1)]
  #          pyautogui.click((h[0]+h[1])//2, (v[0]+v[1])//2-10, duration=0.25)

    

def ClickMe():
    pyautogui.keyDown("ctrl")
    pyautogui.click(x=2500,y=1080,duration=0.2)
    pyautogui.click(x=2501,y=1080)
    pyautogui.keyUp("ctrl")
 
if "True" in Remainder: 
     ClickMe()



#from_invetory()
#If remains >0 
 #   click Function_List[i+1]