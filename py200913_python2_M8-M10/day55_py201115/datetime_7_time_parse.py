"""

"""

from datetime import time

time1 = time(hour=23, minute=59, second=45, microsecond=37)
print(time1)


print(f"hour = {time1.hour}")
print(f"min = {time1.minute}")
print(f"sec = {time1.second}")
print(f"microsec = {time1.microsecond}")
print()

time1 = time(hour=23, minute=59, microsecond=37)
print(time1)

print(f"hour = {time1.hour}")
print(f"min = {time1.minute}")
print(f"sec = {time1.second}")
print(f"microsec = {time1.microsecond}", type(time1.microsecond))
print(f"milliseconds = {time1.microsecond/1000}")
