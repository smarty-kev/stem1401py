from py210911_python3c.day102_py211016.plantvszombie__design_v2_KevinLiu.zombie import Zombie


class PoleVaultingZombie(Zombie):
    # variables
    hp = 500
    atk_dmg = 15
    jumping_pole = "Yes"  # yes : still has jump power, if no : cannot jump

    # behaviours
    def jump(self):
        if self.jumping_pole == "Yes":
            self.coordinate[1] -= 1
        self.jumping_pole = "No"
