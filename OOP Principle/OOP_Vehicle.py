class Vehicle:
    def __init__(self, make, model, year):
        self.make = make  # <--- Encapsulation of attributes
        self.model = model
        self.year = year

    def start_engine(self):
        pass  # <-- Abstraction of method


class Car(Vehicle):  # <--- Inheritance from the Vehicle class
    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} car is now running."  # Polymorphism


class Motorcycle(Vehicle):  # <--- Another class inheriting from Vehicle
    def start_engine(self):
        return f"The engine of the {self.year} {self.make} {self.model} motorcycle is now running."  # Polymorphism


# Creating objects
car = Car("Toyota", "Corolla", 2020)
motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2019)

# Using polymorphism to call the same method on different objects
print(car.start_engine())  # Output: The engine of the 2020 Toyota Corolla car is now running.
print(motorcycle.start_engine())  # Output: The engine of the 2019 Harley-Davidson Sportster motorcycle is now running.
