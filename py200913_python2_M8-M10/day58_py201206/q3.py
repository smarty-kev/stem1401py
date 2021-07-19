"""

"""

import datetime

now = datetime.datetime.now()

timestamp = now.timestamp()
date_time = datetime.datetime.fromtimestamp(timestamp)

print("Output 1:", date_time.strftime("%c"))
print("Output 2:", date_time.strftime("%x"))
print("Output 3:", date_time.strftime("%X"))
