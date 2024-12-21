from tkinter import Tk
from game_controller import Game_Controller
from user_interface import UI

DEFAULT_PADDING = 20

window = Tk()
window.config(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

controller = Game_Controller()

ui = UI(controller, window)
ui.grid(row=1, column=0, columnspan=3)

window.mainloop()   