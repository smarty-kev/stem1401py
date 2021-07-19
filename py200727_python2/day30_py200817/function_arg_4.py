"""
variable function argument

3. python arbitrary argument
"""

print(1)
print(1,2)
print(1,2,3)
print(1,2,3,4)

# print(*object,end="\n",sep=" ")

# calculate the sum of your (arbitrary) input
# return
# output the sum of your input

def mysum(*num):
    # print(num,type(num))
    sum = 0
    for i in num:
        # print(i)
        sum = sum + i
    return sum


sum = mysum(1,2,3,4,5,6)
print(sum)
print("====")

#
def foo(n,*m):
    print(n)
    print(m)

print(foo(1,2,3))

def foo(*m,n):
    print(m)
    print(n)

def foo(*m, a="1",n):
    print(a)
    print(n)
    pass

# foo(1,2,3,a=1,3)
