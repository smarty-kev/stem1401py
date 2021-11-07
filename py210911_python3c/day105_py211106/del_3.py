# Definition
class MyClass:
# Initialization
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a+self.b
obj = Add(3,4)
# Access
print(obj.add())
# Garbage collection