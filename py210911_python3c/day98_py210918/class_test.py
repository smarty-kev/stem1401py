"""

"""


class MyClass:
    def __init__(self):
        pass
    x = 1


v1 = MyClass()
print(v1.x)
print("====\n")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print("====\n")


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is {} and I am {} years old.".format(self.name, self.age))

p1 = Person("John", 36)
p1.myfunc()
print("====\n")


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)


p1 = Person("John", 36)
p1.myfunc()
