"""
why we need function

1. remove reduncdanct statement
"""

# case 1.

# paragraph
def printtext():
    print("sequence 1")
    print("sequence 2")
    print("sequence 3")
    print("sequence 4")


# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()
# printtext()

for i in range(127):
    printtext()
print()

# case 2


def add(num1, num2):
    # num1 = 1
    # num2 = 2

    res = num1 + num2
    print(res)


add(1,2)
