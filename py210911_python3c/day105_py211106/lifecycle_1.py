"""
print out object information
"""

# defining a class
class WildCat:

    # def __new__(cls, *args, **kwargs):
    #     pass

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # self.color does not exist.

    def sleep(self):
        print('sleep() is called')

    def eat(self):
        print('eat() is called')
        print(self.name, 'in eat()')    # accessing attributes


    def __str__(self):
        # print('__str__() is called')
        # TypeError: __str__ returned non-string (type NoneType)
        objinfo = self.__class__.__name__+"["\
                  +"name='"+self.name+"'" \
                  + ",age="+str(self.age) \
                  +"]"
        # return '__str__() is called new'
        return objinfo

#
tom = WildCat("Tom",1)

# print info.
print(tom.name)
print(tom.age)

print(tom)

tom.name = "Tommy"
print(tom)

tom.age = 2
print(tom)

tom.eat()


def myfunc():
    pass