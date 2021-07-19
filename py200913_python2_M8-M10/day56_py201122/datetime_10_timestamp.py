"""

get timestamp from object
"""


from datetime import datetime

# OSError
a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("year =", a.month)
print("year =", a.day)
print("year =", a.min)


# get timestamp

print("timestamp =", a.timestamp())

