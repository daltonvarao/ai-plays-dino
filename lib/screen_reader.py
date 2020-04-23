import mss
import numpy as np
import matplotlib.pyplot as plt
import time


class ScreenReader:

    def __init__(self):
        pass

    def grab(self, monitor):
        with mss.mss() as screen:
            img = np.array(screen.grab(monitor))
            img = self.process_img(img)
            return img

    def binarize(self, img):
        img[img < 128] = 0
        img[img >= 128] = 1
        return img

    def inverse(self, img):
        return np.abs(img - 1)

    def dark_mode(self, img):
        white_pixels = np.count_nonzero(img)
        percent = white_pixels / img.size

        if percent < .05:
            return True

        return False

    def process_img(self, img):
        img = img[:, :, 0]
        img = self.binarize(img)

        if self.dark_mode(img):
            img = self.inverse(img)

        return img

    def show(self, img):
        plt.imshow(img, cmap='gray')
        plt.show()


class ImageScanner:

    def __init__(self):
        pass

    def game_over(self):
        white_pixels = np.count_nonzero(self.img[:60])

        if white_pixels > 33200:
            return False
        return True

    def add_image(self, img):
        self.img = img

    def adjust_game_position(self):
        pos = self.game_position(self.img)
        self.img = self.img[pos['top'] + 20:pos['bottom'] - 10, pos['left']+80:]

    def obstacle_distance(self):
        pos = self.distance(self.img)
        return pos

    def distance(self, img):
        minv1 = self.img.T.argmin()
        left = minv1//self.img.shape[0]
        return left

    def obstacle_length(self):
        indexes = np.argwhere(self.img.sum(axis=0) != self.img.shape[0]).flatten()
        
        for i in range(0, indexes.size - 1):
            if indexes[i + 1] - indexes[i] > 4:
                return int(indexes[i] - indexes[0])

        return int(indexes[-1] - indexes[0])

    def game_position(self, img):
        minv1 = self.img.T.argmin()
        minv2 = self.img.argmin()

        top = minv2//self.img.shape[1]
        right = minv2%self.img.shape[1]

        left = minv1//self.img.shape[0]
        bottom = minv1%self.img.shape[0]

        return {
            'top': top, 
            'left': left,
            'right': right,
            'bottom': bottom
        }
