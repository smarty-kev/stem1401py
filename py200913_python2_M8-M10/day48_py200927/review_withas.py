"""
with as
"""


# 1
file = open("/tmp/foo.txt")

try:
    data = file.read()
except Exception as e:
    print(e)
finally:
    file.close()


# 2
with open("/tmp/foo.txt") as file:
    data = file.read()
