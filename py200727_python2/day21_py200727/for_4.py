"""
nested for loop

what is a matrix


"""

matrix1 = [
    [1,2,3,4],
    [2,4,6,8],
    [3,6,9,12]
]

# print(matrix1)

for row in matrix1:
    # print(row)
    for col in row:
        print(col,end=" ")
    print()
