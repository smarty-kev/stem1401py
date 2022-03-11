"""

"""


class ParentA:
    def __init__(self, name):
        print("ParentA __init__() called.")
        self.name = name


class ParentB:
    def __init__(self):
        print("ParentB __init__() called.")


class Child(ParentA, ParentB):
    def __init__(self, gender):
        print("Child __init__() called.")
        self.gender = gender


# main
child1 = Child('Male')

print(child1.gender)
# print(child1.name)  # AttributeError: 'Child' object has no attribute 'name'
