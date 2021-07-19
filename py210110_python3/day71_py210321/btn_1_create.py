"""
Button

Create a button

# high order
# callback function
"""

from tkinter import *


# Hoist
def myresponse():
    print("I was clicked :)")


# main program
root = Tk()
root.title("Button - Create")
root.geometry("800x450+200+200")
root.configure(bg="#ddddff")

# create a button
# btn1 = Button(root, text="Click Me!", command=myresponse())
btn1 = Button(root, text="Click Me!", command=myresponse)
btn1.pack(padx=20, pady=40)

# create a button for closing
btn2 = Button(root, text="Close", command=root.destroy)
btn2.pack(padx=20, pady=40)

root.mainloop()
