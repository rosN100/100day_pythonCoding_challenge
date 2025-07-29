# To generate random numbers in python - Mersenne Twister
import random
import my_module
# random_int = random.randint(4,98)
#
# print(random_int)

#modules
# print(my_module.my_number)

# random_number_0_1 = random.random()*10
# print(random_number_0_1)
#
# print(random.uniform(34,67))

# random_num = round(random.random()*10)
# if random_num%2 ==0:
#     print("Tails")
# else:
#     print("heads")

#lists - it's a data structure. Used when order of occurrence
#states in USA  in the order they joined union
states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii"
]
# print(states_of_america[8])
# print(states_of_america[-2])
# print(states_of_america[6:10])
#
# states_of_america[4]="pencil"
# print(states_of_america)
#
# states_of_america.append("pune")
# print(states_of_america)
#
# #extend the list
# states_of_america.extend(["mumbai","ranchi"])
# print(states_of_america)

my_friends = ["gaurav", "pranav","saurabh","Ayush","amit","Abhishek","Aman"]
index = random.randint(0,6)
print(my_friends[index])

print(random.choice(my_friends))
# print(states_of_america[50])
print(len(states_of_america))

#nested lists
my_bag =[["mango","apple","banana"],["Ladies finger","onion","tomato","potato"]]
print(my_bag[0])
print(my_bag[0][1])

