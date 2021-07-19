"""
count down and looping
"""

from datetime import date, datetime
from datetime import timedelta
today = date.today()
wkday_today = today.weekday()
print(wkday_today)
wkday_tue = 1
offset = wkday_today - wkday_tue
print(offset)
delta = timedelta(days=offset)
tues = today - delta
print(tues)

print("====")
d1 = datetime(2020,12,7)
print(d1.weekday())
print(d1.strftime("%Y-%m-%d %w %A"))
wkday_d1 = d1.weekday()
offset = (wkday_d1 - wkday_tue)%7
print('offset=',offset)
delta = timedelta(days=offset)
tues = d1 - delta
print(tues)
