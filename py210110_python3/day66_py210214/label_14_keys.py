"""

"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Keys")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


label1 = tk.Label(root, text="Keys")
label1.pack()

list_keys = label1.keys()
for key in list_keys:
    print(key)

root.mainloop()