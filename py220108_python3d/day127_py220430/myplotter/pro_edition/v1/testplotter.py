from plotter import *
from shapetest import *

plotter = MyPlotter()

# 2D
plotter.plotShape(circle)
plotter.plotShape(rectangle)
plotter.plotShape(square)
plotter.plotShape(triangle)
plotter.plotShape(right_triangle)
plotter.plotShape(oval)
plotter.plotShape(parallelogram)
plotter.plotShape(oval)

# 3D
plotter.plotShape(sphere)
plotter.plotShape(cube)
plotter.plotShape(cylinder)
plotter.plotShape(pyramid)

# color
plotter.fillColor(square, "red")
plotter.fillColor(square, "#ff0000")
print(f"This line of code is not a functionality of the plotter, simply for testing. The color of the shape {square.shape_type} is {square.color}")
