"""
create a label widget
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Label")

winw = 640
winh = 480
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


# create a label
label1 = tk.Label(root, text="Text Label")

label1.pack()

label2 = tk.Label(root, text="Second Text Label")

label2.pack()

root.mainloop()