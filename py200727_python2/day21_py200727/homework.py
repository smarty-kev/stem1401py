"""
Homework
"""

"""
step 1. to print out the sequence

step 2. to do the calculation and get the product

set product variable
"""

#
product = 1
for i in range(1,21):
    # print(i)
    product = product * i

print("The product is {}".format(product))


# option 1.
score1 = 85
score2 = 78
score3 = 96
score4 = 85
score5 = 73
score6 = 59
score7 = 45

total_score = 0
total_score = score1+score2+score3+score4+score5+score6+score7
num_of_stu = 7
avg_score = total_score / num_of_stu

# print("The average score is {:.2f}".format(avg_score))

# option 2.
scores = [85,78,96,85,73,59,45]

total_score = 0

num_of_stu_a = 0

for score in scores:
    total_score = total_score + score
# print(total_score)
    if score >= 90:
        num_of_stu_a += 1

num_of_stu = len(scores)
# print(num_of_stu)
avg_score = total_score / num_of_stu

print("The average score is {:.2f}".format(avg_score))
print("The number of students who got an A is {}.".format(num_of_stu_a))

