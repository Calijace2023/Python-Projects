class Item:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id  # Encapsulation of attributes
        self.name = name
        self.price = price
        self.quantity = quantity

    def update_quantity(self, amount):
        self.quantity += amount  # Encapsulation of method
        return f"Quantity updated. New quantity for {self.name}: {self.quantity}"

    def get_total_price(self):
        return self.price * self.quantity  # Encapsulation of method

class PerishableItem(Item):  # Inheritance from Item class
    def __init__(self, item_id, name, price, quantity, expiration_date):
        super().__init__(item_id, name, price, quantity)
        self.expiration_date = expiration_date

    def check_expiration(self, current_date):
        # Polymorphism: specific method for perishable items
        if current_date > self.expiration_date:
            return f"{self.name} has expired."
        else:
            return f"{self.name} is still good until {self.expiration_date}."

class NonPerishableItem(Item):  # Inheritance from Item class
    def __init__(self, item_id, name, price, quantity, warranty_period):
        super().__init__(item_id, name, price, quantity)
        self.warranty_period = warranty_period

    def get_warranty_info(self):
        # Polymorphism: specific method for non-perishable items
        return f"{self.name} comes with a warranty period of {self.warranty_period} months."

# Creating objects
milk = PerishableItem("P001", "Milk", 2.5, 20, "2025-02-28")
laptop = NonPerishableItem("N001", "Laptop", 1200, 10, 24)

# Using the methods
print(milk.update_quantity(10))  # Output: Quantity updated. New quantity for Milk: 30
print(milk.check_expiration("2025-03-01"))  # Output: Milk has expired.

print(laptop.update_quantity(5))  # Output: Quantity updated. New quantity for Laptop: 15
print(laptop.get_warranty_info())  # Output: Laptop comes with a warranty period of 24 months.

"""Explanations:
Encapsulation is demonstrated by bundling the attributes (item_id, name, price, quantity) and methods (update_quantity, get_total_price) within the Item class.

Abstraction is applied in the methods to hide the complex calculations and logic.

Inheritance is shown by PerishableItem and NonPerishableItem classes deriving from the Item class.

Polymorphism is achieved through overriding methods like check_expiration in PerishableItem and get_warranty_info in NonPerishableItem, providing specific implementations for each item type.
"""