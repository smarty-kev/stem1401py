"""
case 3. accessing methods of parent class

Parent(name, talk())
Child(name, talk())

main program/app
"""


class Parent:
    def __init__(self, name):
        self.name = name+' at parent'

    def talk(self):
        print("parent talks")

    def talk3(self):
        self.talk()


class Child(Parent):
    # def __init__(self, name):
    #     self.name = name+' at child'

    def talk(self):
        super().talk()
        print("child talks")

    def talk2(self):
        super().talk()


child = Child("Roger")
print(child.name)
child.talk()
child.talk2()
