"""
class method

@classmethod
"""


class Tool:
    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1
        # self.__class__.count += 1
        # cls.count += 1

    @classmethod
    def getToolCount(cls):
        return cls.count

    @classmethod
    def printToolCount(cls):
        print(cls.getToolCount())


# test
print(Tool.getToolCount())

tool1 = Tool("Hammer")
Tool.printToolCount()
