# scope
# number = 4

# def inside_function():
#     number = 3
#     print(number)
#
# inside_function()
# print(number)

# Local scope
def inside_my_game():
    power = 25 #local scope "power" code outside of inside_my_game doesn't have access.
    return power

power = inside_my_game()
print(power)

# global scope
power = 25

def inside_game():
    print(power)   # inside_game function has access to power even inside the function because power lies in global scope

inside_game()

# there is no concept of Block scope in python- for example

if 2>1:
    num = 45 # this num has global scope

def inside_function():
    number = 456 # this is local scope - "number" can only be accessed within 

