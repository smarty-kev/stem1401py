"""
write a program to get an object of current date and time
convert object in timestamp
"""

import datetime

now = datetime.datetime.now()

timestamp = now.timestamp()
print(f"timestampp = {timestamp}")
date_time = datetime.datetime.fromtimestamp(timestamp)

print("Date time object:", date_time)

print("Output 2 :" ,date_time.strftime("%-m/%d/%Y"))
print("Output 3 :" ,date_time.strftime("%d %b, %Y"))
print("Output 4 :" ,date_time.strftime("%d %B, %Y"))
print("Output 5 :" ,date_time.strftime("%I%p"))
