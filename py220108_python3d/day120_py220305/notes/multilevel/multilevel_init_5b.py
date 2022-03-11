"""

"""


class GrandParent:
    def __init__(self, name):
        print("GrandParent __init__() called.")
        self.name = name


class Son(GrandParent):
    def __init__(self, name, age):
        print("Son __init__() called.")
        self.age = age
        super().__init__(name)


class GrandSon(Son):
    def __init__(self, name, age, gender):
        print("GrandSon __init__() called.")
        self.gender = gender
        super().__init__(name, age)


# main
gs1 = GrandSon("Peter", 16, "Male")
print(f"age:{gs1.age}")
print(f"name:{gs1.name}")
print(f"gender:{gs1.gender}")
