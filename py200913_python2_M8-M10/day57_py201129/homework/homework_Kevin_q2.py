"""
Self-study on the topic of how to convert a datetime object to a formatted string including extracting part of it.
Using datetime format code

My source(s):
https://www.w3schools.com/python/python_datetime.asp

The datetime object has a method for formatting date objects into readable strings.

The method is called strftime(), and takes one parameter, format, to specify the format of the returned string
"""

import datetime

date_x = datetime.datetime(2013, 2, 6)

print(date_x.strftime("%m"), type(date_x.strftime("%m"))) # -> prints: 02 <class 'str'>
                                                                    # 02 is the month of date_x
print(date_x.strftime("%a"), type(date_x.strftime("%a"))) # -> prints: Tue <class 'str'>
                                                                    # Tue is the abbreviated weekday name
print(date_x.strftime("%w")) # -> prints: 2
                                    # 2 is the weekday as a decimal number

# etc

"""
what I learned:
strftime returns the specified string extracted from datetime objects
there multiple format codes, each one extracting different values (ex; year, month, day, hour, etc...) and different ways 
of displaying the value (ex: as a decimal, padded-decimal, abbreviated weekday name, etc...)
"""