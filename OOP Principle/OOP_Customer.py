class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id  # Encapsulation of attributes
        self.name = name
        self.email = email

    def update_email(self, new_email):
        self.email = new_email  # Encapsulation of method
        return f"Email updated for {self.name}. New email: {self.email}"

class Order:
    def __init__(self, order_id, customer, products):
        self.order_id = order_id  # Encapsulation of attributes
        self.customer = customer
        self.products = products
        self.total = 0

    def calculate_total(self):
        # Abstraction of method to calculate order total
        self.total = sum(product.get_price() for product in self.products)
        return f"Total amount for order {self.order_id}: {self.total}"

class Product:
    def __init__(self, product_id, name, price):
        self.product_id = product_id  # Encapsulation of attributes
        self.name = name
        self.price = price

    def get_price(self):
        return self.price  # Encapsulation of method

class DiscountProduct(Product):  # Inheritance from Product
    def __init__(self, product_id, name, price, discount_rate):
        super().__init__(product_id, name, price)
        self.discount_rate = discount_rate

    def get_price(self):
        # Polymorphism: specific implementation for discounted products
        return self.price * (1 - self.discount_rate)

class PremiumProduct(Product):  # Inheritance from Product
    def __init__(self, product_id, name, price, premium_fee):
        super().__init__(product_id, name, price)
        self.premium_fee = premium_fee

    def get_price(self):
        # Polymorphism: specific implementation for premium products
        return self.price + self.premium_fee

# Creating objects
customer = Customer("C001", "John Doe", "john@example.com")
laptop = PremiumProduct("P001", "Laptop", 1200, 200)
e_book = DiscountProduct("D001", "E-Book", 20, 0.1)

# Creating an order
order = Order("O001", customer, [laptop, e_book])

# Using the methods
print(customer.update_email("john.doe@example.com"))  # Output: Email updated for John Doe. New email: john.doe@example.com
print(order.calculate_total())  # Output: Total amount for order O001: 1340.0

"""Explanations:
Encapsulation is demonstrated by bundling the attributes (customer_id, name, email, order_id, products, product_id, name, price) and methods (update_email, calculate_total, get_price) within their respective classes.

Abstraction is applied in the calculate_total method of the Order class to hide the complex calculations.

Inheritance is shown by DiscountProduct and PremiumProduct classes deriving from the Product class.

Polymorphism is achieved through overriding the get_price method in DiscountProduct and PremiumProduct, providing specific implementations for each product type.
"""