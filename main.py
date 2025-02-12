from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}


try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    word_list = data.to_dict(orient="records")  # Convertir a lista de diccionarios



# ---------------------------- RANDOM FRENCH WORD GENERATOR ------------------------------- #
def word_generator():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_list)  # Elegir una palabra aleatoria
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=card_front_photo)
    flip_timer = window.after(3000, func=flip_card)
def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def is_known():
    word_list.remove(current_card)
    data = pd.DataFrame(word_list)
    data.to_csv("data/words_to_learn.csv", index=False)
    word_generator()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


# ********** CANVAS *******

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_photo = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_photo)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)


# ********** BUTTONS *******
# X button
x_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=word_generator)
unknown_button.grid(column=0, row=1)

# Y button
y_image = PhotoImage(file="images/right.png")
known_button = Button(image=y_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)

word_generator()

window.mainloop()