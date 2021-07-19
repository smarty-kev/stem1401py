"""
[Homework] 2021-01-24

Write a Python GUI program to create your own window
Common requirements:
1. set a title
2. set an image icon
Extra requirements:
1. specify dimension at 16:9
2. make it at center point on your screen
3. set a background color
4. make it topmost
5. set max size and min size
6. make it resizable
7. print out the initial height and width of your window at console
8. resizing your window
9. print out the current height and width of your window at console
Due date: by the end of next Saturday
"""

import tkinter
import time

print("This program will create a widget of specified size."
      " After, it is going to resize it to 500x350, then ending the program")

root = tkinter.Tk()


# window title
root.title("Homework - Kevin Liu")


# window icon
# after some research, I found that the format for mac icon is ".icns", but I don't know how to use it using tkinter
image = False
if image:
    root.iconbitmap(image)


# window width and height
print("Please enter a 16:9 ratio dimension for your widget, must be equal or smaller than 1600x900")
w_width = int(input("Please enter the desired width for your widget: "))
w_height = int(input("Please enter the desired height for your widget: "))

while w_width/w_height != 16/9 or w_width > 1600 or w_height > 900:
    print("Please enter a 16:9 ratio dimension for your widget (ex: 1600x900 or 800x450, etc...)"
          "\nMust be equal or smaller than 1600x900")
    w_width = int(input("Please enter the desired width for your widget: "))
    w_height = int(input("Please enter the desired height for your widget: "))

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

top_left_x = int(sw/2 - w_width/2)
top_left_y = int(sh/2 - w_height/2)

root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")


# window background color
root.configure(background="pink")


# window -> topmost
root.wm_attributes("-topmost", True)


# window maxsize and minsize
root.maxsize(1600, 900)
root.minsize(300, 200)


# window -> resizable
root.resizable(1, 1)


root.update()


# echo initial height and width of your window at console
print(root.winfo_width(), "= initial width")
print(root.winfo_height(), "= initial height")


# resizing
time.sleep(2) # to see the effect of resizing

w_width = 500
w_height = 350

top_left_x = int(sw/2 - w_width/2)
top_left_y = int(sh/2 - w_height/2)

root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")

root.update()
time.sleep(2) # to see the effect of resizing

# echo the new height and width of your window at console
print(root.winfo_width(), "= new width")
print(root.winfo_height(), "= new height")
