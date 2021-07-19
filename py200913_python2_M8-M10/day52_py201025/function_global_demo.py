"""
pass argument as a container
"""

def gen2(mylist):
    mylist.append("v1")
    mylist.append("v2")
    mylist.append("v3")

# main prog

# prepare
mylist = []
print("before")
print(mylist)

# data processing
gen2(mylist)

# output
print("after")
print(mylist)
