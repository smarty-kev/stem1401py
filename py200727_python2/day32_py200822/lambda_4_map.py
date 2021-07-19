"""
map()
"""

original = [1, 2, 3, 4]
target = []

# [1, 4, 9, 16]

# solution 1
for i in original:
    # print(i**2,end=", ")
    target.append(i**2)

print(target)

# solution 2
# target = map(lambda x: x ** 2, original)
# target = list(target)

print(list(map(lambda x: x ** 2, original)))
