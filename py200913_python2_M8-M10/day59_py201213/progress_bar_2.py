"""

"""

import time

INTERVAL = 1

print("=== My Progress Bar ===")
time.sleep(INTERVAL)
for i in range(0, 21):
    print(f"\r[{'='*i:20}]{5*i}%", end="", flush=True)
    time.sleep(INTERVAL)


