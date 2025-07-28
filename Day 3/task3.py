"""
if condition:
    do this
else:
    do this
"""
# water_level = 55
# if water_level>80:
#     print("drain the water")
# else:
#     print("keep filling")

# print("Welcome to roller coaster")
# height = int(input("what's your height?"))
#
# if height >= 120:
#     print("You can buy the ticket")
# else:
#     print("sorry! you can't buy the ticket")

# test = 123
# if test == 123:
#     print("You got it right :)")
# else:
#     print("sorry, try again")
# test2 = 160
#
# if test2 != 140:
#     print("you go that right")
# else:
#     print("try again later")

# Modulo operator (%)
# answer = 10 % 3
# print(answer)

# even or odd
# number = int(input("enter the number"))
# if number % 2 == 0:
#     print("it's an even number")
# else:
#     print("it's odd number")

# print("wellcome to roller coaster")
# height = int(input("What's your height?"))
# age = int(input("what's your age?"))
#
# if height>= 120:
#     if age <= 12:
#         print("You can buy the ticket. It costs 5$")
#     elif age <= 18:
#         print("You can buy the ticket. It costs 7$")
#     else:
#         print("You can buy the ticket. It costs 12 $")
# else:
#     print("sorry, you can't buy the ticket")

# weight = 85
# height = 1.85
#
# bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

# if bmi < 18.5:
#     print("You are in underweight range\n")
# elif bmi < 25:
#     print("You are in normal weight range\n")
# else:
#     print("You are in overweight range\n")

#multiple if's
print("wellcome to roller coaster")
height = int(input("What's your height?"))
age = int(input("what's your age?"))
bill = 0

if height > 120:
    if age <= 12:
        bill +=5
        print("You are eligible for a ticket. It costs 5$")
    elif age <= 18:
        bill += 7
        print("You are eligible for a ticket. It costs 7$")
    elif age >= 45 and age <= 55:
        print("You get a midlife crisis discount. Congrats!")
    else:
        bill += 12
        print("You are eligible for a ticket. It costs 12 $")
    want_photo = input("do you want photo?enter y for yes and n for no")
    if want_photo == "y":
        bill +=3
        print(f"Your total is {bill}. Thanks for the purchase!")
    else:
        print(f"Your total is {bill}. Thanks for the purchase!")
else:
    print("sorry, you can't buy the ticket")

#logical operators
# and , or, not

