"""
class member 4
writing class attributes
"""


class Foo:
    # class attribute
    # shared among instances
    attr1 = 123

    def __init__(self):
        # instance attribute
        self.attr2 = 234

    def method2(self):
        pass


# write 1
Foo.attr1 = 999
print(Foo.attr1)

# read 2 - not recommended
obj1 = Foo()
print(obj1.attr1)

# read 3
print(obj1.__class__.attr1)
