"""
Inheritance type : single inheritance
Description
Clothing(size, material, color, cost, wear(), wash())
TShirt(picture_on_front, picture_on_back)
A t-shirt is a clothe.
"""


class Clothing:
    def __init__(self, size, material, color, cost):
        self.size = size
        self.material = material
        self.color = color
        self.cost = cost

    def wear(self):
        print("Wears {}.".format(self.__class__.__name__))

    def wash(self):
        print("Washes {}.".format(self.__class__.__name__))


class TShirt(Clothing):
    def __init__(self, size, material, color, cost, picture_on_front, picture_on_back):
        super().__init__(size, material, color, cost)
        self.front_image = picture_on_front
        self.back_image = picture_on_back


t_shirt_1 = TShirt("small", "synthetic", "black", 14.99, None, None)
t_shirt_1.wash()
t_shirt_1.wear()
