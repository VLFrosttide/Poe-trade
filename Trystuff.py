import pyautogui
import time
# from Currency import CurrencyList
from AfterTradeFromInv import Clicker

XCoords = 1720
YCoords = 810

Clicker(XCoords, YCoords)

# StartTime = time.time()

# def From_Inv_1():
#     global YCoords, XCoords
#     for i in range(5):
#         pyautogui.moveTo(XCoords, YCoords)
#         pyautogui.click(XCoords, YCoords)
#         YCoords = YCoords + 70
               
# for i in range(12):
#     From_Inv_1()
#     XCoords = XCoords + 70
#     YCoords = 810
    
    

# def GridClick(StartX, StartY, Rows, Columns):
#     pyautogui.keyDown("ctrl")
#     for i in range(1,Rows*Columns+1):
#         # pyautogui.moveTo(StartX, StartY)
#         pyautogui.click(StartX, StartY)
#         StartY = StartY+70
#         if i % 5 == 0 and i !=0:
#             StartX = StartX + 70
#             StartY = 810
#     pyautogui.keyUp("ctrl")
            
# GridClick(1720, 810, 5, 12)

EndTime = time.time()
# ElapsedTime = EndTime - StartTime
# print(ElapsedTime)