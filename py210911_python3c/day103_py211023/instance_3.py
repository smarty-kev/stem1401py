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
        print("sleep() is called")


# main program
tom = Cat("Tom", 1)
jerry = Cat("Jerry", 3)
pablo = Cat("Pablo", 4)

print(id(tom))
print(id(jerry))
print(id(pablo))

# 4312634032
# 4312410384
# 4312411920

print("=====")

tomma = tom

print(id(tomma))  # 4375032496
print(id(tom))  # 4375032496
