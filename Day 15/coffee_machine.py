# units: water/milk in ml, coffee in g; cost in USD
menu = {
    "espresso": {
        "ingredients": {"water": 50, "milk": 0, "coffee": 18},
        "cost": 2.00
    },
    "americano": {
        "ingredients": {"water": 300, "milk": 0, "coffee": 18},
        "cost": 2.50
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 3.50
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.00
    }
}

resources = {
    'water': 1000,
    'milk': 1000,
    'coffee': 500,
    'money': 2.5
}
state = True

supported_coin_types = {
    'quater': 0.25,
    'dime': 0.10,
    'nickle': 0.05,
    'pennie': 0.01
}
def check_respurce(coffee):
    if resources['water'] >= menu[coffee]['ingredients']['water']:
        if resources['milk'] >= menu[coffee]['ingredients']['milk']:
            if resources['coffee'] >= menu[coffee]['ingredients']['coffee']:
                return True
    else:
        return False

def check_coins(coin,count,response):
    unit = supported_coin_types[coin]
    value = count*unit
    if value == menu[response]['cost']:
        return True
    else:
        return False

def process_transaction(response):
    resources['water'] -= menu[response]["ingredients"]["water"]
    resources['milk'] -= menu[response]["ingredients"]["milk"]
    resources['coffee'] -= menu[response]["ingredients"]["coffee"]
    resources['money'] += menu[response]['cost']
    print("Enjoy your coffee!")

while state:
    response = (input("What would you like? (espresso/latte/cappuccino):\n")).lower()
    if response == 'report':
        print(f"Here is the resource status: \n1. Water: {resources['water']} \n2. Milk: {resources['milk']} \n3. Coffee: {resources['coffee']} \n4.Balance: {resources['money']}")
    elif response == 'off':
        state = False
    elif response == "espresso" or response == "americano" or  response == "latte" or response == "cappuccino" :
        output = check_respurce(response)
        if output:
            coin = input("Insert coins (quater,dime,nickel,pennie):\n")
            count = int(input("enter the number of coins\n"))
            verification = check_coins(coin,count,response)
            if verification:
                process_transaction(response)
        else:
            print("Sorry we are out of few ingredients!")

