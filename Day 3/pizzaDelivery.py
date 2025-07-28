bill = 0
print("Welcome to the python pizza delivery!")
size = input("What size pizza do you want? S,M or L:")
pepperoni = input("Do you want pepperoni on your pizza? type y for yes and n for no:")
extra_cheese = input("Do you want extra cheese on your pizza? type y for yes and n for no:")

if size == "S":
    bill +=15
    if pepperoni =="y":
        bill +=2
elif size == "M":
    bill +=20
    if pepperoni =="y":
        bill +=3
elif size == "L":
    bill +=25
    if pepperoni =="y":
        bill +=3
else:
    print("incorrect entry!")
if extra_cheese == "y":
    bill +=1
print(f"You total bill is: ${bill}")