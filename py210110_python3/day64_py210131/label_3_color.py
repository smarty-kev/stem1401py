"""
label color
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Label, Color")

winw = 640
winh = 480
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")
root.config(bg="#ddddff")


# create a label
label1 = tk.Label(root, text="Text Label", width=50, height=3, bg="blue", fg="white")

label1.pack()

label2 = tk.Label(root, text="Second Text Label", width=30, height=5, bg="red", fg="white")

label2.pack()

root.mainloop()