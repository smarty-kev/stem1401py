"""
alignment of numbers
"""

# 1.abc
# 2.abc
# 3.abc
# 9.abc
# 10.abc

print("|{:0}|".format(1))
print("|{:0}|".format(9))
print("|{:0}|".format(10))
print("|{:0}|\n".format(99))

print("|{:2}|".format(1))
print("|{:2}|".format(9))
print("|{:2}|".format(10))
print("|{:2}|\n".format(99))

print("|{:6}|".format(1))
print("|{:6}|".format(9))
print("|{:6}|".format(10))
print("|{:6}|\n".format(99))

print("|{:02}|".format(1))
print("|{:02}|".format(9))
print("|{:02}|".format(10))
print("|{:02}|\n".format(99))

print("|{:6}|".format(123))
print("|{:6}|".format(12345678))
print("|{:10.4f}|".format(1234.5678))
print("|{:010.4f}|".format(1234.5678))