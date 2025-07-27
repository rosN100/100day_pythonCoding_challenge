# value = str(123456)
# print(len(value))

# Strings
# print("Hello"[0])
# print("Hello"[-1])
# print("123"+"987")

#Integer
# writing large numbers
# num = 1_23_456 # "_" is ignored
# num2 = 4_56_897
# print(num+num2)

#float
float_num = 4.78

#Boolean
# print(True)
# print(False)
#
# print(type(45_678))
# print(type(True))
# print(type("roshan"))
# print(type([3,4,5,6]))
# print(type("true"))
# print(type(6.890))
# print(type(type(123.45)))

# num1 = "123"
# print(type (num1))
# num = int("123")
# print(type (num))
#
# print("this is line of text" + str(len(input("who are you?"))))

#mathematical operations
# print (9/2)  # return quotient as a float
# print(type(9/2))
#
# print(9//2) # return quotient as an integer
# print(9 % 2) # returns remainder

#exponent
# print(2**2)  # 2 to the power of 2

# BODMAS(L->R) is followed while mathematical operation ( (),**,* or /, + or -) left -> Right
print((2+2)*9+5+ 3**3+6*5)  # 98
"""
4*9+5+3**3+6*5
4*9+5+27+6*5
36+5+27+30

"""
print(3*3+3/3-3) # 9+1-3 = 7
num = 45.456789
print(int(num))
print(round(num,2))
num = 45.856789
print(round(num,4))

score = 0
# user scores a point
score = score + 1
print(score)
score +=1
print(score)
score -=0.5
print(score)
score *= 3
print(score)
score /= 3
print(score)

# f string
print(f"final score is {score}")