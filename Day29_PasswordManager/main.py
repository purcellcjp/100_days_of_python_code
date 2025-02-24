from tkinter import *
from tkinter import messagebox
import csv
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_list = [random.choice(letters) for _ in range(nr_letters)]

    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = ''.join(password_list)

    # print(f"Your password is: {password}")

    password_entry_input.delete(0, END)
    password_entry_input.insert(0, password)
    # Save new password to clipboard
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_password():
    url = website_entry_input.get()
    email = email_username_entry_input.get()
    password = password_entry_input.get()

    if len(url) == 0 or len(password) == 0:
        messagebox.showinfo(title='Invalid Entries',
                            message='One or more entries are empty.\n\nPlease enter valid data before saving.')
    else:
        is_ok = messagebox.askokcancel(
            title=url,
            message=f'These are the details entered:\nEmail: {email}\nPassword: {password}\nIs it ok to save?')

        if is_ok:
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

password_entry_input = Entry(width=35)
password_entry_input.grid(column=1, row=3, sticky='w')

generate_password_button = Button(
    text='Generate Password', command=generate_password)
generate_password_button.grid(column=2, row=3, sticky='w')

add_button = Button(text='Add', width=30, command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky='w')

window.mainloop()
