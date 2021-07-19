"""

function : lambda function
alias name : anonymous function

syntax:
lambda argument: expression

lambda [arg1, [arg2,...arg(n)]: expression]

high order function : a function that has a function in it
"""


#
def double(n):
    return 2*n


print(double(3))


# lambda expression
double = lambda n : 2*n

print(double(5))


db = lambda x : 2 * x
print(db(10))

