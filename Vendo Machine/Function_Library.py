from Resouce_Data import resources

def is_resources_sufficient(order_ingredients):
    """Return True when order can be made, False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        return True

def process_coins():
    """Return the total calculated  from coins inserted"""
    print("Please insert coins")
    total = int(input("how many quarters?"))*0.25
    total += int(input("how many dimes?")) * 0.1
    total += int(input("how many nickles?")) * 0.05
    total += int(input("how many pennies?")) * 0.01
    return total

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
        print(f"Here is your {drink_name} ☕. Enjoy!!")
        return True


