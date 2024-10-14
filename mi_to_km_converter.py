# from pandas import *
from tkinter import *

PAD_X = 20
PAD_Y = 10

class Main_Window(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Miles to Kilometers Converter")
        self.config(padx=PAD_X, pady=PAD_Y)

        self.setup_layout()

    def setup_layout(self):
        self.mile_input = Entry(width=10)
        self.mile_input.grid(column=2, row=1)

        self.result_text = Label(text="0")
        self.result_text.grid(column=2, row=2)

        km_text = Label(text="Km")
        km_text.grid(column=3, row=2)

        mile_text = Label(text="Mi")
        mile_text.grid(column=3, row=1)

        equal_text = Label(text="is equal to")
        equal_text.grid(column=1, row=2)

        convert_button = Button(text="Convert", command=self.convert_miles)
        convert_button.grid(column=2, row=3)

    def convert_miles(self):
        try:
            miles = float(self.mile_input.get())
            kilometers = miles * 1.60934
            self.result_text.config(text=f"{kilometers:.2f}")
        except ValueError:
            self.result_text.config(text="INVALID!")

window = Main_Window()
window.mainloop()