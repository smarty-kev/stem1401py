"""
while loop

dead loop = runs without stopping
"""

"""
syntax of while loop:

while test_expression:
    body_of_while (code block)
"""

# if I want to print out a greetings words to my friends,
# i can use a loop structure

# 5 times
count = 0

while count < 5:
    print("Hello, Python!")
    count += 1

print("the last counter is {}".format(count))

print()

count = 5

while count > 0:
    print("Hello, Python!")
    count -= 1

print("the last counter is {}".format(count))
