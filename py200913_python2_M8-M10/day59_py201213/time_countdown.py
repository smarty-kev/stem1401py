"""

"""

import time

count_down = 10

for i in range(count_down, 0, -1):
    msg = u"\rThe system will exit in " + str(i) + " second(s)"
    print(msg, end="")
    time.sleep(1)

end_msg = "End." + "  "*(len(msg)-len("End."))

print(f"\r{end_msg}")
