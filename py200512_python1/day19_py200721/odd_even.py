"""
to check if a given number is an odd or even number
"""

n = int(input("Please enter an integer: "))

if n % 2 == 0:
    print("{} is an even number.".format(n))
elif n % 2 != 0:
    print("{} is an odd number.".format(n))