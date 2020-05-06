import tkinter as tk

class GUI:

    def __init__(self, game, handle_start_train, started):
        self.window = tk.Tk()
        self.window.geometry("300x300")
        self.game = game
        self.handle_start_train = handle_start_train
        self.started = started
        self.setup_game_frame()
        self.setup_button_frame()

    def setup_game_frame(self):
        self.game_value_frame = tk.Frame(self.window)
        self.game_value_frame.pack(side=tk.TOP)

        self.distance_label = tk.Label(self.game_value_frame, text="Distance:")
        self.distance_label['width'] = 10
        self.distance_label.pack(side=tk.LEFT)

        self.distance_value = tk.Label(self.game_value_frame, text=self.game.distance)
        self.distance_value['width'] = 4
        self.distance_value.pack(side=tk.LEFT)

        self.length_label = tk.Label(self.game_value_frame, text="Length:")
        self.length_label['width'] = 10
        self.length_label.pack(side=tk.LEFT)

        self.length_value = tk.Label(self.game_value_frame, text=self.game.distance)
        self.length_value['width'] = 4
        self.length_value.pack(side=tk.LEFT)

    def setup_button_frame(self):
        self.start_button_frame = tk.Frame(self.window)
        self.start_button_frame.pack(side=tk.BOTTOM)
        
        self.start_button = tk.Button(self.start_button_frame, text='Stop' if self.started else 'Start')
        self.start_button['command'] = self.handle_start_train
        self.start_button.pack()

    def update(self):
        self.window.update()

    def set_state(self, game):
        self.game = game
