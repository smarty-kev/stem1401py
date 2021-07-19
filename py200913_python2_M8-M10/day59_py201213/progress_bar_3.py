"""

"""

import time

INTERVAL = 1

print("=== My Progress Bar ===")
time.sleep(INTERVAL)
for i in range(0, 21):
    if i != 21:
        print(f"\r[{'◼'*(i-1)+'>':20}]{5*i}%", end="", flush=True)
        time.sleep(INTERVAL)
    if i == 20:
        print(f"\r[{'◼'*i:20}]{5*i}%", end="", flush=True)
        time.sleep(INTERVAL)


