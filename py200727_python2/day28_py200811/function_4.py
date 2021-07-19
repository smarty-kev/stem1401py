"""
docstring in function
"""

# docstring in function without argument
def foo():
    """
    the description of this function
    :return:
    """
    print("Yes, we entered the function foo()")


# to call function
foo()
print("Goodbye!")


# docstring in function with arguments
def add(num1, num2):
    """
    the description of the function add()
    :param num1:
    :param num2:
    :return:
    """
    res = num1 + num2
    print(res)


add(1,2)


print(foo.__doc__)
print(add.__doc__)

