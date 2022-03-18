"""
9.9.6 Super and inheritance
Case 2. Using super

Initialization with super
"""


class Parent:
    def __init__(self, name, *args, **kwargs):
        print('Parent.__init__() start invoking.')
        self.name = name
        print('Parent.__init__() invoked.')


class Son1(Parent):
    def __init__(self, name, age, *args, **kwargs):
        print('Son1.__init__() start invoking.')
        self.age = age
        # calling superclass' init method
        super().__init__(self, name, *args, **kwargs)
        print('Son1.__init__() invoked.\n')


class Son2(Parent):
    def __init__(self, name, gender, *args, **kwargs):
        print('Son2.__init__() start invoking.')
        self.gender = gender
        # calling superclass' init method
        super().__init__(self, name, *args, **kwargs)
        print('Son2.__init__() invoked.\n')


class GrandSon(Son1, Son2):
    def __init__(self, name, age, gender):
        print('GrandSon.__init__() start invoking.\n')
        # calling all superclass' init methods
        super().__init__(self, name, age, gender)
        print('GrandSon.__init__() invoked.\n')


# main
grandson1 = GrandSon('Peter', 16, 'Male')
print('Instance of GrandSon: grandson1 is created.')
print('Name:', grandson1.name)
print('Age:', grandson1.age)
print('Gender:', grandson1.gender)