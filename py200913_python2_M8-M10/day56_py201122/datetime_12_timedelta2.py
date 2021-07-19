"""
module : datetime
class : timedelta

days
weeks
hours
minutes
seconds


total_seconds()
"""

from datetime import datetime, date, timedelta

# case 1
t1 = datetime(year=2019, month=6, day=1, hour=9, minute=15, second=19)
dt1 = timedelta(days=366)

t2 = t1 + dt1

print(f"The new datetime is {t2}.")

# case 2
t1 = datetime(year=2019, month=6, day=1, hour=9, minute=15, second=19)
dt1 = timedelta(weeks=4)

t2 = t1 + dt1

print(f"The new datetime is {t2}.")


# case 3

dt3 = timedelta(weeks=4, days=3, hours=2)
ts = dt3.total_seconds()
print(f"Delta time has {ts} seconds")
