"""
arguments

return value/expression
"""


def add(num1, num2):
    # num1 = 1
    # num2 = 2

    res = num1 + num2
    return res
    # print(res)


result = add(1,2)
print(f"the result is {result}")


# case 3. to return multiple values
def calc(num1, num2):
    sum = num1 + num2
    product = num1 * num2
    return sum, product


mysum, myproduct = calc(2,4)

print("The sum of {} and {} is {}.".format(1,2,mysum))
print("The product of {} and {} is {}.".format(1,2,myproduct))

