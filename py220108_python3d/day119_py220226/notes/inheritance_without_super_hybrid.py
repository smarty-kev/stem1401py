"""
9.9.6 Super and inheritance
Case 1. Without using super

Initialization without super
"""


class Parent:
    def __init__(self, name):
        print('Parent.__init__() start invoking.')
        self.name = name
        print('Parent.__init__() invoked.')


class Son1(Parent):
    def __init__(self, name, age):
        print('Son1.__init__() start invoking.')
        self.age = age
        # calling superclass' init method
        Parent.__init__(self, name)
        print('Son1.__init__() invoked.\n')


class Son2(Parent):
    def __init__(self, name, gender):
        print('Son2.__init__() start invoking.')
        self.gender = gender
        # calling superclass' init method
        Parent.__init__(self, name)
        print('Son2.__init__() invoked.\n')


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print('GrandSon.__init__() start invoking.\n')
        # calling all superclass' init methods
        Son1.__init__(self, name, age)
        Son2.__init__(self, name, gender)
        print('GrandSon.__init__() invoked.\n')


# main
grandson1 = GrandSon('Peter', 16, 'Male')
print('Instance of GrandSon: grandson1 is created.')
print('Name:', grandson1.name)
print('Age:', grandson1.age)
print('Gender:', grandson1.gender)
