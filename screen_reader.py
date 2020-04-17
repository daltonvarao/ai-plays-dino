import mss
import numpy as np


class ScreenReader:
    def __init__(self):
        self.region = {"top": 210, "left": 96, "width": 582, "height": 170}

    def screenshot(self,):    
        with mss.mss() as sct:
            return np.array(sct.grab(self.region))

    def clean_img(self, img):
        img[img < 128] = 0
        img[img >= 128] = 1
        return img

    def proccessed_img(self):
        img = self.screenshot()
        img = self.clean_img(img[:, :, 0])
        return img

    def game_over(self, img):
        return np.count_nonzero(img[30:46, :]) < 9200

