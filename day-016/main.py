""" Coffee Maker Object Oriented Programming
"""
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":

    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    is_on = True
    while is_on:
        user_option = input(f"What would you like? {menu.get_items()}," +
                            "or type 'report' for report,"
                            "or 'off' to turn off the machine ")
        if user_option == "off":
            is_on = False
        elif user_option == "report":
            coffee_maker.report()
            money_machine.report()  # I actually forgot this the first time
        else:  # proceed with drink
            order = menu.find_drink(order_name=user_option)
            can_make = coffee_maker.is_resource_sufficient(order)
            if can_make:
                is_enough_money = money_machine.make_payment(order.cost)
                if is_enough_money:
                    coffee_maker.make_coffee(order=order)
