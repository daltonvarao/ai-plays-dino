class Game:
    def __init__(self):
        self.distance = 0
        self.length = 0
        self.obstacles = 0
        self.stopped = True
    
    def set_state(self, distance, length, stopped):
        self.distance = distance
        self.length = length
        self.stopped = stopped

    def log(self):
        print({
            'stopped': self.stopped,
            'distance': self.distance,
            'length': self.length,
            'obstacles': self.obstacles
        })
