import tkinter as tk
from tkinter import messagebox
import random

#words
words = ['programming','computer','python','jackpot','jawbreaker','topaz','quartz','esponiage', 'hockey','soccer',
         'basketball','dolphin','pancakes','waffles','espresso','decode','exhale','cardigan','undercover','pizza',
         'presents','license','vampire','acorn','squirrel','jelly','jigsaw','jazz','beekeeper','koala','graduation',
         'evolution','folklore','fearless','reputation','midnight','illuminate','wonder','perfect']

#variables
word_to_guess = random.choice(words)
guessed_word = ['_']*len(word_to_guess)
incorrect_guesses = []
max_incorrect_guesses = 6
incorrect_count = 0

#functions
def reset_game():
    global word_to_guess, guessed_word,incorrect_guesses, max_incorrect_guesses, incorrect_count
    word_to_guess = random.choice(words)
    guessed_word = ['_']*len(word_to_guess)
    incorrect_guesses.clear()
    incorrect_count = 0
    canvas.delete("all")
    draw_gallows()
    update_display()
    enable_all_buttons()
def update_display():
    guessed_word_label.config(text = " ".join(guessed_word))
    incorrect_guesses_label.config(text = f"Incorrect Guesses: {' '.join(incorrect_guesses)}")
    hangman_status_label.config(text =f"Attempts: {incorrect_count}/{max_incorrect_guesses}")
    if '_' not in guessed_word:
        messagebox.showinfo("Congratulations!", "You won the game!")
        reset_game()
    elif incorrect_count>= max_incorrect_guesses:
        messagebox.showinfo("Game Over!",f"You lost! The word was {word_to_guess}")
        reset_game()
def handle_guess(letter, button):
    global incorrect_count
    button.config(state = tk.DISABLED)
    if letter in word_to_guess:
        for i,l in enumerate(word_to_guess):
            if l == letter:
                guessed_word[i] = letter
            else:
                continue
    else:
        incorrect_guesses.append(letter)
        incorrect_count+=1
        draw_hangman()
    update_display()
def enable_all_buttons():
   for button in letter_buttons:
       button.config(state = tk.NORMAL)
def draw_gallows():
    canvas.create_line(50,250,200,250,width = 3)
    canvas.create_line(125,250,125,50, width = 3)
    canvas.create_line(125,50,200,50, width = 3)
    canvas.create_line(200,50,200,80, width = 3)
def draw_hangman():
    if incorrect_count == 1:
        canvas.create_oval(180,80,220,120, width = 3)
    elif incorrect_count == 2:
        canvas.create_line(200, 120, 200,180, width = 3)
    elif incorrect_count == 3:
        canvas.create_line(200,140,170,110, width = 3)
    elif incorrect_count == 4:
        canvas.create_line(200, 140, 230, 110, width=3)
    elif incorrect_count == 5:
        canvas.create_line(200, 180, 180, 220, width=3)
    elif incorrect_count == 6:
        canvas.create_line(200, 180, 220, 220, width=3)

root = tk.Tk()
root.title('Hangman')


guessed_word_label = tk.Label(root, text = " ".join(guessed_word))
guessed_word_label.pack(pady = 10)

incorrect_guesses_label = tk.Label(root, text =f"Incorrect Guesses: {' '.join(incorrect_guesses)}")
incorrect_guesses_label.pack(pady = 10)

hangman_status_label = tk.Label(root, text = f"Attempts: {incorrect_count}/{max_incorrect_guesses}")
hangman_status_label.pack(pady =10)

canvas = tk.Canvas(root, width = 300, height = 300, bg = 'white')
canvas.pack(pady = 10)

draw_gallows()

letter_buttons = []
button_frame = tk.Frame(root)
button_frame.pack(pady = 10)

def create_button_handler(letter,button):
    def button_handler():
        handle_guess(letter, button)
    return button_handler

for i,letter in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    button = tk.Button(
        button_frame,
        text = letter,
        width = 4,
        )
    button.config(command = create_button_handler(letter.lower(),button))
    button.grid(row = i//9, column = i%9,padx = 5,pady = 5)
    letter_buttons.append(button)
    
reset_button = tk.Button(root, text = 'Reset Game', command = reset_game)
reset_button.pack(pady = 20)

root.mainloop()
