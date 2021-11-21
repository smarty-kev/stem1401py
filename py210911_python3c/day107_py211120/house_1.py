"""

"""


class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return self.name


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return self.house_type + ","\
                + str(self.area) + ","\
                + str(self.free_area) + ","\
                + self.item_list

    def add_house_item(self, house_item):
        if house_item.area < self.free_area:
            self.item_list.append(house_item)
            self.free_area -= house_item.area
        else:
            print("Not enough space.")


peter_house = House("Duplex", 50)

peter_bed = HouseItem("Bed", 4)
peter_chest = HouseItem("Chest", 2)
peter_table = HouseItem("Table", 1.5)

peter_house.add_house_item(peter_bed)
peter_house.add_house_item(peter_chest)
peter_house.add_house_item(peter_table)
