import tkinter as tk
from PIL import ImageTk, Image
import random

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("600x400")
root.config(bg="White")


rock_img = ImageTk.PhotoImage(Image.open("RockPaperScissor/RPS/Rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("RockPaperScissor/RPS/Paper.png").resize((100, 100)))
scissor_img = ImageTk.PhotoImage(Image.open("RockPaperScissor/RPS/Scissors.png").resize((100, 100)))
logo_img = ImageTk.PhotoImage(Image.open("RockPaperScissor/RPS/logo.png").resize((150, 150)))


welcome_frame = tk.Frame(root, bg="lightblue")
game_frame = tk.Frame(root, bg="lightblue")

user_score = 0
computer_score = 0


result_label = None
user_choice_label = None
computer_choice_label = None
score_label = None


def show_welcome():
    welcome_frame.pack(fill="both", expand=True)
    tk.Label(welcome_frame, image=logo_img, bg="white").pack(pady=(70, 20)) 
    tk.Label(welcome_frame, text="Rock Paper Scissors Game", font=("Helvetica", 30, "bold"), bg="white").pack(pady=20)
    tk.Button(welcome_frame, text="Play", font=("Helvetica", 20, "bold"), bg="black", fg="white", command=start_game).pack(pady=(20, 30))


def start_game():
    welcome_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)

    global user_choice_label, computer_choice_label, result_label, score_label

  
    left_frame = tk.Frame(game_frame, bg="white")
    left_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)

    tk.Label(left_frame, text="You Choose:", font=("Helvetica", 25, "bold"), bg="white").pack(pady=10)
    tk.Button(left_frame, image=rock_img, command=lambda: play("rock")).pack(pady=5)
    tk.Button(left_frame, image=paper_img, command=lambda: play("paper")).pack(pady=5)
    tk.Button(left_frame, image=scissor_img, command=lambda: play("scissor")).pack(pady=5)

    user_choice_label = tk.Label(left_frame, text="", font=("Helvetica", 25, "bold"), bg="white")
    user_choice_label.pack(pady=10)

 
    right_frame = tk.Frame(game_frame, bg="white")
    right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    tk.Label(right_frame, text="Computer Chooses:", font=("Helvetica", 15, "bold"), bg="white").pack(pady=10)
    computer_choice_label = tk.Label(right_frame, text="", font=("Helvetica", 15, "bold"), bg="white")
    computer_choice_label.pack(pady=10)

  
    center_frame = tk.Frame(game_frame, bg="white")
    center_frame.pack(side="top", expand=True)

    score_label = tk.Label(center_frame, text=f"You: {user_score} | Computer: {computer_score}", font=("Helvetica", 20), bg="white")
    score_label.pack(pady=10)

    result_label = tk.Label(center_frame, text="", font=("Helvetica", 16, "bold"), fg="blue", bg="white")
    result_label.pack(pady=10)

    tk.Button(center_frame, text="Play Again", font=("Helvetica", 12), command=reset_game).pack(pady=10)


def play(user_choice):
    global user_score, computer_score

    choices = ["rock", "paper", "scissor"]
    computer_choice = random.choice(choices)

    user_choice_label.config(text=f"You chose {user_choice.capitalize()}")
    computer_choice_label.config(text=f"Computer chose {computer_choice.capitalize()}")

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissor") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissor" and computer_choice == "paper"):
        result = "You Win! 🎉"
        user_score += 1
    else:
        result = "You Lose! 😢"
        computer_score += 1

    result_label.config(text=result)
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_choice_label.config(text="")
    computer_choice_label.config(text="")
    result_label.config(text="")
    score_label.config(text=f"You: {user_score} | Computer: {computer_score}")

show_welcome()
root.mainloop()
