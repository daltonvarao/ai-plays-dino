import mss
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import time


def screenshot(region):    
    with mss.mss() as sct:
        return np.array(sct.grab(region))

def clean_img(img):
    img[img < 128] = 0
    img[img >= 128] = 1
    return img

def processed_img(region):
    img = screenshot(region)
    img = img[:, :, 0]
    img = clean_img(img)
    return img

# top, left = 200, 100
# width, height = 600, 600

# s_region = { 'top': 100, 'left': 10, 'width': width, 'height': height }

width, height = pyautogui.size() 
s_region = {"top": 100, "left": 10, "width": width//2 - 40, "height": height-100}

img = processed_img(s_region)
plt.imshow(img, cmap="gray")
plt.show()


def game_status(img):
    minv = img.T.argmin()
    axis_0 = minv % height
    soma = np.count_nonzero(img[axis_0, :])

    if soma > 500:
        return 'initial'
    return 'started'

def find_initial_pos(img):
    minv = img.T.argmin()
    axis_0 = minv // height
    axis_1 = minv % height

    return axis_0, axis_1


def find_region(img):
    axes = find_initial_pos(img)
    print(axes)

find_region(img)
