"""

"""


class Person:
    def __init__(self, name, initial_weight):
        self.name = name
        self.weight = initial_weight

    def __str__(self):
        return f"{self.name}'s weight is {self.weight}kg."

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 1


peter = Person("Peter", 75)
amy = Person("Amy", 45)

for p in range(2):
    peter.eat()
    amy.eat()
    print("\nBoth ate.")

    print(peter)
    print(amy)

    peter.run()
    amy.run()
    print("\nBoth ran.")

    print(peter)
    print(amy)
