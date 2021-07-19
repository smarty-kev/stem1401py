"""
dir() - is a built in function
"""

import py200727_python2.day33_py200824.myfunc as myfunc

print(dir(myfunc))

for i in dir(myfunc):
    print(i)

print(myfunc.__doc__)


import math


for i in dir(math):
    print(i)