# from pandas import *
from tkinter import *
import operator as op

PAD_X = 20
PAD_Y = 10

    def calculate(self):
        self.second_number = self.read_number()
        print(self.second_number)
        result = self.operators[self.selected_operator](self.first_number, self.second_number)
        self.display.config(text=str(result))

window = Main_Window()
window.mainloop()