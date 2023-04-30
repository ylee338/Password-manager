from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    if len(web_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showwarning(title="Oops", message="Please don't leave any fields empty")
    else:
        yes_no = messagebox.askokcancel(title=web_entry.get(), message=f"These are the details entered: \n "
                                                              f"Email: {email_entry.get()} \n "
                                                              f"Password: {password_entry.get()} \n"
                                                              f"Is it ok to save?")
    if yes_no:
        with open("data.txt", "a") as file:
            file.write(f"{web_entry.get()}|{email_entry.get()}|{password_entry.get()}\n")
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

generate_button = Button(text="Generate Password")
generate_button.grid(row=3, column=2, columnspan=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)



window.mainloop()
