import math
def life_in_weeks(current_age):
    avg_human_lifespan = 90*52.14
    weeks_lived = current_age*52.14
    print(f"you have lived {weeks_lived}weeks")
    weeks_left = math.floor(avg_human_lifespan - weeks_lived)
    print(f"You have {weeks_left} weeks left.")

current_age = int(input("what's your current age?"))

life_in_weeks(current_age)