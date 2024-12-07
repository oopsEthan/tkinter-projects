from tkinter import *
from flashcard import Flashcard

# Constants
DEFAULT_PADDING = 50
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

window = Tk()
window.title("Russian Flashcards")
window.config(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, bg=BACKGROUND_COLOR)

card = Flashcard()
card.grid(row=0, column=0, columnspan=3)

flipper = Button(text="FLIP", 
                 command=card.flip_card, 
                 width=5, height=3, 
                 font=(FONT_NAME, 24), 
                 highlightthickness=0, 
                 bd=0)

success_image = PhotoImage(file="right.png")
success = Button(image=success_image, highlightthickness=0, bd=0)

fail_image = PhotoImage(file="wrong.png")
fail = Button(image=fail_image, highlightthickness=0, bd=0)

# TODO - Implement button commands into flashcard
# TODO - Move button and shtuff to a single format/class in user_interface.py

flipper.grid(row=1, column=1, columnspan=1, pady=20, sticky="EW")
success.grid(row=1, column=2, sticky="E")
fail.grid(row=1, column=0, sticky="W")

window.mainloop()