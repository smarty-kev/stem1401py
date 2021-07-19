"""
while - else
"""

# else

x = 0
y = 1

while y <= 10:
    x = x + y
    y += 1
else:
    print("Inside else")

print("The answer is {}".format(x))
