"""
instance and or object of a class
"""


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("sleep() is called")

    def eat(self):
        print("eat"
              "() is called")


# main program
tom = Cat("Tom", 1)


# accessing instance attributes
name = tom.name
age = tom.age
print(name)
print(age)

tom.sleep()
tom.eat()
