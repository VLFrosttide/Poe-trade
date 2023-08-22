import pyautogui
import time

t_end = time.time() + 300

left = 650    # X-coordinate of the left edge
top = 50     # Y-coordinate of the top edge
width = 350  # Width of the region
height = 135 # Height of the region

region = (left, top, width, height)

while time.time() < t_end:
    if pyautogui.locateOnScreen("Amd.png", region=region, confidence=0.8):
        print("Found", flush=True)
        break
    else:
        print("Not found", flush=True)
    time.sleep(1)  # Adjust the sleep time as needed to avoid excessive checking
