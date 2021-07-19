"""
simulate a clock

1. show time with interval of 1 second
2. localtime = time.localtime()
3. time.sleep(n_sec)
4. \r
"""

import time

# timer counter by 10 second
localtime = time.localtime()
# print(localtime)

"""
time.struct_time    (tuple)
tm_year
tm_month
tm_mday
tm_hour
tm_min
tm_sec
tm_wday     start from monday -> 0
tm_yday
tm_isdst    is weekend or not
"""

while True:
    # get current local time
    localtime = time.localtime()
    # print(localtime)

    # get string form
    result = time.strftime("%I:%M:%S %p", localtime)
    print('\r' + result, end="", flush=True)

    INTERVAL = 1  # seconds
    time.sleep(INTERVAL)
