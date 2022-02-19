"""
directly accessing properties and methods of parent class

Parent(name, talk())
Child

main program/app
"""


class Parent:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print("talk")


class Child(Parent):
    pass


child = Child("Roger")
print(child.name)
child.talk()
