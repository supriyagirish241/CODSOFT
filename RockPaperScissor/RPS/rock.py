import tkinter as tk
import random

# Initialize main window
root = tk.Tk()
root.title("Rock Paper Scissors Game 🎮")
root.geometry("400x400")
root.configure(bg="#f0f0f0")

# Scores
user_score = 0
computer_score = 0

# Choices list
choices = ["Rock", "Paper", "Scissors"]

# Labels
title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 18, "bold"), bg="#f0f0f0")
title.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="#f0f0f0")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Your Score: 0 | Computer Score: 0", font=("Arial", 12), bg="#f0f0f0")
score_label.pack(pady=10)

# Function to determine winner
def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        computer_score += 1

    # Display choices and result
    result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")
    score_label.config(text=f"Your Score: {user_score} | Computer Score: {computer_score}")

# Buttons for user choice
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

rock_btn = tk.Button(button_frame, text="Rock 🪨", width=12, command=lambda: play("Rock"))
paper_btn = tk.Button(button_frame, text="Paper 📄", width=12, command=lambda: play("Paper"))
scissors_btn = tk.Button(button_frame, text="Scissors ✂️", width=12, command=lambda: play("Scissors"))

rock_btn.grid(row=0, column=0, padx=5)
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn.grid(row=0, column=2, padx=5)

# Reset Button
def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    result_label.config(text="")
    score_label.config(text="Your Score: 0 | Computer Score: 0")

reset_btn = tk.Button(root, text="Play Again 🔁", command=reset_game)
reset_btn.pack(pady=10)

# Run the app
root.mainloop()
