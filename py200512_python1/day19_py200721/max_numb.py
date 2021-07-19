"""
to find the largest number among three given number
"""

a = float(input("Please enter a number: "))
b = float(input("Please enter a number: "))
c = float(input("Please enter a number: "))

"""
if a > b:
    if a > c:
        print("{} is the biggest number.".format(a))
elif b > c:
    if b > a:
        print("{} is the biggest number.".format(b))
else:
    print("{} is the biggest number.".format(c))
"""

max = a
if a >= max:
    max = a

if b >= max:
    max = b

if c >= max:
    max = c

print(max)
