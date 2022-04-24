"""
standard edition

Requirements of Standard Edition:
An end-user may input a name of shape from their keyboard.
The application then draws a shape that the user desires.
The basic parameter(s) of a shape should print on the console, which determines possible measurements of a shape.
i.e. perimeter, area, surface area, volume, etc.
The perimeter of a 2D shape should print on the console.
The area of a 2D shape should print on the console.
The volume of a 3D shape should print on the console.
The surface area of a 3D shape should print on the console.
"""


from shape_entities import Shape, TwoDShape, Circle, Rectangle, Square, Triangle, \
                                  ThreeDShape, Sphere, Cube


class PerimeterFinder:
    def getPerimeter(self, shape_obj):
        perimeter = shape_obj.findPerimeter()
        return perimeter

    def getMultiplePerimeter(self, *shape_obj):
        perimeters = []
        for obj in shape_obj:
            perimeters.append(self.getPerimeter(obj))
        return perimeters


class AreaFinder:
    def getArea(self, shape_obj):
        area = shape_obj.findArea()
        return area

    def getMultipleArea(self, *shape_obj):
        areas = []
        for obj in shape_obj:
            areas.append(self.getArea(obj))
        return areas


class VolumeFinder:
    def getVolume(self, shape_obj):
        volume = shape_obj.findVolume()
        return volume

    def getMultipleVolume(self, *shape_obj):
        volumes = []
        for obj in shape_obj:
            volumes.append(self.getVolume(obj))
        return volumes


class Drawer:
    def startDrawing(self, shape_obj):
        print("===New Shape===")
        print(f"Drawing the shape \"{shape_obj.shape_type}\"...")

    def finishDrawing(self):
        print("Finished drawing.")
        print("\n")


class MyPlotter(PerimeterFinder, AreaFinder, VolumeFinder):
    def __init__(self):
        self.drawer = Drawer()
        print("===MY PLOTTER===\n\n")

    def plotShape(self, shape_obj):
        self.drawer.startDrawing(shape_obj)
        if shape_obj.dimension == "TwoD":
            perimeter = self.getPerimeter(shape_obj)
            area = self.getArea(shape_obj)
            print(f"The perimeter of the {shape_obj.shape_type} is {perimeter}")
            print(f"The area of the {shape_obj.shape_type} is {area}")
        elif shape_obj.dimension == "ThreeD":
            area = self.getArea(shape_obj)
            volume = self.getVolume(shape_obj)
            print(f"The area of the {shape_obj.shape_type} is {area}")
            print(f"The volume of the {shape_obj.shape_type} is {volume}")
        self.drawer.finishDrawing()
