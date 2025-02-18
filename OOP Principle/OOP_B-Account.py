class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number  # <-- Encapsulation of attributes
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount  # <-- Encapsulation of method
        return f"{amount} deposited. New balance is {self.balance}."

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount  # <--- Encapsulation of method
        return f"{amount} withdrawn. New balance is {self.balance}."

    def get_balance(self):
        return self.balance  # <--- Encapsulation of method


class SavingsAccount(BankAccount):  # <--- Inheritance from BankAccount
    def __init__(self, account_number, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_number, account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied. New balance is {self.balance}."


class CheckingAccount(BankAccount):  # <--- Inheritance from BankAccount
    def __init__(self, account_number, account_holder, balance=0, overdraft_limit=500):
        super().__init__(account_number, account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft_limit:
            return "Insufficient funds, even with overdraft"
        self.balance -= amount  # Polymorphism: overriding the method
        return f"{amount} withdrawn. New balance is {self.balance}."


# Creating objects
savings = SavingsAccount("123456789", "John Doe", 1000)
checking = CheckingAccount("987654321", "Jane Doe", 500)

# Using the methods
print(savings.deposit(500))  # Output: 500 deposited. New balance is 1500.
print(savings.apply_interest())  # Output: Interest applied. New balance is 1530.

print(checking.withdraw(1000))  # Output: 1000 withdrawn. New balance is -500.
print(checking.withdraw(600))  # Output: Insufficient funds, even with overdraft

"""Explanations:

Encapsulation is seen in how the attributes (account_number, account_holder, and balance) and methods (deposit, withdraw, and get_balance) are bundled within the BankAccount class.

Abstraction is applied by hiding the internal workings of deposit and withdrawal methods.

Inheritance is demonstrated by SavingsAccount and CheckingAccount classes inheriting from the BankAccount class.

Polymorphism is shown by overriding the withdraw method in the CheckingAccount class to account for overdraft limits."""