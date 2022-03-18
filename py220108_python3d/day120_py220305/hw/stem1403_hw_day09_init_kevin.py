"""
[Homework]
Date: 2022-03-05
Due date: 2022-03-11
1. Rewrite codes for initialization in all cases of inheritance.
Hints:
One case per python file
Do not submit them to SLACK.
Keep them on your computer.
2. Write a summary of all cases of initialization
Example,
case 1. title and description
case 2. title and description
case 3. title and description
Hints:
Write everything within a comment in your python file.
"""


# SINGLE INHERITANCE

"""
Parent
Child(Parent)
"""

# case 1 single_init_1
"""
child class inherits the __init__() method of the parent class
the parent class has NO parameter

!!!
# important points:
not much
"""

# case 2 single_init_1b
"""
child class inherits the __init__() method of the parent class
the parent class has ONE parameter

!!!
# important points:
not much
"""

# case 3single_init_2
"""
child class overrides the __init__() method of the parent class with it's own __init__() method
the parent class has NO parameter
the child class has NO parameter

!!!
# important points:
parent's __init__() method is not accessed when initiating child class
"""

# case 4 single_init_2b
"""
child class overrides the __init__() method of the parent class with it's own __init__() method
the parent class has NO parameter
the child class has ONE parameter

!!!
# important points:
not much
"""

# case 5 single_init_2c
"""
child class overrides the __init__() method of the parent class with it's own __init__() method
the parent class has ONE parameter ("name")
the child class has ONE parameter  ("age")

!!!
# important points:
c1 = Child(age)
c1 has no attribute name
because parent's __init__() is not accessed
"""

# case 6 single_init_2d
"""
child class overrides the __init__() method of the parent class with it's own __init__() method
the parent class has ONE parameter ("name")
the child class has TWO parameter  ("age", "name")

!!!
# important points:
c1 = Child(age, name)
parent's __init__() method is still not accessed
"""

# case 7 single_init_2e
"""
child class overrides the __init__() method of the parent class with it's own __init__() method
the parent class has ONE parameter ("name")
the child class has TWO parameter  ("age", "name")
inside child class:
super().__init__(name)
# call to parent class' __init__()

!!!
# important points:
parent's __init__() method is accessed with the super().__init__() method
"""


# MULTILEVEL INHERITANCE

"""
Grandparent
Son(Grandparent)
Grandson(Son)
"""

# case 1 multilevel_init_1
"""
grandparent class has it's own __init__() method

!!!
# important points:
not much
"""

# case 2 multilevel_init_2
"""
grandparent class has it's own __init__() method
son class has it's own __init__() method

!!!
# important points:
grandparent's __init__() method is NOT accessed because the grandson class stops when he sees son's __init__() method
"""

# case 3 multilevel_init_3
"""
grandparent class has it's own __init__() method
son class has it's own __init__() method
grandson class has it's own __init__() method

!!!
# important points:
grandson class overrides all other __init__()
"""

# case 4 multilevel_init_4
"""
grandparent class has it's own __init__() method
grandson class has it's own __init__() method

inside grandson class:
super().__init__(name)
# calls to grandparent's __init__() method

grandparent class has ONE parameter ("name")
grandson class has ONE parameter    ("name")

!!!
# important points:
grandson class calls grandparent's __init__() with one parameter ("name")
"""

# case 5 multilevel_init_4b
"""
grandparent class has it's own __init__() method
son class has it's own __init__() method
grandson class has it's own __init__() method

inside grandson class:
super().__init__(name)
# calls to son's __init__() method

grandparent class has ONE parameter ("name")
grandson class has ONE parameter    ("age")

!!!
# important points:
this program does not work because the __init__() method in son class does not take any parameter
"""

# case 6 multilevel_init_4c
"""
grandparent class has it's own __init__() method
son class has it's own __init__() method
grandson class has it's own __init__() method

inside grandson class:
super().__init__(name)
# calls to son's __init__() method

grandparent class has ONE parameter ("name")
son class has ONE parameter         ("age")
grandson class has ONE parameter    ("age")

!!!
# important points:
grandparent's __init__() is not accessed
"""

# case 7 multilevel_init_5
"""
grandparent class has it's own __init__() method
son class has it's own __init__() method
grandson class has it's own __init__() method

inside son class:
super().__init__(name)
# calls to grandparent's __init__() method

inside grandson class:
super().__init__(name, age)
# calls to son's __init__() method

grandparent class has ONE parameter ("name")
son class has TWO parameter         ("name", "age")
grandson class has TWO parameter    ("name", "age")

!!!
# important points:
grandson's __init__() calls son's __init__() which also calls grandparent's __init__()
"""

# case 8 multilevel_init_5b
"""
grandparent class has it's own __init__() method
son class has it's own __init__() method
grandson class has it's own __init__() method

inside son class:
super().__init__(name, age)
# calls to grandparent's __init__() method

inside grandson class:
super().__init__(name, age)
# calls to son's __init__() method

grandparent class has ONE parameter ("name")
son class has TWO parameter         ("name", "age")
grandson class has THREE parameter    ("name", "age", "gender")

!!!
# important points:
grandson has three parameters for it's __init__() method
gender is defined at grandson
age is defined at son
name is defined at grandparent
"""


# MULTIPLE INHERITANCE

"""
ParentA
ParentB
Child(A, B)
"""

# case 1 multiple_init_1
"""
ParentA has it's own __init__() method
ParentB has it's own __init__() method
Child inherits ParentA's __init__()

!!!
# important points:
ParentB's __init__() method is not accessed (rules of MRO)
"""

# case 2 multiple_init_2
"""
ParentA has it's own __init__() method
ParentB has it's own __init__() method
Child   has it's own __init__() method

!!!
# important points:
Child overrides all other __init__() methods with it's own __init__()
"""

# case 3 multiple_init_3
"""
ParentA has it's own __init__() method
ParentB has it's own __init__() method
Child   has it's own __init__() method

ParentA class has ONE parameter ("name")
Child class has ONE parameter   ("gender")

!!!
# important points:
Child overrides all other __init__() methods with it's own __init__()
c1 = Child(age)
c1 has not attribute 'name' since ParentA's __init__() method is not accessed
"""

# case 4 multiple_init_3b
"""
ParentA has it's own __init__() method
ParentB has it's own __init__() method
Child   has it's own __init__() method

ParentA class has ONE parameter ("name")
Child class has TWO parameter   ("gender", "name")

!!!
# important points:
Child overrides all other __init__() methods with it's own __init__()
c1 = Child(gender, name)
c1 has attribute 'name' BUT ParentA's __init__() method is not accessed
"""

# case 5 multiple_init_3c
"""
ParentA has it's own __init__() method
ParentB has it's own __init__() method
Child   has it's own __init__() method

inside Child class:
super().__init__(name)

ParentA class has ONE parameter ("name")
Child class has TWO parameter   ("gender", "name")

!!!
# important points:
Child calls ParentA's __init__() method with the super().__init__() method
c1 = Child(gender, name)
c1 has attribute 'name' AND ParentA's __init__() method IS accessed
"""

# case 6 multiple_init_3d
"""
ParentA has it's own __init__() method
ParentB has it's own __init__() method
Child   has it's own __init__() method

inside Child class:
super().__init__(name)


ParentA class has ONE parameter ("name")
BUT the parameter "name" is not used inside the __init__():
    def __init__(self, name):
        print("ParentA __init__() called.")

ParentB class has ONE parameter ("name")
Child class has TWO parameter   ("gender", "name")

!!!
# important points:
Child calls ParentA's __init__() method with the super().__init__() method
c1 = Child(gender, name)
c1 has no attribute 'name'
ParentA's __init__() method IS accessed under MRO rule
but it is not defined
even though it is defined in ParentB, because of MRO, ParentB's __init__() method is NOT accessed
"""
