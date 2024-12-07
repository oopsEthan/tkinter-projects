from tkinter import *

# Constants
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Arial"

class UI():
    def __init__(self, card_set):
        self.cards = card_set
        self.flipper = Button(text="FLIP", 
                 command=self.cards.flip_card, 
                 width=5, height=3, 
                 font=(FONT_NAME, 24), 
                 highlightthickness=0, 
                 bd=0)

        self.success_rate = 1
        self.successes = 0
        self.failures = 0
        self.success_rate_label = Label(text="Success Rate: 0.00%", font=(FONT_NAME, 24, "bold"), bg=BACKGROUND_COLOR, fg="#000000")

        self.place_buttons()
    
    def place_buttons(self):
        self.flipper.grid(row=2, column=1, columnspan=1, pady=20, sticky="EW")

        self.success_image = PhotoImage(file="Flashcards/right.png")
        self.success = Button(image=self.success_image, command=self.trigger_success, highlightthickness=0, bd=0)
        self.success.grid(row=2, column=2, sticky="E")
        self.success_rate_label.grid(row=0, column=0, columnspan=3, pady=20)

        self.fail_image = PhotoImage(file="Flashcards/wrong.png")
        self.fail = Button(image=self.fail_image, command=self.trigger_failure, highlightthickness=0, bd=0)
        self.fail.grid(row=2, column=0, sticky="W")

    def trigger_success(self) -> None:
        self.successes += 1
        self.cards.correctly_guessed_word()
        self.determine_success_rate()

    def trigger_failure(self) -> None:
        self.failures += 1
        self.determine_success_rate()

    def determine_success_rate(self) -> None:
        try:
            self.success_rate = self.successes / (self.successes + self.failures)

            if self.success_rate >= 1:
                self.success_rate = 1.0

        except ZeroDivisionError:
            self.success_rate = 1.0
        
        finally:
            print(f"{self.successes} / {self.failures}")
            self.success_rate_label.config(text=f"Success Rate: {self.success_rate*100:.2f}%")
            self.cards.new_word()