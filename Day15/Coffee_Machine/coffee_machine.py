MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def print_resources():
    global money
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Money : {money}")

def check_resources(coffee):
    selected_coffee = MENU[coffee]
    required_ingredients = selected_coffee["ingredients"]

    if resources["water"]<required_ingredients["water"]:
        print("Sorry there is insufficient water")
        return False
    elif resources["milk"]<required_ingredients["milk"]:
        print("Sorry there is insufficient milk")
        return False
    elif resources["coffee"]<required_ingredients["coffee"]:
        print("Sorry there is insufficient coffee")
        return False
    
    return True

def transaction_succesful(coffee, inserted_money):
    global money 

    selected_coffee = MENU[coffee]
    coffee_cost = selected_coffee["cost"]

    if inserted_money < coffee_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
    money += coffee_cost
    resources["coffee"] -= selected_coffee["ingredients"]["coffee"]
    resources["milk"] -= selected_coffee["ingredients"]["milk"]
    resources["water"] -= selected_coffee["ingredients"]["water"]

    if inserted_money>coffee_cost:
        print(f"Change returned : {inserted_money - coffee_cost}")

    return True


running = True

while running:
    user_input = input("What would you like? (espresso/latte/cappuccino): ")

    if user_input == 'off':
        running = False
        break
    elif user_input == 'report':
        print_resources()
    elif user_input in MENU:

        coffee = user_input

        resources_sufficient = check_resources(coffee)

        if resources_sufficient:
            print(f"Cost of coffee : {MENU[coffee]["cost"]}")
            
            print("Insert coins:")
            quarters = int(input("Quarters : "))
            dimes = int(input("Dimes : "))
            nickels = int(input("Nickels : "))
            cents = int(input("Cents : "))

            money_inserted = (quarters*0.25)+(dimes*0.1)+(nickels*0.05)+(cents*0.01)

            if transaction_succesful(coffee, money_inserted):
                print(f"Here is your {coffee}. Enjoy!")