from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

state = True

while state:
    options = menu.get_items()
    choice = input(f"What do you like to have? {options}:").lower()
    if choice == "off":
        state = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.money_received(drink.cost):
            coffee_maker.make_coffee(drink)