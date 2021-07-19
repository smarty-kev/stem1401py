"""

"""

import datetime


date = datetime.datetime.now()

str_year = date.strftime("%Y")
str_month = date.strftime("%-m")
str_month1 = date.strftime("%B")
str_month2 = date.strftime("%b")
str_day = date.strftime("%d")
str_time = date.strftime("%X")
str_datetime = date.strftime("%x") + date.strftime("%X")
str_datetime1 = str_year + "-" + str_month2 + "-" + str_day + ", " + date.strftime("%X")

print(f"year : {str_year}")
print(f"month : {str_month}")
print(f"month : {str_month1}")
print(f"month : {str_month2}")
print(f"day : {str_day}")
print(f"time : {str_time}")
print(f"date and time : {str_datetime}")
print(f"date and time : {str_datetime1}")

