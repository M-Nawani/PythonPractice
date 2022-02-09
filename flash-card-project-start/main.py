from tkinter import *

import pandas
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"


# ------------------ACCESSING THE DATA FILE--------------------------------- #
try:
    data_file = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data_file = pd.read_csv("data/french_words.csv")
    to_learn = original_data_file.to_dict(orient="records")
else:
    to_learn = data_file.to_dict(orient="records")

current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfigure(card_title, text='French', fill="black")
    canvas.itemconfigure(card_word, text=current_card['French'], fill="black")
    canvas.itemconfigure(canvas_image, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def remove_card():
    to_learn.remove(current_card)
    next_card()
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    global current_card
    canvas.itemconfigure(canvas_image, image=back_image)
    canvas.itemconfigure(card_title, text='English', fill="white")
    canvas.itemconfigure(card_word, text=current_card['English'], fill="white")

# -------------------UI CREATION---------------------------------------------- #


window = Tk()
window.title("Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
flip_timer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_image)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="Word", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=remove_card)
right_button.grid(row=1, column=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
print(current_card)

window.mainloop()

