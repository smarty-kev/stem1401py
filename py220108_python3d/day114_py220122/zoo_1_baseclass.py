"""
OOP - inheritance
Animals

v1. Parent class only
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


# main program
creature1 = Animal()

creature1.eat()
creature1.drink()
creature1.run()
creature1.sleep()
