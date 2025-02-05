import os

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
    "bank": 0.00
}

coins = {
    'quarter':0.25,
    'dime': 0.10,
    'nickel': 0.05,
    'penny': 0.01,
}

bank = 0.00

def update_resources(beverage):
    
    # print('update_resources()', 'beverage', beverage,sep='|')
    
    for key in beverage['ingredients']:
        resources[key] -= beverage['ingredients'][key]
        
    resources['bank'] += beverage['cost']
        
    

def process_transaction(drink_name, beverage_cost):
    total=0.00
    ret = True

    i = 0
    trans=[]

    print('Please insert coins:')
    for key in coins:
        while True:
            amount = input(f'How many {key}s? ')
            try:
                amount = int(amount)
            except:
                print('Please enter numeric digits.')
                continue
            trans.append(amount)
            break
    

    # add up the coins
    for coin in coins:
        total += coins[coin] * trans[i]
        i += 1

    if total < beverage_cost:
        print('Sorry that''s not enough money. Money refunded.')
        ret = False
    else:
        # change
        print(f'Here is ${total - beverage_cost} in change')
        print(f'Here is you\'re {drink_name} ☕. Enjoy !!!')

    return ret


def view_report():
    rpt = (
        f"Water: {resources['water']}ml\n"
        f"Milk: {resources['milk']}ml\n"
        f"Coffee: {resources['coffee']}g\n"
        f"Money: ${resources['bank']}"
    )
    print(rpt)


def check_resources(ingredients):
    # loop through ingredients
    for x in ingredients:
        if (resources[x] - ingredients[x]) < 0:
            print(f"Sorry there's not enough {x}")
            return False
    return True


def coffee_machine_program():

    # clear terminal
    # os.system('cls')
    
    # build list to use to validate input selection
    choice_key_list = list(MENU.keys())
    choice_key_list.append('report')
    choice_key_list.append('off')
    
    # prompt user for choice
    while True:
        response = input('What would you like? (espresso/latte/cappuccino): ').lower()
        # validate
        if response not in choice_key_list:
            print('Invalid choice. The valid choices are: espresso/latte/cappuccino.')
            continue
        break
        
    match response:
        case 'report':
            # display resources report
            view_report()
        case 'off':
            # exit program
            return
        case _:
            # process drink order
            drink = MENU[response]

            # Check resources
            if check_resources(drink['ingredients']):
                if process_transaction(response, drink['cost']):
                    # Update resources
                    update_resources(drink)
                
    coffee_machine_program()

        

coffee_machine_program()
