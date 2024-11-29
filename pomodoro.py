from tkinter import *
from pomodoro_obj import *

# Constants
PAD_X = 200
PAD_Y = 100
BLACK = "#000"
PINK = "#E2979C"
RED = "#E7305B"
GREEN = "#9BDEAC"
YELLOW = "#F7F5DD"
FONT_NAME = "Courier"

# Grid Constants
CENTER = 3
BUTTON_ROW = 4

window = Tk()
window.config(padx=PAD_X, pady=PAD_Y, bg=YELLOW)

display_for_timer_state = Label(text="OFF", font=(FONT_NAME, 32, "bold"), background=YELLOW, width=11)
rotation_count = Label(text="", font=(FONT_NAME, 16, "bold"), background=YELLOW, fg=GREEN)

timer = Timer()

def update_UI():
    # Update display to show correct timer_state
    display_for_timer_state.config(text=f"{timer.timer_state}", fg=timer.timer_state_color)

    # Update rotation_count by rotations
    rotations = 0
    rotation_display = ""
    while rotations < timer.timer_rotations:
        rotation_display += "✓"
        rotations += 1

    rotation_count.config(text=f"{rotation_display}")
    
    window.after(1000, update_UI)

def start():
    timer.start_timer()
    update_UI()

def reset():
    timer.reset_timer()
    update_UI()

if timer:
    start_button = Button(text="Start", command=start)
    reset_button = Button(text="Reset", command=reset)

    timer.grid(row=2, column=CENTER)
    start_button.grid(row=BUTTON_ROW, column=2)
    reset_button.grid(row=BUTTON_ROW, column=4)
    display_for_timer_state.grid(row=0, column=CENTER)
    rotation_count.grid(row=5, column=CENTER)

window.mainloop()