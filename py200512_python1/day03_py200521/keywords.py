"""
keywords
"""


"""
True, False, None
and, or, not
if, else, elif, for, while, break, continue
def, return, yield, lambda, pass
class,
try, except, raise, finally, with
global, nonlocal
import, from, as
assert, del, in, is
"""
# valid name (identifier)
# rule 1 a-z A-Z 0-9 _
car = 'BMW'
CAR = 'Benz'
_car = 'Dodge'
c001 = 123
a_123 = 345
_123 = 456

# rule 2 cannot start with a number
'''
0abc = 1
is error
'''
# rule 3 can be any length
this_is_a_long_variable_name = 123

# rule 4
# cannot use ; !@#$%^&*()-+={}|\

def foo(x):
    """
    this is a docstring for the function foo(x)
    :param x: 
    :return: 
    """
    print(x)
print(foo.__doc__)