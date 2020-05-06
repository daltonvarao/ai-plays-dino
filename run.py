import time
import pyautogui
from statistics import mean
import cv2

from lib.screen_reader import ScreenReader, ImageScanner
from lib.game import Game
from lib.ga import GeneticAlgorithm

start = input("Pressione 's' e aperte enter para iniciar: ")

WIDTH, HEIGHT = pyautogui.size()

screen = ScreenReader()
scanner = ImageScanner()

time2 = 0
distance1 = 0
speeds = []
speed = 2.9
pop_size = 24
net_layers = (4, 5, 5, 1)

genetic_algorithm = GeneticAlgorithm(net_layers=net_layers, pop_size=pop_size, mr=0.15, bests_num=4, cr=0.5)
game = Game(genetic_algorithm)

if start == 's':
    game.focus_on_game()

try:
    while True and start == 's':
        grab = screen.grab((20, 100, int(WIDTH*0.49), int(HEIGHT*0.78)))
        img = screen.process_img(grab)
        scanner.add_image(img)
        scanner.adjust_game_position()

        adjusted_img = grab[scanner.top:scanner.bottom, scanner.left:]

        if not scanner.game_over():
            game.run()
            distance_x = scanner.obstacle_distance()

            if distance_x:

                if distance_x > game.distance_x and game.distance_x > 0:
                    game.obstacles += 1

                if distance_x > game.distance_x:
                    distance1 = distance_x
                    time1 = time.time()

                if distance_x <= 150 and not time2:
                    time2 = time.time() 
                    speeds.append(((distance1 - distance_x)/150)/(time2 - time1))
                    time2 = 0

                if len(speeds) > 10:
                    speed = mean(speeds)
                    speeds.clear()

                length = scanner.obstacle_length(distance_x)
                distance_y1, distance_y2 = scanner.obstacle_height(distance_x, length)

                game.set_state(distance_x, distance_y1, length, speed)
                game.activate_brain()

                if game.brain_output <= .45:
                    game.press_down()
                elif game.brain_output >= .55:
                    game.press_up()
                else:
                    game.release_all_keys()

        else:
            if genetic_algorithm.train_mode:
                if not game.stopped:
                    if genetic_algorithm.generation.current_individual.has_experience():
                        genetic_algorithm.generation.current_individual.save_score(game.obstacles)
                        genetic_algorithm.generation.next_individual()
                    
                    if genetic_algorithm.generation.over:
                        new_population = genetic_algorithm.avaliate()
                        genetic_algorithm.new_generation(new_population)

            game.release_all_keys()
            game = Game(genetic_algorithm)
            game.focus_on_game()
        

except KeyboardInterrupt as error:
    print('\nLast Generation genes saved')
    genetic_algorithm.save_many()
