"""
Adding an attribute to an object
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("sleep() is called")

    def eat(self):
        print("sleep() is called")


# main program
tom = Cat("Tom", 2)
# print(tom.color) AttributeError: 'Cat' object has no attribute 'color'

tom.color = "Orange"
print(tom.color)

peter = Cat("Peter", 1)
# print(peter.color) AttributeError: 'Cat' object has no attribute 'color'
