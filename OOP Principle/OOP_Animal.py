class Animal:
    def __init__(self, name, species):
        self.name = name  # <--- Encapsulation of attributes
        self.species = species

    def make_sound(self):
        pass  # <--- Abstraction of method

class Dog(Animal):  # <---Inheritance from the Animal class
    def make_sound(self):
        return "Bark!"  # <---Polymorphism allows different behavior for different objects


class Cat(Animal):  # <---Another class inheriting from Animal
    def make_sound(self):
        return "Meow!"  # <---Polymorphism


# Creating objects
dog = Dog("Buddy", "Dog")
cat = Cat("Whiskers", "Cat")

# Using polymorphism to call the same method on different objects
print(dog.name + " says " + dog.make_sound())  # Output: Buddy says Bark!
print(cat.name + " says " + cat.make_sound())

"""Explanations:

Encapsulation is seen in how the name and species attributes are bundled within the Animal class.

Abstraction is used in the make_sound method, which hides the implementation details.

Inheritance is demonstrated with Dog and Cat classes deriving from the Animal class.

Polymorphism allows the make_sound method to be called on different objects (a dog and a cat), producing different outputs."""