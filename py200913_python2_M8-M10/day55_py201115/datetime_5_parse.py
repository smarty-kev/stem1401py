"""
get today's year, month, day

parsing

xmL

<tag>xxx<tag>
"""

from datetime import date

today_obj = date.today()

print(today_obj)
print()

# parsing
print(f"year = {today_obj.year}")
print(f"month = {today_obj.month}")
print(f"day = {today_obj.day}")
print()

# exercise
# parsing 2025 Christmas
date_obj = date(2025, 12, 25)
print(date_obj, type(date_obj))

print(f"year = {date_obj.year}")
print(f"month = {date_obj.month}")
print(f"day = {date_obj.day}")
print()

# default date
default_date = date(2020, 12, 31)
print(default_date)


#
year = int(input())
month = int(input())
day = int(input())

try:
    date_obj = date(year, month, day)  # ValueError: month must be in 1..12 , ValueError: day is out of range for month
    print(date_obj, type(date_obj))

    print(f"year = {date_obj.year}")
    print(f"month = {date_obj.month}")
    print(f"day = {date_obj.day}")
except ValueError as ve:
    print(ve)
except Exception as e:
    print(e)
