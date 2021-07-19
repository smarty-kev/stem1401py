"""
[Homework] 2021-01-17
1. Create a main window with specified width and height
user may input width and height
2. Please center the window
3. Please add image icon to your window
"""

import tkinter

root = tkinter.Tk()

root.title("Homework - Kevin Liu")

# after some research, I found that the format for mac icon is ".icns", but I don't know how to use it using tkinter
image = False
if image:
    root.iconbitmap(image)

w_width = int(input("Please enter the desired width for your widget: "))
w_height = int(input("Please enter the desired height for your widget: "))

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

top_left_x = int(sw/2 - w_width/2)
top_left_y = int(sh/2 - w_height/2)

root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")

root.mainloop()
