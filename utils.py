import cv2
import pytesseract
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity
import glob
from pathlib import Path







def get_text(img):
    lower = np.array([220, 220, 220])
    upper = np.array([255, 255, 255])
    mask = cv2.inRange(img, lower, upper)
    result = cv2.bitwise_and(img, img, mask = mask)
    custom_config = r'--oem 1 --psm 7'
    res = pytesseract.image_to_string(result, config=custom_config)
    res = res.strip()
    return res

# A simple function which takes image object and display on juyter notebook
def display_img(img):
    plt.imshow(img)
    plt.axis("off")
    plt.show()

stuff = [
    [[48, 249], [124, 249], [200, 249], [300, 249], [376, 249], [479, 249], [554, 249], [631, 249], [707, 249], [783, 249]],
    [[48, 340], [124, 340], [200, 340], [276, 340], [376, 340], [435, 340], [554, 340], [631, 340], [707, 340], [783, 340]],
    [[48, 417], [124, 417], [200, 417], [276, 417], [376, 417], [435, 417], [554, 417], [631, 417], [707, 417], [783, 417]],
    [[48, 509], [124, 509], [200, 509], [276, 509], [554, 509], [631, 509], [707, 509], [783, 509]],
    [[48, 584], [124, 584], [200, 584], [276, 584], [554, 584], [631, 584], [707, 584], [783, 584]],
    [[48, 660], [124, 660], [200, 660], [276, 660], [554, 660], [631, 660], [707, 660], [783, 660]],
    [[186, 791], [262, 791], [338, 791], [415, 791], [491, 791], [569, 791], [646, 791]], 
    [[186, 871], [262, 871], [338, 871], [415, 871], [491, 871], [569, 871], [646, 871]], 
]



def Init_imgs(dir_name):
    assets = [] 
    
    for file in glob.glob(f"assets/{dir_name}/*.png"):
        
        img = cv2.imread(file)
        filename = Path(file).stem 
        assets.append((filename, img))
   
    return assets




def similar(img, assets):
    
    assert img.shape == (35, 57, 3)
   
    

    max_sim = 0
    max_label = "awd"
    for i in range(len(assets)):
        sim_val = round(structural_similarity(img, assets[i][1], full=True, channel_axis=2)[0], 3)
        if sim_val > max_sim:
            max_sim = sim_val
            max_label = assets[i][0]
    if max_label in ["blank"]:
        return None
    return (max_label, max_sim)


def comparable(img):
    img = cv2.resize(img, (57, 57))
    img = img[22:, :]
    return img