"""
module : datetime
class : timedelta
"""

from datetime import datetime, date

# case 1
# 2020-06-01
t1 = date(year=2020, month=6, day=1)

# 2019-06-01
t2 = date(year=2019, month=6, day=1)

dt = t1 - t2
print(f"delta time is {dt}")

# case 2
# 2020-06-01
t3 = datetime(year=2020, month=6, day=1, hour=8, minute=8, second=15)

# 2019-06-01
t4 = datetime(year=2019, month=6, day=1, hour=9, minute=15, second=19)

dt2 = t3 - t4
print(f"delta time is {dt2}")

dt3 = t4 - t3
print(f"delta time is {dt3}")
