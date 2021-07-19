"""
to prove the break statement just terminates the innermost loop structure

step 1 create a nested for or while loop

step 2 place the break statement in correct position

step 3 run the program and draw a conclusion
"""

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]

# jump out of innermost loop
for row in matrix:
    for col in row:
        if col == 6:
            break
        print(col)
    print()

print("===2===")
# jump out of outermost loop
for row in matrix:
    for col in row:
        if col == 6:
            break
        print(col)
    # print("col in outer loop is {}").format(col)
    if col == 6:
        break
    print()