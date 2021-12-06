"""
private member
private attribute
private method

"""


class Animal:
    def __init__(self, name):
        self._name = name
        self.age = 1

    def getName(self):
        return self._name

    def setName(self, new_name):
        # write private attribute
        self._name = new_name
        self._processName()

    def _processName(self):
        self._name = "My " + self._name
        print("inner "+self.getName())


# test
dog1 = Animal("Husky")
print(dog1.age)
# print(dog1.name)
print(dog1.getName())
dog1.setName("Peter")
print(dog1.getName())

# print(dog1._Animal__name)
