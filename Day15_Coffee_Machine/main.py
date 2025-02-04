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
    "money":0.00
}

coins = {
    'quarter':0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01,
}

bank = 0.00

def update_resources(beverage):
    resources['water'] -= beverage['ingrients']['water']
    resources['milk'] -= beverage['ingrients']['milk']
    resources['coffee'] -= beverage['ingrients']['coffee']
    resources['money'] += beverage['cost']


def process_transaction(beverage_cost):
    total=0.00
    ret = 0

    i = 0
    trans=[]

    print('Please insert coins:')
    trans.append(int(input('How many quarters? ')))
    trans.append(int(input('How many dimes? ')))
    trans.append(int(input('How many nickels? ')))
    trans.append(int(input('How many pennies? ')))

    # add up the coins
    for coin in coins:
        total += coins[coin] * trans[i]
        i += 1

    if total < beverage_cost:
        print('Sorry that''s not enough money. Money refunded.')
        ret = -1
    else:
        # change
        print(f'Here is ${total - beverage_cost} in change')

    return ret

def process_report():
    rpt = (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${resources['money']}"
    )
    print(rpt)

def check_resources(ingredients):
    # loop through ingredients
    for x in ingredients:
        if (resources[x] - ingredients[x]) < 0:
            print(f"Sorry there's not enough {x}")
            return -1
    return 0


def coffee_machine_program():

    # prompt user for choice
    response = input('What would you like?').lower()

    drink = MENU[response]

    # Check resources
    ret = check_resources(drink['ingredients'])
    if ret == 0:
        ret = process_transaction(drink['cost'])
        if ret == 0:
            # Update resources
            update_resources(drink)


coffee_machine_program()