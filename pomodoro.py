from tkinter import *

# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
tomato = PhotoImage(file="tomato.png")
tomato_width, tomato_height = tomato.width(), tomato.height()
canvas = Canvas(window, width=tomato_width, height=tomato_height, bg=YELLOW, highlightthickness=0)

start_button = Button(text="Start")
reset_button = Button(text="Reset")


canvas.create_image(100, 112, image=tomato)
canvas.grid(row = 3, column = 3)
start_button.grid(row = 4, column = 2)
reset_button.grid(row = 4, column = 4)

window.config(bg=YELLOW)
window.minsize(800, 600)

window.mainloop()