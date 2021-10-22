"""
Coding plantvszombie__design_v2_KevinLiu 12
"""


# n2 : write a program to calculate 1x2x4x6x8x10...x20

a = 1

for i in range(1,21):
    if i % 2 == 0:
        i = i * a
        a = i

print("The answer is {}.".format(i))


# n3 : use coding to determine the class average and how many students got grade A

how_many_students = 7
grades = [85,78,96,85,73,59,45]

a = 0
num_of_A = 0

for i in grades:
    if i >= 90:
        num_of_A += 1
    i = i + a
    a = i
else:
    i /= 7

print("The average of the class is {}".format(i))

if num_of_A == 0:
    print("Nobody got an A grade.")
elif num_of_A == 1:
    print("1 person got an A grade.")
else:
    print("{} persons got an A grade.".format(num_of_A))
