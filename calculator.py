# from pandas import *
from tkinter import *

PAD_X = 20
PAD_Y = 10

class Main_Window(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Calculator")
        self.config(padx=PAD_X, pady=PAD_Y)

        self.num_buttons = self.setup_keypad()

    def setup_keypad(self) -> list:
        buttons = []
        self.input_label = Label(self, text="0")
        self.input_label.grid(row=0, column=0, columnspan=4)
        for n in range(3):
            print(f"n:{n}")
            for m in range(3):
                print(f"m:{m}")
                number = n * 3 + m + 1
                print(f"number:{number}")
                button = Button(text=f"{number}", width=5, height=2)
                button.grid(row=n + 1, column=m + 1)
                buttons.append(button)

        button_zero = Button(self, text="0", width=5, height=2)
        button_zero.grid(row=4, column=1)
        buttons.append(button_zero)
                
        Button(text="Clear", width=5, height=2).grid(row=4, column=0)
        Button(text="Enter", width=5, height=2).grid(row=4, column=2)

        print(buttons)
        return buttons


window = Main_Window()
window.mainloop()