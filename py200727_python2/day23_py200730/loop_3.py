"""
please convert for loop into while loop
1+2+3+4+5..+10
1+2+3  +5..+10
"""

a = 0
for i in range(1,11,):
    a = a + i
print("The answer is {}.".format(a))


sum = 0
i = 1
while i <= 10:
    sum = sum + i
    i += 1

print("The answer is {}.".format(sum))


sum = 0
i = 1
while i <= 10 and i != 4:
    sum = sum + i
    i += 1
i += 1
while i <= 10:
    sum = sum + i
    i += 1
print("The answer is {}.".format(sum))

