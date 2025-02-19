from tkinter import *


def miles_to_km():
    miles = float(input.get())
    km = miles * 1.60934
    label3.config(text=f'{km}')


# Creating a new window and configurations
window = Tk()
window.title("Mile to KM Converter")
# window.minsize(width=300, height=200)
window.config(padx=25, pady=25)

# Entry
input = Entry(width=7)
input.insert(END, string='0')
input.grid(column=1, row=0)

# Label
label1 = Label(text='Miles')
label1.grid(column=2, row=0)

label2 = Label(text='is equal to')
label2.grid(column=0, row=1)

label3 = Label(text='0')
label3.grid(column=1, row=1)

label4 = Label(text='Km')
label4.grid(column=2, row=1)

# Button
button1 = Button(text='Calculate', command=miles_to_km)
button1.grid(column=1, row=2)


window.mainloop()
