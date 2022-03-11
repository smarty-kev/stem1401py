"""

"""


class ParentA:
    def __init__(self, name):
        print("ParentA __init__() called.")
        # self.name = name + " at ParentB"


class ParentB:
    def __init__(self, name):
        # not accessed under MRO
        print("ParentB __init__() called.")
        self.name = name + " at ParentB"


class Child(ParentA, ParentB):
    def __init__(self, gender, name):
        print("Child __init__() called.")
        self.gender = gender
        super().__init__(name)


# main
child1 = Child('Male', "Peter")

print(child1.gender)
print(child1.name)  # AttributeError: 'Child' object has no attribute 'name'
