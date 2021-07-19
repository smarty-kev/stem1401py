"""
quiz 5
"""

bool1 = True
print(bool1, type(bool1))

print(isinstance(bool1, int))
print(isinstance(bool1, bool))

# fi is a floating number
f1 = 1.23
print(type(f1))

#
num = 9
print(isinstance(num, int))

# 6.2
mylist = [2,6,3,1,0,7]
print(mylist[0])
print(mylist[-1])
print(mylist[5])

# 6.3
mylist[3] = 999
print(mylist[3])

# 6.4
mytuple = (2,6,3,1,0,7)
print(mytuple[0])
print(mytuple[5])

# 6.5
# mytuple[3] = 999

# 6.6
myset = {1,1,2,2,3,3}
print(myset)

# 6.7
mydict = {
    "Mon" : 1,
    "Tue" : 2
}

print(mydict)

# 7
a1 = 1.2
b1= str(a1)
print(b1, type(b1))

# ValueError: invalid literal for int() with base 10: '1.2'
b1 = '3'
c1 = int(b1)
print(c1, type(c1))
print()

# convert a1 into float
a1 = '1.2'
b1 = float(a1)
print(b1)

# convert b1 into int
c1 = int(b1)
print(c1, type(c1))