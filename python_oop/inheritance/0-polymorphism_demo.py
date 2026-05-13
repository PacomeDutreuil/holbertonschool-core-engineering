#!/usr/bin/env python3

class Animal:
    def speak(self):
        return "Some sound"


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


# Create objects
dog = Dog()
cat = Cat()

print(dog.speak())
print(cat.speak())


# Demonstrate polymorphism
animals = [Dog(), Cat(), Dog()]

for animal in animals:
    print(animal.speak())


# Check class relationships
print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
