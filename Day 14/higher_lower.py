import celebrities
import random

# generate celebrity A & B randomly from the list where A should not be equal be B
def generate_random_celeb():
    return (random.choice(celebrities.data))

# compare A and B follower count. print win or loss
def result(choice_one,choice_two):
    if choice_one['follower_count'] > choice_two['follower_count']:
        return choice_one

    elif choice_one['follower_count'] < choice_two['follower_count']:
        return choice_two

# main control function
game_is_on = True
score = 0
choice_one = generate_random_celeb()
choice_two = generate_random_celeb()
print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}")
print(f"Against B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']}")

while game_is_on:
    response = input("Who has more followers? Type 'A' or 'B': ")
    outcome = result(choice_one,choice_two)
    if response == 'A' and outcome == choice_one:
        score +=1
        print("\n" * 20)
        print(f"You are right! Current Score: {score}")
        choice_two = generate_random_celeb()
        print(f"Compare A: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}")
        print(f"Against B: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']}")
    elif response == 'B' and outcome == choice_two:
        score += 1
        print("\n" * 20)
        print(f"You are right! Current Score: {score}")
        choice_one = generate_random_celeb()
        print(f"Compare A: {choice_two['name']}, a {choice_two['description']}, from {choice_two['country']}")
        print(f"Against B: {choice_one['name']}, a {choice_one['description']}, from {choice_one['country']}")
    else:
        print(f"You lost! Score: {score}")
        game_is_on = False