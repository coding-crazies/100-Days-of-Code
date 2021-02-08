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

from art import logo

profit=0

def print_report():
    '''Prints the report'''
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ₹{profit}")
    #print(f"{MENU['espresso']['ingredients']['water']+MENU['latte']['ingredients']['water']+MENU['cappuccino']['ingredients']['water']}")

def is_resource_sufficient(order_ingredients):
    '''Checks if the coffee machine has enough resources'''
    for item in order_ingredients:
        if order_ingredients[item]>=resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

def process_coins():
    '''Returns the total amount from coins inserted'''
    print("Please insert coins🪙:")
    total=int(input("How many quarters?: "))*0.25
    total+=int(input("How many dimes?: "))*0.1
    total+=int(input("How many nickles?: "))*0.05
    total+=int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successful(money_received,drink_cost):
    '''Check if the money given by the user is enough to buy a coffee'''
    if money_received>=drink_cost:
        change=round(money_received-drink_cost, 2)
        print(f"Here's ₹{change} in change💵.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded💵.")
        return False

def make_coffee(drink_name, order_ingredients):
    '''Deduct the required ingredients from the resources'''
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]
    print(f"Here's your {drink_name} ☕")

is_on=True

while is_on:
    print(logo)
    choice=input("What would you like? (espresso/latte/cappuccino): ")
    if choice=='off':
        is_on=False
    elif choice=='report':
        print_report()
    else:
        drink=MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment=process_coins()
            if is_transaction_successful(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])