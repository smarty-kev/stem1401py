"""
datetime.time
time object
"""

from datetime import time

# no argument
default = time()
print(f"default time is {default}")

# hour, min, sec
# time2 = time(11, 22, 66)
# print(time2)

# time2 = time(11, 60, 45)
# print(time2)

# hour = 0 - 23
time2 = time(23, 59, 45)
print(time2)

# time2 = time(24, 59, 45)
# print(time2)


#
time3 = time(hour=23, minute=59, second=45)
print(time2)


time3 = time(hour=23, minute=45)
print(time2)

time3 = time(minute=45)
print(time2)

time3 = time(second=56, minute=45)
print(time2)


# microsecond
time4 = time(hour=23, minute=59, second=45, microsecond=37)
print(time4)
