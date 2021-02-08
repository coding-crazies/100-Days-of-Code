MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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

profit=0

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")
    #print(f"{MENU['espresso']['ingredients']['water']+MENU['latte']['ingredients']['water']+MENU['cappuccino']['ingredients']['water']}")

in_on=True

while is_on:
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=='off':
        is_on=False
    elif choice=='report':
        print_report()
    else:
        drink=MENU[choice]
        print(drink)