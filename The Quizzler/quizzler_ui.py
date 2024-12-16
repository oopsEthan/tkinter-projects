from tkinter import *

class UI(Canvas):
    def __init__(self, question_generator):
        super().__init__()
        self.question = question_generator