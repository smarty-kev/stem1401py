"""

"""


class Pet:
    def __init__(self, petClass="pet"):
        self.petClass = petClass

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
        print(f"{self.name} feeds his {pet.petClass}")
        pet.eat()
        print(type(pet))


peter = Person("Peter")
cat = Cat("cat")
dog = Dog("dog")
pet = Pet()

peter.feed(cat)
peter.feed(dog)
peter.feed(pet)
