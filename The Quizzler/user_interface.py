from tkinter import *

# Constants
DEFAULT_WIDTH = 700
DEFAULT_HEIGHT = 350
DEFAULT_PADDING = 20

# Main style preferences
EGGSHELL = "#fff5f3"
FONT_NAME = "Arial"

# Style options for the main question Window
QUESTION_WINDOW_STYLE = {
    "height": DEFAULT_HEIGHT, 
    "width": DEFAULT_WIDTH, 
    "bd": 0, 
    "highlightthickness": 0,
    "bg": EGGSHELL
}

# Style options for the True and False buttons
BUTTON_STYLE = {
    "height": 5,
    "font": (FONT_NAME, 16, "bold"),
    "bd": 0,
    "highlightthickness": 0
}

# Grid placement options for buttons
BUTTON_GRID = {
    "sticky": "EW",
    "padx": DEFAULT_PADDING,
    "pady": DEFAULT_PADDING/2
}

# Style options for the question text
QUESTION_TEXT_STYLE = {
    "font": (FONT_NAME, 24),
    "fill": "#000",
    "width": DEFAULT_WIDTH,
    "justify": "center",
}

class UI(Canvas):
    def __init__(self, game_controller, main_window):
        super().__init__()
        self.controller = game_controller
        self.window = main_window
        self.config(**QUESTION_WINDOW_STYLE)
        self.question_string = ""
        self.generate_ui()

    def generate_ui(self):
        self.question_on_display = self.create_text(DEFAULT_WIDTH/2,
                                                    DEFAULT_HEIGHT/2,
                                                    text=self.controller.question,
                                                    **QUESTION_TEXT_STYLE)
        self.generate_buttons()
    
    def new_question(self):
        self.controller.get_question_from_bank()
        self.itemconfigure(self.question_on_display, text=self.controller.question)

    def generate_buttons(self):
        true_button = Button(text="True",
                             command=lambda: self.controller.submit_answer("True"),
                             **BUTTON_STYLE)
        
        false_button = Button(text="False",
                              command=lambda: self.controller.submit_answer("False"),
                              **BUTTON_STYLE)
        
        generate_button = Button(text="Generate",
                                  command=self.new_question,
                                  **BUTTON_STYLE)
        
        true_button.grid(row=2, column=0, **BUTTON_GRID)
        generate_button.grid(row=2, column=1, **BUTTON_GRID)
        false_button.grid(row=2, column=2, **BUTTON_GRID)