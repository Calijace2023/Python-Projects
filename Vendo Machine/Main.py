from Resouce_Data import resources, Coffee_Menu
from Function_Library import is_resources_sufficient, process_coins, make_coffee
from prettytable import PrettyTable


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

# 1. Prompt User by asking "What would you like? (espresso/latte/cappuccino:"
is_on = True
profit = 0
while is_on:

    option = input("What would you like? (espresso/latte/cappuccino:)")
    # 2. Turn off Coffe M/C by entering "off" to the prompt.
    if option == "off":
        is_on = False
        print("machine is turning off")

    # 3. Print report
    elif option == "report":
        table = PrettyTable()
        table.add_column("Raw Materials", ["Water", "Milk", "Coffee","Money"])
        table.add_column("Ingredients", [resources["water"], resources["milk"], resources["coffee"], profit])
        table.add_column("Units", ["ml", "ml", "g", "$"])
        print(table)

    # 4. Check resources sufficient?
    else:
        drink = Coffee_Menu[option]
        if is_resources_sufficient(drink["ingredients"]):
            # 5. Process Coins.
            payment = process_coins()

            # 6. Check transaction successful?

            if is_transaction_successful(payment, drink["cost"]):
                # 7. Make Coffee
                make_coffee(option, drink["ingredients"])
