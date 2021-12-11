"""
STEM 1403 Python Core III b
Final Exam - B
Kevin Liu
"""


# PART 1
"""
q1 D
q2 C
q3 D

q4  9
    10
    9
    11
    10

q5  [1, 2, 3]
    [9, 2, 3]
    [9, 2, 3]
    [99, 2, 3]

q6 C
q7 D
q8 B
q9 C
q10 C
q11 B
q12 A
q13 B
q14 B
q15 B
"""

# q16
class PC:
    def __init__(self, cpu, ram, storage, wifi, ethernet, graphics):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.wifi = wifi
        self.ethernet = ethernet
        self.graphics = graphics
        self.state = False

    def turn_on(self):
        self.state = True

    def turn_off(self):
        self.state = False

    def run_programs(self):
        pass

    def connect_to_wifi(self):
        pass


cpu = "INTEL i7"
ram = "2 x 8GB DDR3"
storage = "1TB SSD"
wifi = "built-in WiFI module"
ethernet = "ethernet network interface"
graphics = "GeForce RTX 3090"
peter_PC = PC(cpu, ram, storage, wifi, ethernet, graphics)


"""
q17 Peter
    Jack
q18 A
q19 D
q20 C
q21 B
"""


# q22
class Cat:
    def __init__(self, name="Peter"):
        self.name = name
        self.age = 1

    def __str__(self):
        objinfo = self.__class__.__name__ + "[" + "self.name = " + self.name + ", self.age = " + str(self.age) + "]"
        # return "__str__() is called"
        return objinfo


print(Cat())

"""
q23 B
q24 E
"""


# q25
class Cat:
    def __init__(self, name="Peter"):
        self._name = name
        self._age = 1
