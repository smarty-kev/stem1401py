"""
[Homework]
Date: 2021-01-30
1. Try out label widget
Description:
create a window based on previous plantvszombie__design_v2_KevinLiu
set icon, title, dimension, maxsize, minsize, bg and any other options for the window as much as you know
create a text Label
set dimension, font, fg, bg, font and any other options which are necessary you think.
Due date: by the end of next Friday
"""

import tkinter
import time

root = tkinter.Tk()


# window title
root.title("Homework, Label - Kevin Liu")


# window icon
# after some research, I found that the format for mac icon is ".icns", but I don't know how to use it using tkinter
image = False
if image:
    root.iconbitmap(image)


# window width and height
w_width = int(input("Please enter the desired width for your widget: "))
w_height = int(input("Please enter the desired height for your widget: "))

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

top_left_x = int(sw/2 - w_width/2)
top_left_y = int(sh/2 - w_height/2)

root.geometry(f"{w_width}x{w_height}+{top_left_x}+{top_left_y}")


# window background color
root.configure(background="purple")


# window -> topmost
root.wm_attributes("-topmost", True)


# window maxsize and minsize
root.maxsize(1600, 900)
root.minsize(300, 200)


# window -> resizable
root.resizable(1, 1)


# label
label1 = tkinter.Label(root, text="This is a normal sized label :)", fg="pink", bg="gray", font=12, width=20, height=1)
label1.pack()

label2 = tkinter.Label(root, text="Big Label (:", fg="gold", bg="blue", font=16, width=80, height=20)
label2.pack()

label3 = tkinter.Label(root, text="tiny", fg="white", bg="black", font=5, width=2, height=1)
label3.pack()

label3 = tkinter.Label(root, text="You may resize the window (you have 10 secs), "
                                  "the new dimension will be echoed in console"
                       , fg="green", bg="yellow")
label3.pack()


# update
root.update()

time.sleep(10)


root.update()

# echo initial height and width of your window at console
print("Your window's width =", root.winfo_width())
print("Your window's height =", root.winfo_height())


root.mainloop()
