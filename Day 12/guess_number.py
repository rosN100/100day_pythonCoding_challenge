import guess_number_logo
import random
print(guess_number_logo.logo)
print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")

should_show = True
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard':\n")
attempts = 0
if difficulty_level == 'hard':
    attempts = 5
elif difficulty_level == 'easy':
    attempts = 10
current_attempt_count = 0

# generate a number
def decide_number():
    return random.randint(1,100)
def how_close(guessed_number, decided_num):
    if guessed_number == decided_num:
        return "You won!"
    elif guessed_number > decided_num:
        return "Too High!"
    elif guessed_number < decided_num:
        return "Too Low!"
    elif current_attempt_count > attempts:
        return "You lost!"

decided_num = decide_number()
print(f"decided_number: {decided_num}")

while should_show:
    guessed_number = int(input("Make a guess:\n"))
    current_attempt_count += 1
    result = how_close(guessed_number,decided_num)
    print(result)
    if result == "You lost!" or result == "You won!":
        should_show = False
    print("Guess again!")





