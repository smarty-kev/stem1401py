"""
matrix(3x4)

1, 2, 3 ,4,
5, 6, 7, 8,
9, 10, 11, 12,
13, 14, 15, 16,

to calculate the average of this matrix

"""

# step 1
matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]


# step 2

summary = 0

count = 0

for row in matrix1:
    # print(row)
    for col in row:
        # print(col)
        summary += col
        count += 1


# step 4
num = count
avg = summary / num

print("The average of the total of all the numbers in the matrix is {}".format(avg))
print("There are {} items in the matrix.".format(num))
