"""
count down and looping
"""
import time
# set count-down time in second
count_down = 10
# set interval time for freshing screen in second
interval = 0.25
for i in range(0, int(count_down/interval)):
    ch_list = ["\\", "|", "/", "-"]
    index = i % 4
    msg = "\rRunning... " + ch_list[index]
    print(msg, end="")
    time.sleep(interval)
print(u"\rDone." + "  "*len(msg))