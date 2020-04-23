import curses

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

    def run(self):
        self.stopped = False

    def emit(self):
        return {
            'stopped': self.stopped,
            'distance': self.distance,
            'length': self.length,
            'obstacles': self.obstacles
        }

    def status(self):
        if self.stopped:
            return 'Stopped'
        return 'Running'

    def log(self):
        stdscr = curses.initscr()
        curses.curs_set(False)
        stdscr.clear()
        stdscr.addstr(3, 5, 'AI plays Dino')
        stdscr.addstr(7, 5, 'Distance: {}'.format(self.distance))
        stdscr.addstr(7, 35, 'Length: {}'.format(self.length))
        stdscr.addstr(7, 60, 'Obstaculos: {}'.format(self.obstacles))
        stdscr.addstr(10, 5, 'Status: {}'.format(self.status()))
        stdscr.refresh()
