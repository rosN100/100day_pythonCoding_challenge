import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

symbols = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/',
 ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|',
 '}', '~']
numbers = ["0","1","2","3","4","5","6","7","8","9"]


print("Welcome to the PyPassword generator")
letters_count = int(input("How many letters do you want in the password?\n"))
symbols_count = int(input("How many symbols do you want in password?\n"))
numbers_count = int(input("How many numbers do you want in password?\n"))

num1 = letters_count + 1
num2 = symbols_count + 1
num3 = numbers_count + 1

# using string
# password = ""
# for element in range(1,num1):
#     password += random.choice(letters)
# for element in range(1, num2):
#     password += random.choice(symbols)
# for element in range(1, num3):
#     password += random.choice(numbers)
# print(password)

#using list
password = []
passwordf =[]
for element in range(1,num1):
    password.append(random.choice(letters))
for element in range(1, num2):
    password.append(random.choice(symbols))
for element in range(1, num3):
    password.append(random.choice(numbers))
for element in password:
    char = random.choice(password)
    passwordf.append(char)
final_password = ''.join(passwordf)
print(final_password)