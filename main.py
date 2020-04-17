import numpy as np
import pyautogui

from screen_reader import ScreenReader

screen = ScreenReader()

while True:
    img = screen.proccessed_img()

    if screen.game_over(img):
        print('STATUS: GAME OVER')
        pyautogui.press('space', interval=0)
    else:
        print('STATUS: RUNNING')
        pyautogui.press('up', interval=0)
