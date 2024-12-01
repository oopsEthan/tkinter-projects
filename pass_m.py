from tkinter import *
from pass_m_obj import *

window = Tk()
window.title("MyPass Password Manager")
window.config(padx=20, pady=20)

logo = Logo()
input_form = InputForm(window)

window.mainloop()