from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

french_df = pd.read_csv('data/french_words.csv')
# print(french_df.describe())

# ‘records’ : list like [{column -> value}, … , {column -> value}]
french_dict = {}


def load_word_list():
    # using global value reference
    global french_dict
    try:
        df = pd.read_csv('data/words_to_learn.csv')
    except FileNotFoundError:
        df = pd.read_csv('data/french_words.csv')

    french_dict = df.to_dict(orient='records')
    print(len(french_dict))


def save_words_to_learn():
    df = pd.DataFrame(french_dict)
    df.to_csv('data/words_to_learn.csv', index=False)


def remove_word():
    print(current_card['French'])
    french_dict.remove(current_card)
    print('length:', len(french_dict))
    save_words_to_learn()
    next_card()


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(french_dict)
    # print(current_card['French'])
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=current_card['French'], fill='black')
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=current_card['English'], fill='white')


window = Tk()
window.title('Flashcards')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file='images/card_front.png')
card_back_img = PhotoImage(file='images/card_back.png')

canvas_image = canvas.create_image(400, 263, image=card_front_img)

card_title = canvas.create_text(
    400, 150, text='Title', font=('Arial', 40, 'italic'))
card_word = canvas.create_text(
    400, 263, text='word', font=('Arial', 60, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

cross_image = PhotoImage(file='images/wrong.png')
unknown_button = Button(
    image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

check_image = PhotoImage(file='images/right.png')
known_button = Button(
    image=check_image, highlightthickness=0, command=remove_word)
known_button.grid(row=1, column=1)

load_word_list()
next_card()

window.mainloop()
