"""
case 2. overriding properties and methods of parent class

Parent(name, talk())
Child(name, talk())

main program/app
"""


class Parent:
    def __init__(self, name):
        self.name = name+' at parent'

    def talk(self):
        print("parent talks")


class Child(Parent):
    def __init__(self, name):
        self.name = name+' at child'

    def talk(self):
        print("child talks")


child = Child("Roger")
print(child.name)
child.talk()
