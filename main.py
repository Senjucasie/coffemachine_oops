from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu=Menu()
cash=MoneyMachine()
coffee=CoffeeMaker()
_ison=True
while(_ison):
    print("adad")
    choice=input("What would you like? "+menu.get_items())
    if(choice=="off"):
        _ison=False
    elif(choice=="report"):
        coffee.report()
    else:
        drink=menu.find_drink(choice)
        if(coffee.is_resource_sufficient(drink) and cash.make_payment(drink.cost)):
            coffee.make_coffee(drink)






