"""
padx = a
pady = b
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Pad")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


label1 = tk.Label(root, text="normal text", bg="gold", fg="blue", padx=20, pady=15, font="helvetica 16 ")

label1.pack()

root.update()
w = label1.winfo_width()
h = label1.winfo_height()
print(w, h)
# 123 45 -> padx = 20, pady = 10
# 123 55 -> padx = 20, pady = 15

label2 = tk.Label(root, text="normal text", bg="red", fg="white", padx=30, pady=15)

label2.pack()

root.mainloop()