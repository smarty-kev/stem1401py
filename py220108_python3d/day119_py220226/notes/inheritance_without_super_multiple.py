"""
9.10.1 Super and inheritance
Case 1. Without using super

Initialization without super
subclass inherits properties from multiple superclasses

child has its own property: gender
child inherits property of ParentA: name
child inherits property of ParentB: age

ParentA has a property: name
ParentB has a property: age
"""


class ParentA:
    def __init__(self, name):
        print('ParentA __init__() called.')
        self.name = name +' at ParentA'


class ParentB:
    def __init__(self, age):
        print('ParentB __init__() called.')
        self.age = str(age) + ' at ParentB'


class Child(ParentA, ParentB):
    def __init__(self, name, age):
        print('Child __init__() called.')
        ParentA.__init__(self, name)
        ParentB.__init__(self, age)


# main
child1 = Child('Peter',16)
print(child1.name)
print(child1.age)
