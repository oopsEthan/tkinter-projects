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
        print(f"debug - Num Buttons: {self.num_buttons}")
        self.operator_buttons = self.setup_operators()
        print(f"debug - Operator Buttons: {self.operator_buttons}")
        self.button_command_creation()

    def setup_keypad(self) -> list:
        buttons = []
        self.input_label = Label(self)
        self.input_label.grid(row=0, column=0, columnspan=5)

        # Separate code for 0
        button = Button(self, text="0", width=5, height=2)
        button.grid(row=4, column=2)
        buttons.append(button)

        # For loop through the rest
        for n in range(3):
            for m in range(3):
                number = n * 3 + m + 1
                button = Button(text=f"{number}", width=5, height=2)
                button.grid(row=n + 1, column=m + 1)
                buttons.append(button)

                
        Button(text="Clear", width=5, height=2).grid(row=4, column=1)
        Button(text="Enter", width=5, height=2).grid(row=4, column=3)

        print(buttons)
        return buttons
    
    def setup_operators(self):
        operators = ["+", "-", "/", "*"]
        operator_buttons = []
        for n in range(4):
            button = Button(text=operators[n], width=5, height=2)
            button.grid(row=n+1, column=4)
            operator_buttons.append(button)

        return operator_buttons
    
    def button_command_creation(self):
        for button in self.num_buttons:
            button.config(command=lambda button=button: self.input_number(button["text"]))

    def input_number(self, number):
        self.input_label.config(text=f"{self.input_label["text"] + number}")
    
    def read_number(self) -> int:
        output = int(self.input_label["text"])
        print(output)
        return output

window = Main_Window()
window.mainloop()