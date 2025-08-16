# Debugging

# def my_function():
#     for i in range (1,21):
#         if i == 20:
#             print("You got it")
#
# my_function()

# from random import randint
# dice_images = ["1","2","3","4","5","6"]
# dice_num = randint(0,5)
# print(dice_num)
# print(dice_images[dice_num])

# year = int(input("which year where you born?"))
#
# if year >1980 and year <= 1994:
#     print("You are millennial")
# elif year >1994:
#     print("You are gen z")
# try:
#     age = int(input("enter your age"))
# except ValueError:
#     print("Invalid input. enter your age in numerical format. for example - 18")
#     age = int(input("enter your age"))
#
# if age >18:
#     print(f"You can drive at age {age}")

# word_per_page = 0
# pages = int(input("Number of pages:"))
# word_per_page =int(input("Number of words per page:"))
# print(word_per_page)
# total_words = pages * word_per_page
# print(total_words)
#
# import random
# import maths
#
# def mutate(a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item * 2
#         new_item += random.randint(1,3)
#         new_item = maths.add(new_item, item)
#         b_list.append(new_item)
#     print(b_list)
#
# mutate([1, 2, 3, 5, 8, 13])

# def odd_or_even(number):
#     if number % 2 == 0:
#         return "This is an even number."
#     else:
#         return "This is an odd number."
#
# result = odd_or_even(33)
# print(result)

# def is_leap(year):
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False
#
# result = is_leap(2000)
# print(result)

def fizz_buzz(target):
    for number in range(1, target + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print([number])

fizz_buzz(10)