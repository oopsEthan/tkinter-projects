from tkinter import *

# Constants
DEFAULT_WIDTH = 700
DEFAULT_HEIGHT = 350
DEFAULT_PADDING = 20

# Main style preferences
EGGSHELL = "#fff5f3"
GREEN = "#80FF80"
RED = "#FF8080"
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
    "width": DEFAULT_WIDTH-20,
    "justify": "center",
}

# The UI class handles pretty much all the player input and requests from controller when needed
class UI(Canvas):
    def __init__(self, game_controller):
        super().__init__()
        self.controller = game_controller
        self.config(**QUESTION_WINDOW_STYLE)
        self.submission_in_progress = False
        self.question_string = ""
        self.generate_ui()

    # Generates and places the initial UI elements
    def generate_ui(self):
        self.question_on_display = self.create_text(DEFAULT_WIDTH/2,
                                                    DEFAULT_HEIGHT/2,
                                                    text="Press 'Generate' to get questions.",
                                                    **QUESTION_TEXT_STYLE)
        self.generate_buttons()
        self.score_display = Label(text=f"SCORE: {self.controller.score}", font=(FONT_NAME, 16))
        self.score_display.grid(row=0, column=0, columnspan=3, pady=DEFAULT_PADDING)
    
    # Updates UI state, mainly called in submit_answer
    def update_ui_state(self, in_progress, bg_color=EGGSHELL):
        self.submission_in_progress = in_progress
        self.config(bg=bg_color)

    # Generates questions initially and places or hides buttons as needed
    def generate_questions(self):
        self.true_button.grid(row=2, column=0, **BUTTON_GRID)
        self.false_button.grid(row=2, column=2, **BUTTON_GRID)
        self.generate_button.grid_forget()
        self.generate_new_question()

    # Generates a new question from the GameController's bank and displays the question
    def generate_new_question(self):
        self.config(bg=EGGSHELL)
        self.true_button.config(state="normal")
        self.false_button.config(state="normal")

        self.controller.get_question_from_bank()
        self.itemconfigure(self.question_on_display, text=self.controller.question)

    # Submits the answer to the GameController to determine score + correct/not, also disables buttons
    #   to prevent user from spamming inputs
    def submit_answer(self, answer):
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")

        if self.controller.accept_answer(answer):
            self.config(bg=GREEN)
        else:
            self.config(bg=RED)

        self.score_display.config(text=f"SCORE: {self.controller.score}")
        self.after(2000, self.generate_new_question)

    # Generates buttons and their commands + places 'Generate' button
    def generate_buttons(self):
        self.true_button = Button(text="True",
                             command=lambda: self.submit_answer("True"),
                             **BUTTON_STYLE)
        
        self.false_button = Button(text="False",
                              command=lambda: self.submit_answer("False"),
                              **BUTTON_STYLE)
        
        self.generate_button = Button(text="Generate",
                                  command=self.generate_questions,
                                  **BUTTON_STYLE)
        
        self.generate_button.grid(row=2, column=1, **BUTTON_GRID)