import time
import pyautogui
from pynput import keyboard

from lib.screen_reader import ScreenReader, ImageScanner
from lib.game import Game

screen = ScreenReader()
scanner = ImageScanner()
game = Game()

# novo = 0

while True:
    img = screen.grab((20, 100, 660, 600))

    scanner.add_image(img)
    scanner.adjust_game_position()

    if not scanner.game_over():
        game.run()
        distance = scanner.obstacle_distance()

        if distance:
            # if distance > game.distance and game.distance < 50:
            #     novo += 1
            #     print('novo: ', novo)

            if (game.distance > 0 and game.distance < 50) and distance > 100:
                game.obstacles += 1

            # if distance < 115:
            #     pyautogui.press('up')

            length = scanner.obstacle_length()
            game.set_state(distance, length, False)

    else:
        game.set_state(0, 0, True)
    game.log()