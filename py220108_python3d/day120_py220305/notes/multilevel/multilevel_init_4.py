"""

"""


class GrandParent:
    # not accessed in this case
    def __init__(self, name):
        print("GrandParent __init__() called.")
        self.name = name


class Son(GrandParent):
    # def __init__(self):
    #     print("Son __init__() called.")
    pass


class GrandSon(Son):
    def __init__(self, name):
        print("GrandSon __init__() called.")
        super().__init__(name)


# main
gs1 = GrandSon("Peter")
print(gs1.name)
