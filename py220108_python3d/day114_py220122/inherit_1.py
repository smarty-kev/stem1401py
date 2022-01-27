"""
single inheritance
"""


class Animal:
    def __init__(self):
        self.name = "animal"

    def run(self):
        print("animal runs.")


class Bird:
    pass


class Dog(Animal):
    def bark(self):
        print("dog barks.")


class Parrot(Bird):
    pass


dog1 = Dog()
print(dog1.name)
dog1.run()


a1 = Animal()
# a1.bark()  # AttributeError: 'Animal' object has no attribute 'bark'
