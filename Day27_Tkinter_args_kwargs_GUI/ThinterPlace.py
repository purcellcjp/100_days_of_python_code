from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()
window.title('First GUI Program')
window.minsize(width=500, height=300)
# pad the space between objects
window.config(padx=20, pady=20)


# Label
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack(side='left')
# my_label.place(x=100,y=0)
my_label.grid(column=0, row=0)

# pad spaces around a specific object
my_label.config(padx=50, pady=50)


# Change existing text
# my_label['text']  = 'New Text'
# or
my_label.config(text='New Text1')

# Button
button1 = Button(text='Button1', command=button_clicked)
button1.grid(column=1, row=1)

button2 = Button(text='Button2', command=button_clicked)
button2.grid(column=2, row=0)


# # Entry
input = Entry(width=30)
input.insert(END, string='Some text to begin with.')
print(input.get())
input.grid(column=3, row=2)


window.mainloop()
