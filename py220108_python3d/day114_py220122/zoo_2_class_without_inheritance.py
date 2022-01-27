"""
OOP - inheritance
Animals

v2. Parent class only
"""


class Animal:
    def eat(self):
        print("Animal eats.")

    def drink(self):
        print("Animal drinks.")

    def run(self):
        print("Animal runs.")

    def sleep(self):
        print("Animal sleeps.")


class Dog:
    def eat(self):
        print("Animal eats.")

    def drink(self):
        print("Animal drinks.")

    def run(self):
        print("Animal runs.")

    def sleep(self):
        print("Animal sleeps.")

    # exclusive
    def bark(self):
        print("wouf wouf")


# main program
creature1 = Dog()

creature1.eat()
creature1.drink()
creature1.run()
creature1.sleep()
creature1.bark()
