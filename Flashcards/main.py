from tkinter import *
from flashcard import Flashcard
from user_interface import UI

# Constants
DEFAULT_PADDING = 50
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

window = Tk()
window.title("Russian Flashcards")
window.config(padx=DEFAULT_PADDING, pady=DEFAULT_PADDING, bg=BACKGROUND_COLOR)

card = Flashcard()
card.grid(row=1, column=0, columnspan=3)

ui = UI(card)

window.mainloop()