"""

"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("sleep() is called")

    def eat(self):
        print("sleep() is called")
        print(self.name, "in eat()")

    def live(self):
        self.sleep()
        self.eat()


# main program
tom = Cat("Tom", 1)
tom.live()