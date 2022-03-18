"""

"""


class ParentA:
    def __init__(self, age, *args):
        print("ParentA __init__() called.")
        self.age = str(age) + ' at ParentA'

        super().__init__(*args)


class ParentB:
    def __init__(self, name, *args):
        # not accessed under MRO
        print("ParentB __init__() called.")
        self.name = name + " at ParentB"


class Child(ParentA, ParentB):
    def __init__(self, gender, name, age):
        print("Child __init__() called.")
        self.gender = gender

        # ParentA has no attribute: name
        super().__init__(age, name)


# main
child1 = Child("Gender: Male", "Name: Peter", 16)
print(child1.gender)
print(child1.name)
print(child1.age)
