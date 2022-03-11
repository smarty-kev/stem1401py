"""

"""


class GrandParent:
    # not accessed in this case
    def __init__(self, name):
        print("GrandParent __init__() called.")
        self.name = name


class Son(GrandParent):
    def __init__(self):
        print("Son __init__() called.")


class GrandSon(Son):
    def __init__(self, age):
        print("GrandSon __init__() called.")
        super().__init__(age)


# main
gs1 = GrandSon(16)
print(gs1.age)
