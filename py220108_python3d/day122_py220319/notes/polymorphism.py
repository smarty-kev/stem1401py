"""

"""


class Pet:
    def eat(self):
        print("A pet eats food")


class Cat(Pet):
    def eat(self):
        print("Cat eats fish")


class Dog(Pet):
    def eat(self):
        print("Dog eats meat")


class Person:
    def __init__(self, name):
        self.name = name

    def feed(self, pet):
        pet.eat()


peter = Person("Peter")

cat = Cat()

dog = Dog()

pet = Pet()

peter.feed(cat)
peter.feed(dog)
peter.feed(pet)
