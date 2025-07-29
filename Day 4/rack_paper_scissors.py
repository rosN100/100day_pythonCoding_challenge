import random
player_choice =input("What do you chose? rock,paper or scissors\n")
computer_options = ["rock","paper","scissors"]
computer_choice = random.choice(computer_options)
print(f"Computer chooses {computer_choice}")

if player_choice=="rock":
    if computer_choice == "paper":
        print("You Lost!")
    elif computer_choice == "scissors":
        print("You Won!")
    elif computer_choice == "rock":
        print("Try again!")
elif player_choice == "paper":
    if computer_choice == "rock":
        print("You won!")
    elif computer_choice == "scissors":
        print("You lost!")
    elif computer_choice == "paper":
        print("Try again!")
elif player_choice == "scissors":
    if computer_choice == "paper":
        print("You won!")
    elif computer_choice == "rock":
        print("You Lost!")
    elif computer_choice == "scissors":
        print("Try again!")