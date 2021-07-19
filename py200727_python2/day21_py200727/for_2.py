"""
for-loop
exercise 2

"""

"""
num = range(1,int(input("Please enter a number: ")) + 1)

str_temp = "12 x {} = {}"

for a in num:
    print(str_temp.format(a, 12 * a))
"""

# input a number
num = int(input("Please enter a number: "))
num += 1

# generating the multiplication table
for x in range(1,num):
    # print(x)
    str_template = "12 x {} = {}"
    print(str_template.format(x, 12 * x))
