import os
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def execute_coffee_maker():
    
    # myMenuItem = MenuItem()
    myMenu = Menu()
    myCoffeeMaker = CoffeeMaker()
    myMoneyMachine = MoneyMachine()
    
    coffee_maker_on = True
    
    choice_key_list = myMenu.get_items()    
    choice_key_list += 'report'
    choice_key_list += 'off'
    
    while coffee_maker_on:
        # prompt user for choice
        while True:
            response = input('What would you like? (espresso/latte/cappuccino): ').lower()
            # validate
            if response not in choice_key_list:
                print('Invalid choice. The valid choices are: espresso/latte/cappuccino.')
                continue
            break

        if response == 'off':
            coffee_maker_on = False
        elif response == 'report':
            myCoffeeMaker.report()
            myMoneyMachine.report()
        else:
            my_drink = myMenu.find_drink(response)
            if myCoffeeMaker.is_resource_sufficient(my_drink):                
                if myMoneyMachine.make_payment(my_drink.cost):
                    myCoffeeMaker.make_coffee(my_drink)
        
            

os.system('cls')
execute_coffee_maker()