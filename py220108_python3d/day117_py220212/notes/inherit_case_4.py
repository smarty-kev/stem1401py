"""
case 4. forcefully accessing private properties and methods of parent class

Parent(name, talk())
Child(name, talk())

main program/app
"""


class Parent:
    def __init__(self, name):
        self.__name = name+' at parent'

    def __talk(self):
        print("parent talks")


class Child(Parent):
    def talk(self):
        super()._Parent__talk()


child = Child("Roger")
print(child._Parent__name)
child.talk()
