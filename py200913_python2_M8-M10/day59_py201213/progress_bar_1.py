"""
progress bar
"""

import time

INTERVAL = 1

print("=== My Progress Bar ===")
print("[", end="")
time.sleep(INTERVAL)
for i in range(20):
    print("=", end="")
    time.sleep(INTERVAL)
print("]")
