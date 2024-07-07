from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

BACKGROUND_COLOR = "white"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.extend([random.choice(letters) for char in range(random.randint(4, 6))])
    password_list.extend([random.choice(symbols) for char in range(random.randint(4, 6))])
    password_list.extend([random.choice(numbers) for char in range(random.randint(4, 6))])

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

    pyperclip.copy(password_entry.get())
# ---------------------------- SEARCH PASSWORD ------------------------------#
def search():
    website = website_entry.get()

    if len(website)==0:
        messagebox.showerror(message="Website name cannot be blank.", title="Enter a website")

    else:
        try:
            with open("password.json", "r") as file:
                json_data = json.load(file)
                website_info = json_data[website]

        except FileNotFoundError:
            messagebox.showerror(message="No Data File Found.", title="File Not Found")

        except KeyError:
            messagebox.showerror(message="Website not registered.", title=website)

        else:
            text = f"Email : {website_info["username"]}\nPassword : {website_info["password"]}"
            messagebox.showinfo(title=website, message=text)
            pyperclip.copy(website_info["password"])

        finally:
            website_entry.delete(0, END)            
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # Checking for empty fields
    if len(username)==0 or len(website)==0 or len(password)==0:
        messagebox.showerror(message="Please fill all the required fields.", title="Empty Fields")

    else:
        is_okay = messagebox.askokcancel(title="Add Passwprd", message=f"These are the details entered:\nEmail : {username}\nPassword : {password}\nWebsite : {website}\nClick 'OK' to confirm.")
        if is_okay:
            new_entry = {
                website: {
                    "username": username,
                    "password": password,
                }
            }
            json_data = {}
            try:
                with open("password.json", mode="r") as file:
                    json_data = json.load(file)

            except FileNotFoundError:
                with open("password.json", mode="w") as file:
                    json.dump(new_entry, file, indent=4)

            except json.JSONDecodeError:
                json_data={}
                
            else:
                json_data.update(new_entry)
                with open("password.json", mode="w") as file:
                    json.dump(json_data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                messagebox.showinfo(message="Password has been added successfully.")
            
            
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.title("Password Manager")

# Created the canvas with the image
canvas = Canvas(width=200, height=200,bg=BACKGROUND_COLOR, highlightthickness=0)
image = PhotoImage(file="./logo.png")
canvas.create_image(100, 100, image = image)

# Creating all the labels
website_label = Label(text="Website:",bg=BACKGROUND_COLOR)
username_label = Label(text="Email/Username:",bg=BACKGROUND_COLOR)
password_label = Label(text="Password:",bg=BACKGROUND_COLOR)

# Creating entries
website_entry = Entry(width=22,bg=BACKGROUND_COLOR, highlightthickness=0)
website_entry.focus()
username_entry = Entry(width=40,bg=BACKGROUND_COLOR, highlightthickness=0)
username_entry.insert(END, "ananyapratapsingh7@gmail.com")
password_entry = Entry(width=22,bg=BACKGROUND_COLOR, highlightthickness=0)

#Creating the buttons
search_button = Button(text="Search", width=15, command=search,bg=BACKGROUND_COLOR)
generate_password_button = Button(text="Generate Password", width=15, command=generate_password,bg=BACKGROUND_COLOR)
add_button = Button(text="Add", width=38, command=add,bg=BACKGROUND_COLOR)

# Adding to Grid (Layout)
canvas.grid(row=0, column=1)
website_label.grid(row=1, column=0)
website_entry.grid(row=1, column=1)
username_label.grid(row=2, column=0)
username_entry.grid(row=2, column=1, columnspan=2)
password_label.grid(row=3, column=0)
password_entry.grid(row=3, column=1)
generate_password_button.grid(row=3, column=2)
add_button.grid(row=4, column=1, columnspan=2)
search_button.grid(row=1, column=2)

window.mainloop()