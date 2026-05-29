from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}
to_learn = {}

try:
    data = pd.read_csv("Day 31/data/words_to_learn.csv")
except FileNotFoundError:
    original_file = pd.read_csv("Day 31/data/french_words.csv")
    to_learn = original_file.to_dict(orient="records")
# print(data) ye ek dataframe ko roop mein ban gya hai
else:
    to_learn = data.to_dict(orient="records")
# print(to_learn)


def next_word():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_word["French"], fill="black")
    canvas.itemconfig(card_background, image=white_card_image)
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, fill="white", text="English")
    canvas.itemconfig(card_word, fill="white", text=current_word["English"])
    canvas.itemconfig(card_background, image=green_card_image)

def is_known():
    to_learn.remove(current_word)
    data = pd.DataFrame(to_learn)
    data.to_csv("Day 31/data/words_to_learn.csv", index=False)
    next_word()

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
white_card_image = PhotoImage(file="Day 31/images/card_front.png")
green_card_image = PhotoImage(file="Day 31/images/card_back.png")
card_background = canvas.create_image(400, 263, image=white_card_image)
card_title = canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="Day 31/images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_word)
cross_button.grid(row=1, column=0)

right_image = PhotoImage(file="day 31/images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_word()


window.mainloop()
