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

    def __str__(self):
        objinfo = self.__class__.__name__+"["+"self.name = " + self.name + ", self.age = " + str(self.age)+"]"
        # return "__str__() is called"
        return objinfo


tom = Cat("Tom", 1)
print(tom.name)
print(tom.age)

print(tom)
