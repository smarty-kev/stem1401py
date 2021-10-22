class Entity:
    # Class variables
    hp = 0
    coordinate = (0, 0)

    # behaviours
    def __init__(self, hp, coord):
        self.hp = hp
        self.coordinate = coord
