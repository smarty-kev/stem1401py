"""

"""

num = 9


a = ""

# if num % 2 == 0:
for i in range(2,num):
    if num % i == 0:
        a = False
        break
    else:
        a = True

if a:
    print("{} is a prime number.".format(num))
else:
    print("{} is not a prime number.".format(num))
