"""
get time from timestamp

1970-01-01 at UTC
"""

from datetime import date

timestamp = date.fromtimestamp(1600000000)
print(type(timestamp))
print("DATE =", timestamp)
