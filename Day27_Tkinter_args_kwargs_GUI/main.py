from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


window = Tk()

window.title('First GUI Program')

window.minsize(width=500, height=300)

# Label
my_label = Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack(side='left')
my_label.pack()

# Change existing text
# my_label['text']  = 'New Text'
# or
my_label.config(text='New Text1')

# Button
button = Button(text='Click Me', command=button_clicked)
button.pack()

# Entry
input = Entry(width=30)
input.insert(END, string='Some text to begin with.')
print(input.get())
input.pack()


window.mainloop()
