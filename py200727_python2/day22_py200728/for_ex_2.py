"""
matrix(3x4)

1, 2, 3 ,4,
5, 6, 7, 8,
9, 10, 11, 12,

"""

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

max_num = matrix1[0][0]
min_num = matrix1[2][3]


for row in matrix1:
    for col in row:
        if col > max_num:
            max_num = col
        if col < min_num:
            min_num = col

print("The biggest number is {}.".format(max_num))
print("The smallest number is {}.".format(min_num))