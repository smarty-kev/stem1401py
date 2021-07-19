"""
print out the coord for items of a matrix
3 * 3
"""


for row in range(0,3):
    for col in range(0,3):
        print(("({},{})".format(row,col)),end=" ")
    print()