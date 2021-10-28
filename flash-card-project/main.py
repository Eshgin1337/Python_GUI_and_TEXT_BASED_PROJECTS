import random
import tkinter
import pandas

BACKGROUND_COLOR = "#B1DDC6"
present_card = {}
words_to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    initial_data = pandas.read_csv("data/french_words.csv")
    words_to_learn = initial_data.to_dict(orient="records")
else:
    words_to_learn = data.to_dict(orient="records")


def is_known():
    words_to_learn.remove(present_card)
    unknown_data = pandas.DataFrame(words_to_learn)
    unknown_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# Function to choose a random French word
def next_card():
    global present_card, flip_timer
    window.after_cancel(flip_timer)
    present_card = random.choice(words_to_learn)
    french_word = present_card["French"]
    card_front_canvas.itemconfig(title_text, text="French", fill="black")
    card_front_canvas.itemconfig(word, text=french_word, fill="black")
    card_front_canvas.itemconfig(view_image, image=front_photo)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    card_front_canvas.itemconfig(view_image, image=back_photo)
    card_front_canvas.itemconfig(title_text, text="English", fill="white")
    card_front_canvas.itemconfig(word, text=present_card["English"], fill="white")


window = tkinter.Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title("Flash-Card App")

flip_timer = window.after(3000, func=flip_card)

card_front_canvas = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_photo = tkinter.PhotoImage(file="images/card_front.png")
back_photo = tkinter.PhotoImage(file="images/card_back.png")
view_image = card_front_canvas.create_image(400, 263, image=front_photo)
title_text = card_front_canvas.create_text(400, 150, text="Title", fill="black", font=("Arial", 40, "italic"))
word = card_front_canvas.create_text(400, 263, text="word", fill="black", font=("Arial", 60, "bold"))
card_front_canvas.grid(row=0, column=0, columnspan=2)

wrong_button_image = tkinter.PhotoImage(file="images/wrong.png")
wrong_button = tkinter.Button(image=wrong_button_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_button_image = tkinter.PhotoImage(file="images/right.png")
right_button = tkinter.Button(image=right_button_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
