from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

running = True

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


while running:

    user_input = input(f"What would you like? ({menu.get_items()}): ")
    
    if user_input == 'off':
        running = False
        break

    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()

    else:
        drink = menu.find_drink(user_input)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
            else:
                print("Sorry not enough money.")
        else:
            print("Insufficient resources.")