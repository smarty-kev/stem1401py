"""
private member
private attribute
private method

"""


class Animal:
    def __init__(self, name):
        self._name = name
        self.age = 1

    def get_name(self):
        return self._name

    def set_name(self, new_name):
        # write private attribute
        self._name = new_name


# test
dog1 = Animal("Husky")
print(dog1.age)
# print(dog1.name)
print(dog1.get_name())
dog1.set_name("Peter")
print(dog1.get_name())
