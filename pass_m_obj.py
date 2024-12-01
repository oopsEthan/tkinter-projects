from tkinter import *
from tkinter import messagebox
from random import choice
from string import *

# Constants
LABEL_COLUMN = 0
ENTRY_COLUMN = 1
WEBSITE_ROW = 1
EMAIL_ROW = 2
PASSWORD_ROW = 3

class InputForm():
    def __init__(self, win) -> None:
        self.generate_labels()
        self.designated_window = win
        self.generate_input_fields()
        self.generate_buttons()
    
    def generate_labels(self) -> None:
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=WEBSITE_ROW, column=LABEL_COLUMN)
        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(row=EMAIL_ROW, column=LABEL_COLUMN)
        self.password_label = Label(text="Password:")
        self.password_label.grid(row=PASSWORD_ROW, column=LABEL_COLUMN)

    def generate_input_fields(self) -> None:
        self.website_input = Entry(width=35)
        self.website_input.grid(row=WEBSITE_ROW, column=ENTRY_COLUMN, columnspan=2)
        self.email_input = Entry(width=35)
        self.email_input.grid(row=EMAIL_ROW, column=ENTRY_COLUMN, columnspan=2)
        self.password_input = Entry(width=20)
        self.password_input.grid(row=PASSWORD_ROW, column=ENTRY_COLUMN)

        self.get_entries()

    def generate_buttons(self) -> None:
        self.generate_password_button = Button(text="Generate Password", width=11, command=self.generate_password)
        self.generate_password_button.grid(row=PASSWORD_ROW, column=2)
        self.save_input_form_button = Button(text="Add", width=32, command=self.save_entry)
        self.save_input_form_button.grid(row=4, column=ENTRY_COLUMN, columnspan=2)

    def validate_entry(self) -> bool:
        self.get_entries()

        if not self.website or not self.email or not self.password:
            messagebox.showerror(title="ERROR: Invalid Entries", message="One or more of your entry fields is blank.")
            return False

        return messagebox.askquestion(title="Please Confirm", message=f"Are you sure you want to save this information?\n\nEmail/Username: {self.email}\nPassword: {self.password}")

    def save_entry(self) -> None:
        if self.validate_entry():
            save_file = open("logins.txt", "a")
            save_string = f"{self.website} | {self.email} | {self.password}\n"
            save_file.write(save_string)
            save_file.close()
                
            self.reset_entry()
    
    def reset_entry(self) -> None:
        self.website_input.delete(0, len(self.website_input.get()))
        self.email_input.delete(0, len(self.email_input.get()))
        self.password_input.delete(0, len(self.password_input.get()))
        self.get_entries()
    
    def get_entries(self) -> None:
        self.website = self.website_input.get()
        self.email = self.email_input.get()
        self.password = self.password_input.get()

    def generate_password(self) -> None:
        generated_password_length = 20
        generated_password = ""
        while len(generated_password) < generated_password_length:
            generated_password += choice(ascii_letters + punctuation + digits)
        
        self.password_input.delete(0, len(self.password_input.get()))
        self.password_input.insert(0, generated_password)

        self.designated_window.clipboard_clear()
        self.designated_window.clipboard_append(generated_password)
        
        print(self.password_input.get())

class Logo(Canvas):
    def __init__(self) ->  None:
        super().__init__()
        self.logo_img = PhotoImage(file="logo.png")
        logo_width, logo_height = self.logo_img.width(), self.logo_img.height()
        self.config(width=logo_width, height=logo_height, highlightthickness=0)

        self.create_image(logo_width/2, logo_height/2, image=self.logo_img)
        self.grid(row=0, column=ENTRY_COLUMN)