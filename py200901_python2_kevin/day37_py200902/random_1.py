"""
there are many random cases or numbers in the nature

to generate a real random number is not easy

random seed
random number

random event

evenly distributed
weighed distributed -> not evenly distributed
"""

import random

# to create random number

# a = random.randrange(1,7)
# print(a)

# write to prove the number you input is not included in the random number set
while True:
    a = random.randrange(7)
    if a == 6:
        print(a)
        break
    else:
        print(a)
# for i in range(10):
#     a = random.randrange(6)
#     print(a)

b = random.randint(1,6)
print()

for i in range(100):
    b = random.randint(1, 6)
    print(b)
