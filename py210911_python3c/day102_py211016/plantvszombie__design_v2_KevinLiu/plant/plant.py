from py210911_python3c.day102_py211016.plantvszombie__design_v2_KevinLiu.entity import Entity


class Plant(Entity):
    # Class variables

    # behaviours
    def __init__(self, hp, coord, sun_cost):
        super().__init__(hp, coord)
        self.sun_cost = sun_cost

