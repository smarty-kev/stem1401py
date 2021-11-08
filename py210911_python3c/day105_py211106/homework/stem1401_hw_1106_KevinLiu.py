"""
- Problem description
Mahima has been experimenting with a new style of art.
She stands in front of a canvas and, using her brush, flicks drops of paint onto the canvas.
When she thinks she has created a masterpiece, she uses her 3D printer to print a frame to surround the canvas.

Your job is to help Mahima by determining the coordinates of the smallest possible rectangular frame such that each drop of paint lies inside the frame.
Points on the frame are not considered inside the frame.


- Input specification
The first line of input contains the number of drops of paint, N, where 2 =< N =< 100 and N is an integer.
Each of the next N lines contain exactly two positive integers X and Y separated by one comma (no spaces).
Each of these pairs of integers represents the coordinates of a drop of paint on the canvas.
Assume X < 100 and Y < 100, and that there will be at least two distinct points.
The coordinates (0, 0) represent the bottom-left corner of the canvas.

For 12 of the 15 available marks, X and Y will both be two-digit integers.

- Output specification
Output two lines.
Each line must contain exactly two non-negative integers separated by a single comma (no spaces).
The first line represents the coordinates of the bottom-left corner of the rectangular frame.
The second line represents the coordinates of the top-right corner of the rectangular frame.
"""

sample = (5,
    [44, 62],
    [34, 69],
    [24, 78],
    [42, 44],
    [64, 10]
            )

collected_data = []

use_sample = False


# main program


# data collection
print("If you wish to use the sample, please enter the number 0. If not:")
print("First, how many drops of paint did Mahima paint (minimum is 2, maximum is 100).\n"
      "Then input the coordinates of each paint drop. (format : 'x,y', where x and y are integers) ↓")
number_of_paint_drops = int(input())
collected_data.append(number_of_paint_drops)
for i in range(number_of_paint_drops):
    user_input = input()
    coordinates = user_input.split(",")
    collected_data.append(coordinates)

if number_of_paint_drops == 0:
    collected_data = sample


# data analysis
smallest_x = 100
biggest_x = 0

smallest_y = 100
biggest_y = 0

for i in range(collected_data[0]):
    x = int(collected_data[i+1][0])
    y = int(collected_data[i+1][1])

    if biggest_x < x <= 100:
        biggest_x = x

    if smallest_x > x >= 0:
        smallest_x = x

    if biggest_y < y <= 100:
        biggest_y = y

    if smallest_y > y >= 0:
        smallest_y = y

# print(biggest_x, smallest_x, biggest_y, smallest_y)
smallest_x -= 1
biggest_x += 1

smallest_y -= 1
biggest_y += 1


# answer
top_coordinates = [[biggest_x, smallest_y], [biggest_x, biggest_y]]       # top_coordinates[0] = top-left, top_coordinates[1] = top-right
bottom_coordinates = [[smallest_x, smallest_y], [smallest_x, biggest_y]]  # bottom_coordinates[0] = bottom-left, bottom_coordinates[1] = bottom-right
# print(top_coordinates, bottom_coordinates)

print("==============\nThe answer is:")
print(f"{bottom_coordinates[0][0]},{bottom_coordinates[0][1]}")
print(f"{top_coordinates[1][0]},{top_coordinates[1][1]}")
