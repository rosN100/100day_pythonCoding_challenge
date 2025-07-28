print("Welcome to the treasure Island. Your mission is to find the tressure")
choice1 = input("You are on a cross road. where you wanna go from here? left or right:\n")
if choice1 == "left":
    choice2 = input("What you want to do next? swim or wait for a boat. Type swim or wait:\n")
    if choice2 == "swim":
        print("Game over! crocodiles ate you :(")
    if choice2 == "wait":
        choice3 = input("You reached a place using boat. which door you want to enter? red, yellow or blue:")
        if choice3 == "red":
            print("Game over! Dragon killed you :(")
        elif choice3 == "blue":
            print("Gave over! witch casted a sleeping spell on you :(")
        elif choice3 == "yellow":
            print("You win! take away your treasure")
        else:
            print("Gave over! wrong input :(")
elif choice1 == "right":
    print("Game over! a rock crushed you :(")
else:
    print("Gave over! wrong input :(")