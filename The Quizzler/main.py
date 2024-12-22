from tkinter import Tk
from game_controller import GameController
from user_interface import UI

DEFAULT_PADDING = 20

window = Tk()
window.config(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING)

controller = GameController()

ui = UI(controller)
ui.grid(row=1, column=0, columnspan=3)

window.mainloop()   