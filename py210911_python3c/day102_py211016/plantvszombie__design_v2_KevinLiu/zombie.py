from py210911_python3c.day102_py211016.plantvszombie__design_v2_KevinLiu.entity import Entity


class Zombie(Entity):
    # Class variables
    atk_dmg = 0

    # behaviours
    def __init__(self, hp, coord, atk_dmg):
        super().__init__(hp, coord)
        self.atk_dmg = atk_dmg

    def move(self):
        pass

    def end_game(self):  # eat your brains
        pass
