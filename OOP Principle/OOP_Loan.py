class Loan:
    def __init__(self, loan_id, borrower, principal, interest_rate, term):
        self.loan_id = loan_id  # Encapsulation of attributes
        self.borrower = borrower
        self.principal = principal
        self.interest_rate = interest_rate
        self.term = term

    def calculate_interest(self):
        # Abstraction of method to calculate interest
        return self.principal * self.interest_rate * self.term / 100


class HomeLoan(Loan):  # Inheritance from Loan class
    def __init__(self, loan_id, borrower, principal, interest_rate, term, property_value):
        super().__init__(loan_id, borrower, principal, interest_rate, term)
        self.property_value = property_value

    def calculate_interest(self):
        # Polymorphism: specific implementation for HomeLoan
        return (self.principal * self.interest_rate * self.term / 100) * 0.95  # Discounted rate for home loan


class CarLoan(Loan):  # Inheritance from Loan class
    def __init__(self, loan_id, borrower, principal, interest_rate, term, car_model):
        super().__init__(loan_id, borrower, principal, interest_rate, term)
        self.car_model = car_model

    def calculate_interest(self):
        # Polymorphism: specific implementation for CarLoan
        return (self.principal * self.interest_rate * self.term / 100) * 1.05  # Slightly higher rate for car loan


# Creating objects
home_loan = HomeLoan("HL001", "Alice Smith", 300000, 3.5, 30, 350000)
car_loan = CarLoan("CL001", "Bob Johnson", 20000, 5, 5, "Toyota Camry")

# Using the methods
print(f"Home Loan Interest: {home_loan.calculate_interest()}")  # Output: Home Loan Interest: 99750.0
print(f"Car Loan Interest: {car_loan.calculate_interest()}")  # Output: Car Loan Interest: 5250.0

"""Explanations:
Encapsulation is demonstrated by bundling the attributes (loan_id, borrower, principal, interest_rate, and term) and methods (calculate_interest) within the Loan class.

Abstraction is used in the calculate_interest method to hide the complex calculations.

Inheritance is shown by HomeLoan and CarLoan classes deriving from the Loan class.

Polymorphism is achieved by overriding the calculate_interest method in HomeLoan and CarLoan to provide specific implementations for each loan type."""