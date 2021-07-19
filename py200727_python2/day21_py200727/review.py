"""
review syntax for loop

"""

# case 1
mylist = [10,20,30,40,50]

for i in mylist:
    print(i,end=",")
print("\n")

# case 2

a = range(10)
print(a,"\n")

res = list(a)
print(res, type(res))
print()


for x in range(10):
    print(x,end=",")
print("\n")

b = range(1,10)
print(b, type(b),"\n")

for y in range(1,10):
    print(y,end=",")
print()


#
c = range(1, 10, 2)

d = range(1, 10, 1)
d = range(1, 10)

for z in range(1, 10, 2):
    print(z,end=",")


