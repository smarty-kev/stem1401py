"""
defining a class
adding attributes and methods
"""


class Cat:
    def __init__(self, name, color, size, age):
        self.name = name
        self.color = color
        self.size = size
        self.age = age

    def sleep(self):
        pass

    def meow(self):
        pass

    def run(self):
        pass


# main program
tom = Cat("tom", "gray", 15, 15)
print(tom)
