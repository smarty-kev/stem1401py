"""

"""

import datetime

date_string = "6 December, 2020 01:20:38"
try:
    date_object = datetime.datetime.strptime(date_string, "%d %B, %Y %X")
    print(date_object)
except ValueError as ve:
    print(ve)

