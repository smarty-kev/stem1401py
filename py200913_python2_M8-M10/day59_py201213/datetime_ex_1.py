"""
date.today()
date.weekday()
"""

import datetime

today = datetime.date.today()
print(today.weekday())

offset = (today.weekday() - 1) % 7

last_tuesday = today - datetime.timedelta(days=offset)

print(last_tuesday)
