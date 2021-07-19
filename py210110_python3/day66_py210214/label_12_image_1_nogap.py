"""
show an .gif image without showing any gaps
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Label Image")

# step 1.
photo_obj = tk.PhotoImage(file="img/pimon.gif")

# step 2.
label = tk.Label(root, image=photo_obj)
label.pack()

root.mainloop()