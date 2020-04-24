class Game:
    def __init__(self):
        self.distance = 0
        self.length = 0
        self.obstacles = 0
        self.stopped = True
        self.speed = 0
    
    def set_state(self, distance, length, stopped, speed):
        self.distance = distance
        self.length = length
        self.stopped = stopped
        self.speed = speed

    def run(self):
        self.stopped = False

    def emit(self):
        return {
            'stopped': self.stopped,
            'distance': self.distance,
            'length': self.length,
            'obstacles': self.obstacles,
            'speed': self.speed
        }

    def status(self):
        if self.stopped:
            return 'Stopped'
        return 'Running'

    def log(self):
        print(self.emit())
        print("Status: {}".format(self.status()))
