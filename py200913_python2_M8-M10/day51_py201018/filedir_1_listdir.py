"""
list dir(s)

list dir()
"""

import os

# current path
path = "."
result = os.listdir(path)

# print(type(result))

for i in result:
    print(i)
print()
print()

# subdir path
try:
    path = ".\\sample"
    result = os.listdir(path)

    for i in result:
        print(i)
    print()
    print()
except FileNotFoundError as fe:
    print(fe)
except Exception as e:
    print(e)

# relative path
path = ".."
result = os.listdir(path)

for i in result:
    print(i)
print()
print()

# using absolute path
path = r"/Users/jenn/PycharmProjects/stem1401py/py200913_python2_M8-M10"
result = os.listdir(path)

for i in result:
    print(i)
