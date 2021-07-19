"""
Homework 10

Check if a given year  is a leap year or not
"""
print("=======Start=======")

print("Test if a year is a leap year!")

year = int(input("Please enter a year: "))
a = ""
b = "{} is a leap year."
c = "{} is not a leap year."
a = b
#
if year % 4 == 0:
    a = b
    if year % 100 == 0:
        if year % 400 != 0:
            a = c
        else:
            a = b
    else:
        a = b
else:
    a = c

if a == b:
    print(b.format(year))
else:
    print(c.format(year))

print("========End========")