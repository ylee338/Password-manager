from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letter = [choice(letters) for char in range(randint(8, 10))]

    pass_symbol = [choice(symbols) for char in range(randint(2, 4))]

    pass_number = [choice(numbers) for char in range(randint(2, 4))]

    password_list = pass_letter + pass_symbol + pass_number
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    data = {
        web_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get(),
         }
    }

    if len(web_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        try:

            with open("data.json", 'r') as file:
                # read old data
                new_data = json.load(file)

        except FileNotFoundError:

            with open("data.json", 'w') as file:
                json.dump(data, file, indent=4)

        else:
            # update with new data
            new_data.update(data)

            with open("data.json", "w") as file:
                # saving updated data
                json.dump(new_data, file, indent=4)

        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            web_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
# create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# image canvas
canvas = Canvas(height=200, width=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "ylee1359256@gmail.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(width=35)
password_entry.grid(row=3, column=1, columnspan=2)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
