import time
import pyautogui
from statistics import mean

from lib.screen_reader import ScreenReader, ImageScanner
from lib.game import Game

WIDTH, HEIGHT = pyautogui.size()

screen = ScreenReader()
scanner = ImageScanner()
game = Game()

time2 = 0
distance1 = 0
speeds = []
speed = 0

while True:
    img = screen.grab((20, 100, int(WIDTH*0.49), int(HEIGHT*0.78)))

    scanner.add_image(img)
    scanner.adjust_game_position()

    if not scanner.game_over():
        game.run()
        distance = scanner.obstacle_distance()

        if distance:
            if distance < 120:
                pyautogui.press('up')

            if distance > game.distance:
                distance1 = distance
                time1 = time.time()

            if distance <= 150 and not time2:
                time2 = time.time() 
                speeds.append(((distance1 - distance)/150)/(time2 - time1))
                time2 = 0

            if len(speeds) > 10:
                speed = mean(speeds)
                speeds.clear()

            if (game.distance > 0 and game.distance < 50) and distance > 100:
                game.obstacles += 1

            length = scanner.obstacle_length(distance)
            game.set_state(distance, length, False, speed)

    else:
        game = Game()
    game.log()
