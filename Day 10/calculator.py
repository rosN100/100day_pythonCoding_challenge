import calculator_art
print(calculator_art.art)
def calculator(number1, number2, operator):
    if operator == "+":
        return number1 +number2
    elif operator == "-":
        return number1-number2
    elif operator == "*":
        return number1*number2
    elif operator == "/":
        return number1/number2
    else:
        return "invalid input!"

def start_calculation():
    should_continue = True
    first_number = int(input("What's the first number?\n"))
    while should_continue:
        print(f"+\n -\n *\n /\n")
        operator = input("Pick the operation:")
        second_number = int(input("What's next number?\n"))
        result = calculator(first_number,second_number,operator)
        print(f"{first_number} {operator} {second_number} = {result}")
        next_operation = input(f"Type 'y' to continue calculation with {result} or Type 'n' to start a fresh calculation")
        if next_operation == 'y':
            first_number = result
        elif next_operation == 'n':
            should_continue = False
start_calculation()