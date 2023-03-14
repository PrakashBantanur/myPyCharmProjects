
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

profit = 0
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'Money': 0
}
# TODO: 1. Print the report of all the resource of coffee machine
# TODO: 2. Check the resources are sufficient to make drink
# TODO: 3. Print report


# TODO: 4. Check resources sufficient?
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True to process, False if the ingredients are not enough"""
    for items in order_ingredients:
        if order_ingredients[items] >= resources[items]:
            print(f'Sorry, not enough {items}')
            return False
        return True


def process_coins():
    """ Returns total amount"""
    print('Please insert coins!')
    total = int(input('how many quarters?:')) * 0.25
    total += int(input('how many dimes?:')) * 0.1
    total += int(input('how many nickles?:')) * 0.05
    total += int(input('how many pennies?:')) * 0.01
    return total


def is_transaction_successful(inserted_coins, drink_cost):
    """Returns True when payment accepted, or False payment having not enough money"""
    if inserted_coins <= drink_cost:
        print(f"Sorry that's not enough money to purchase {choice}. Money refunded.")
        return False
    else:
        change = round(inserted_coins - drink_cost, 2)
        print(f"Here is {change} in change")
        global profit
        profit += drink_cost
        return True


def update_resources(drink_name, resource_update):
    for item in resource_update:
        resources[item] = resources[item] - resource_update[item]
    print(f'Here is your ordered {drink_name}')


while is_on:
    choice = input('What would you like? (espresso/latte/cappuccino): ').lower()
    if choice == 'off':
        is_on=False
    elif choice == 'report':
        print(f"Water:{resources['water']}ml")
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee:{resources['coffee']}gm")
        print(f"Money:{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                update_resources(choice, drink['ingredients'])