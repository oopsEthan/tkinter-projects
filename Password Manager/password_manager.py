from tkinter import *
from tkinter import messagebox
from random import choice
from string import *
import json

# Constants
LABEL_COLUMN = 0
ENTRY_COLUMN = 1
WEBSITE_ROW = 1
EMAIL_ROW = 2
PASSWORD_ROW = 3
DEFAULT_PASSWORD_LENGTH = 20

class InputForm():
    def __init__(self, win) -> None:
        self.designated_window = win
        self.generate_labels()
        self.generate_input_fields()
        self.generate_buttons()
    
    # Generates the UI's labels and grids them
    def generate_labels(self) -> None:
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=WEBSITE_ROW, column=LABEL_COLUMN, sticky="W")
        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(row=EMAIL_ROW, column=LABEL_COLUMN, sticky="W")
        self.password_label = Label(text="Password:")
        self.password_label.grid(row=PASSWORD_ROW, column=LABEL_COLUMN, sticky="W")

    # Generates the UI's fields and grids them
    #   reset_entry is ran to ensure fields are blank on load and no rogue variables
    def generate_input_fields(self) -> None:
        self.website_input = Entry()
        self.website_input.grid(row=WEBSITE_ROW, column=ENTRY_COLUMN, columnspan=2, sticky="EW")
        self.email_input = Entry()
        self.email_input.grid(row=EMAIL_ROW, column=ENTRY_COLUMN, columnspan=2, sticky="EW")
        self.password_input = Entry()
        self.password_input.grid(row=PASSWORD_ROW, column=ENTRY_COLUMN, sticky="EW")
        self.reset_entry()

    # Generates the UI's buttons and grids them
    def generate_buttons(self) -> None:
        self.generate_password_button = Button(text="Generate Password", command=self.generate_password)
        self.generate_password_button.grid(row=PASSWORD_ROW, column=2, sticky="EW")
        self.save_input_form_button = Button(text="Add", command=self.save_entry)
        self.save_input_form_button.grid(row=4, column=ENTRY_COLUMN, columnspan=2, sticky="EW")
        self.search_button = Button(text="Search", command=self.search_data)
        self.search_button.grid(row=WEBSITE_ROW, column=2, sticky="EW")

    # Grabs entry data and validates the fields to ensure none are blank
    #   Additionally, validate_entry creates the data_package used in save_entry
    def validate_entry(self) -> bool:
        self.get_entry_data()

        if not self.website or not self.email or not self.password:
            messagebox.showerror(title="Invalid Entry", message="One or more of your entry fields is blank or invalid.")
            return False

        self.data_package = {
            self.website: {
                "email": self.email,
                "password": self.password
            }
        }

        return messagebox.askquestion(title="Please Confirm", message=f"Are you sure you want to save this information?\n\nEmail/Username: {self.email}\nPassword: {self.password}")

    # Saves the entry to file and handles file not existing
    def save_entry(self) -> None:
        if self.validate_entry():
            try:
                with open("logins.json", "r") as login_data:
                    data = json.load(login_data)
                    data.update(self.data_package)
                
                with open("logins.json", "w") as login_data:
                    json.dump(data, login_data, indent=4)
                    
            except FileNotFoundError:
                with open("logins.json", "w") as login_data:
                    json.dump(self.data_package, login_data, indent=4)
                
            self.reset_entry()
    
    # Resets entry fields and runs a get_entry_data to ensure those variables are blank as well
    def reset_entry(self) -> None:
        self.website_input.delete(0, len(self.website_input.get()))
        self.email_input.delete(0, len(self.email_input.get()))
        self.password_input.delete(0, len(self.password_input.get()))
        self.data_package = {}

        self.get_entry_data()
    
    # Gets the input fields entries and sets them to a variable
    def get_entry_data(self) -> None:
        self.website = self.website_input.get()
        self.email = self.email_input.get()
        self.password = self.password_input.get()
    
    # Searches the logins.json file for the website_input entry and provides the email/password keys if found
    def search_data(self) -> None:
        try:
            with open("logins.json", "r") as login_data:
                data = json.load(login_data)

        except FileNotFoundError:
            messagebox.showerror(title="No Data Saved", message="There is not a data file to search through, have you added an account yet?")
        
        else:
            account = self.website_input.get()

            if account in data:
                messagebox.showinfo(title="Account Located", message=f"{account}\n\nEmail/Username: {data[account]["email"]}\nPassword: {data[account]["password"]}")
                self.email_input.insert(0, data[account]["email"])
                self.password_input.insert(0, data[account]["password"])
            
            elif not account:
                messagebox.showerror(title="No Account Found", message="The account field is blank.")
            
            elif account not in data:
                messagebox.showerror(title="No Account Found", message=f"The account for '{account}' does not exist.")

    # Generates a password for the user to utilize and copies it to the clipboard
    def generate_password(self) -> None:
        generated_password = ""
        while len(generated_password) < DEFAULT_PASSWORD_LENGTH:
            generated_password += choice(ascii_letters + punctuation + digits)
        
        self.password_input.delete(0, len(self.password_input.get()))
        self.password_input.insert(0, generated_password)

        self.designated_window.clipboard_clear()
        self.designated_window.clipboard_append(generated_password)

class Logo(Canvas):
    def __init__(self) ->  None:
        super().__init__()
        self.logo_img = PhotoImage(file="Password Manager/logo.png")
        logo_width, logo_height = self.logo_img.width(), self.logo_img.height()
        self.config(width=logo_width, height=logo_height, highlightthickness=0)

        self.create_image(logo_width/2, logo_height/2, image=self.logo_img)
        self.grid(row=0, column=ENTRY_COLUMN)