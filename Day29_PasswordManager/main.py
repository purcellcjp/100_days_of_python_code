from tkinter import *
import math
import csv

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    return None

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    url = website_entry_input.get()
    email = email_username_entry_input.get()
    password = password_entry_input.get()

    with open('data.txt', mode='a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter='|')
        csvwriter.writerow([url, email, password])

    website_entry_input.delete(0, END)
    password_entry_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

website_label = Label(text='Website:')
website_label.grid(column=0, row=1)

email_username_label = Label(text='Email/Username:')
email_username_label.grid(column=0, row=2)

password_label = Label(text='Password:')
password_label.grid(column=0, row=3)

website_entry_input = Entry(width=35)
website_entry_input.grid(column=1, row=1, columnspan=2, sticky='w')
website_entry_input.focus()

email_username_entry_input = Entry(width=35)
email_username_entry_input.grid(column=1, row=2, columnspan=2, sticky='w')
email_username_entry_input.insert(0, 'dummy@gmail.com')

password_entry_input = Entry(width=21)
password_entry_input.grid(column=1, row=3, sticky='w')

generate_password_button = Button(
    text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='w')

add_button = Button(text='Add', width=30, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
