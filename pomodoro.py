from tkinter import *
from pomodoro_obj import *

# Constants
PAD_X = 200
PAD_Y = 100

window = Tk()
window.config(padx=PAD_X, pady=PAD_Y, bg=YELLOW)

timer = Timer()

if timer:
    start_button = Button(text="Start", command=timer.start_timer)
    reset_button = Button(text="Reset", command=timer.reset_timer)

timer.grid(row = 2, column = 3)

start_button.grid(row = 4, column = 2)
reset_button.grid(row = 4, column = 4)

window.mainloop()