"""
exercise 3

Display 9x9 multiplication table

1x1 = 1
1x2 = 2     2x2 = 4
1x3 = 3     2x3 = 6     3x3 = 9
...
...
1x9 = 9     2x9 = 18    3x9 = 27.... 9x9 = 81
"""

numbers = [1,2,3,4,5,6,7,8,9]

str_template = "{}x{} = {}"

for a in numbers:
    for i in range(1, a + 1):
        print(str_template.format(i,a,i*a),end=" ",sep="")
    print()
