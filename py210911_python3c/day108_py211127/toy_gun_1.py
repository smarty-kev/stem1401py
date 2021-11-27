class Gun:
    def __init__(self, model, capacity, bullet_count):
        self.model = model
        self.capacity = capacity
        self.bullet_count = bullet_count

    def add_bullet(self, count):
        for i in range(count):
            self.bullet_count += 1
            if self.bullet_count == self.capacity:
                print("Fully reloaded!")
                break
        print(f"There are {self.bullet_count} bullets in the gun.")

    def shoot(self):
        if self.bullet_count > 0:
            self.bullet_count -= 1
            print("POW!")
        else:
            print("You do not have any bullets. Please reload first.")


class Soldier:
    def __init__(self, name, gun=None):
        self.name = name
        self.gun = gun

    def yell(self):
        print("Soldier yells.")

    def fire(self):
        if self.gun is not None:
            self.yell()
            self.gun.shoot()
        else:
            print("Stay in position.")

    def reload(self, count):
        self.gun.add_bullet(count)


tom = Soldier("Tom")
ak = Gun("AK47", 8, 8)
tom.gun = ak

for i in range(10):
    tom.fire()
tom.reload(1)
tom.fire()