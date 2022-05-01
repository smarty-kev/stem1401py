"""
class member: class method
"""


class Foo:
    attr1 = 123

    @classmethod
    def getAttr1(cls):
        return Foo.attr1

    @classmethod
    def setAttr1(cls, value):
        cls.attr1 = value


# main
# read
print(Foo.getAttr1())


# write
Foo.setAttr1(999)
# read
print(Foo.getAttr1())

