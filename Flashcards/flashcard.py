from tkinter import *
from tkinter import messagebox
from json import *
from random import randint

# Constants
DEFAULT_WIDTH = 700
DEFAULT_HEIGHT = DEFAULT_WIDTH / 2
EGGSHELL = "#fff5f3"
FONT_NAME = "Courier"
LANGUAGES = ["Russian", "English"]

class Flashcard(Canvas):
    def __init__(self):
        super().__init__()
        self.config(height=DEFAULT_HEIGHT, 
                    width=DEFAULT_WIDTH, 
                    bd=0, 
                    highlightthickness=0, 
                    bg=EGGSHELL)

        self.guessed_words = []
        self.english_word, self.russian_word = self.generate_word()
        # if 1, English / if 0, Russian
        self.side = 0

        if self.english_word and self.russian_word:
            self.place_text(LANGUAGES[self.side])

        # TODO - else:
        #      return error or maybe it's a win?

    def place_text(self, language):
        if language == "Russian":
            self.main_word = self.create_text(DEFAULT_WIDTH/2, DEFAULT_HEIGHT/1.75, text=self.russian_word, font=(FONT_NAME, 48), fill="#000000")

        else:
            self.main_word = self.create_text(DEFAULT_WIDTH/2, DEFAULT_HEIGHT/1.75, text=self.english_word, font=(FONT_NAME, 48), fill="#000000")

        self.language_word = self.create_text(DEFAULT_WIDTH/2, DEFAULT_HEIGHT/3.5, text=language, font=(FONT_NAME, 16, "italic"), fill="#000000")

    def replace_text(self, language):
        if language == "Russian":
            self.itemconfigure(self.main_word, text=self.russian_word)

        else:
            self.itemconfigure(self.main_word, text=self.english_word)

        self.itemconfigure(self.language_word, text=language)

    def generate_word(self) -> str:
        try:
            with open("Flashcards/russian_dictionary.json", "r") as data:
                dic = load(data)
                word = randint(0, 92)

                while dic[word]["russian"] in self.guessed_words:
                    word = randint(0, 92)
                
                return dic[word]["english"], dic[word]["russian"]
                
        except FileNotFoundError:
            messagebox.showerror(title="File Not Found!", message="russian_dictionary.json cannot be found!")
    
    def new_word(self) -> None:
        self.english_word, self.russian_word = self.generate_word()
        self.side = 0
        self.replace_text(LANGUAGES[self.side])

    def correctly_guessed_word(self) -> None:
        self.guessed_words.append(self.russian_word)
        print(self.guessed_words)

    def flip_card(self) -> None:
        self.side = 1 - self.side
        self.replace_text(LANGUAGES[self.side])