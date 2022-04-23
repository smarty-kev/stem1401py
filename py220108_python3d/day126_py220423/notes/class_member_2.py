"""
class member 2
"""


class Foo:
    attr1 = 123

    # def method1(self):
    #     pass

    def __init__(self):
        self.attr2 = 1234

    def method2(self):
        pass


obj1 = Foo()
print(obj1.attr2)
