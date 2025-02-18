class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id  # Encapsulation of attributes
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity  # Encapsulation of method
        return f"Stock updated. New stock for {self.name}: {self.stock}"

    def get_price(self):
        return self.price  # Encapsulation of method

class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id  # Encapsulation of attributes
        self.products = products
        self.total = 0

    def calculate_total(self):
        # Abstraction of method to calculate order total
        self.total = sum(product.get_price() for product in self.products)
        return f"Total amount for order {self.order_id}: {self.total}"

class DigitalProduct(Product):  # Inheritance from Product
    def __init__(self, product_id, name, price, stock, file_size):
        super().__init__(product_id, name, price, stock)
        self.file_size = file_size

    def download(self):
        # Polymorphism: specific method for digital products
        return f"Downloading {self.name}. File size: {self.file_size}MB"

class PhysicalProduct(Product):  # Inheritance from Product
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.weight = weight

    def ship(self):
        # Polymorphism: specific method for physical products
        return f"Shipping {self.name}. Weight: {self.weight}kg"

# Creating objects
laptop = PhysicalProduct("P001", "Laptop", 1200, 50, 2.5)
e_book = DigitalProduct("D001", "E-Book", 15, 1000, 5)

# Creating an order
order = Order("O001", [laptop, e_book])

# Using the methods
print(laptop.update_stock(10))  # Output: Stock updated. New stock for Laptop: 60
print(e_book.download())  # Output: Downloading E-Book. File size: 5MB
print(order.calculate_total())  # Output: Total amount for order O001: 1215

"""Explanations:
Encapsulation is seen in how the attributes (product_id, name, price, and stock) and methods (update_stock, get_price) are bundled within the Product class.

Abstraction is applied in the calculate_total method of the Order class to hide the complex calculations.

Inheritance is demonstrated by DigitalProduct and PhysicalProduct classes deriving from the Product class.

Polymorphism is achieved through overriding methods like download in DigitalProduct and ship in PhysicalProduct, providing specific implementations for each product type.
"""
