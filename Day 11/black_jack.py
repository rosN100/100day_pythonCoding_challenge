import black_jack_art
import random
card = [11,2,3,4,5,6,7,8,9,10,10,10,10]
response = input("Do you want to start the game of black jack? Type 'yes' or 'no'\n")
should_show = True
computer_card = []
player_card = []
game_result =''

def generate_random_card():
    return random.choice(card)

def continue_game():
    computer_card.extend([generate_random_card()])
    player_card.extend([generate_random_card()])
    return computer_card,player_card
def skip():
    computer_card.extend([generate_random_card()])
    return computer_card

def result(player_card, computer_card):
    if sum(player_card) >21:
        return "You lost!"
    elif sum(computer_card) >21:
        return "You Won!"
    elif sum(computer_card) < 17:
        skip()
    elif (21- sum(player_card)) < (21-sum(computer_card)):
        return "You Won!"
    elif (21- sum(player_card)) > (21-sum(computer_card)):
        return "You lost!"

continue_game()
start = True

while should_show:
    if response == 'yes':
        continue_game()
        start = False
        print(f"Your cards:{player_card}. Current score = {sum(player_card)}")
        print(f"One of the computer card = {computer_card[-1]}")
        response = 'next'
    elif response == 'no':
        print("goodbye! have a nice day!")
        should_show = False
        break
    if response == 'y':
        data = continue_game()
        game_result = result(data[0],data[1])
        print(f"Your cards: {player_card}. Current score = {sum(player_card)}")
        print(f"Computer card: {computer_card[0]}")
        response = 'next'

    if response == 'n':
        skip()
        game_result = result(player_card,computer_card)
        print(f"Your cards: {player_card}. Current score = {sum(player_card)}")
        print(f"Computer card: {computer_card[0]}")
        response = 'next'
    if response == 'next':
        response = input("Type 'y' to get another card or 'n' to skip!")

    if game_result == "You lost!":
        print(game_result)
        print(f"Your cards:{player_card}. Current score = {sum(player_card)}")
        print(f"Computer card = {computer_card}")
        should_show = False
    if game_result == 'You Won!':
        print(game_result)
        print(f"Your cards:{player_card}. Current score = {sum(player_card)}")
        print(f"Computer card = {computer_card}")

