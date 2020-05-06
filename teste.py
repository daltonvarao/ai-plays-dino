import time
import pyautogui
import cv2

from lib.screen_reader import ScreenReader, ImageScanner
from lib.game import Game
from lib.ga import GeneticAlgorithm


WIDTH, HEIGHT = pyautogui.size()

screen = ScreenReader()
scanner = ImageScanner()

genetic_algorithm = GeneticAlgorithm()
game = Game(genetic_algorithm)


while True:
    grab = screen.grab((20, 100, int(WIDTH*0.49), int(HEIGHT*0.78)))    
    img = screen.process_img(grab)
    
    scanner.add_image(img)
    scanner.adjust_game_position()
    
    dino = scanner.obstacle_distance()

    adjusted_img = grab[scanner.top:scanner.bottom, scanner.left:]

    cv2.rectangle(adjusted_img, (distance_x, distance_y1), (distance_x + length, distance_y2), (255, 0, 0), 2)
    cv2.imshow('grab', cv2.cvtColor(adjusted_img, cv2.COLOR_BGR2RGB))
    cv2.moveWindow('grab', int(WIDTH/2) + 50, 90)
    cv2.waitKey(1)



# while True:


#     if not scanner.game_over():
#         game.run()
#         distance_x = scanner.obstacle_distance()

#         if distance_x:

#             length = scanner.obstacle_length(distance_x)
#             distance_y1, distance_y2 = scanner.obstacle_height(distance_x, length)
            

#             game.set_state(distance_x, distance_y1, length, speed)
#             game.activate_brain()



