"""

"""

import time

class ToyGun:
    def __init__(self, model, capacity, bullet_count):
        self.model = model
        self.capacity = capacity
        self.bullet_count = bullet_count

    def add_bullet(self, count):
        for i in range(count):
            self.bullet_count += 1
            time.sleep(0.5)
            if self.bullet_count == self.capacity:
                print("")
