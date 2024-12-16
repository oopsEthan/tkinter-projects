from tkinter import Tk
from question_generator import Question_Generator
from quizzler_ui import UI

window = Tk()

questions = Question_Generator()
ui = UI(questions)

window.mainloop()