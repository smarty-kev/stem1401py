"""

"""


class Person:
    def __init__(self, name, initial_weight=75):
        self.name = name
        self.weight = initial_weight

    def __str__(self):
        return f"{self.name}'s weight is {self.weight}kg."

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


peter = Person("Peter")
peter.eat()
peter.run()
print(peter)
