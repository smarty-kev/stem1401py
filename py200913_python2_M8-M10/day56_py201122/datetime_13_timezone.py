"""
list all timezone
"""

from pytz import all_timezones


len_of_timezone = len(all_timezones)
print(len_of_timezone)

for tz in all_timezones:
    print(tz)