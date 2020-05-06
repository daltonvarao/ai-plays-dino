import numpy as np
import pyautogui

class Game:
    def __init__(self, genetic_algorithm):
        self.genetic_algorithm = genetic_algorithm
        self.distance_x = 0
        self.distance_y = 0
        self.length = 0
        self.obstacles = 0
        self.stopped = True
        self.speed = 0
        self.brain_output = 0.5
    
    def set_state(self, distance_x, distance_y, length, speed):
        self.distance_x = distance_x
        self.distance_y = distance_y
        self.length = length
        self.speed = speed

    def run(self):
        self.stopped = False

    def emit(self):
        return {
            'stopped': self.stopped,
            'distance_x': self.distance_x,
            'distance_y': self.distance_y,
            'length': self.length,
            'obstacles': self.obstacles,
            'speed': self.speed
        }

    @property
    def values(self):
        return np.array([self.distance_x, self.distance_y, self.length, self.speed])

    @property
    def normalized_values(self):
        # print(self.values)
        return self.values / np.linalg.norm(self.values)

    def status(self):
        if self.stopped:
            return 'Stopped'
        return 'Running'

    def log(self):
        print(self.emit())
        print("Status: {}".format(self.status()))

    def focus_on_game(self):
        pyautogui.mouseDown(x=200, y=300)
        pyautogui.press('up')
        pyautogui.press('up')

    def release_all_keys(self):
        pyautogui.keyUp('down')

    def press_up(self):
        pyautogui.keyUp('down')
        pyautogui.press('up')

    def press_down(self):
        pyautogui.keyDown('down')

    def activate_brain(self):
        self.brain_output = self.genetic_algorithm.generation.current_individual.activate(self.normalized_values)[0]
