"""
compound="value"
value = "left", "right", "top", "bottom", "center" - overlapped
"""

import tkinter as tk

root = tk.Tk()
root.title("Python GUI - Compound Label")

winw = 800
winh = 450
posx = 300
posy = 200
root.geometry(f"{winw}x{winh}+{posx}+{posy}")


label1 = tk.Label(root, text="Compound Label", compound="left", bitmap="question", fg="white", bg="black")
label1.pack()

label2 = tk.Label(root, text="Compound Label", compound="right", bitmap="info", fg="white", bg="black")
label2.pack()

label3 = tk.Label(root, text="Compound Label", compound="top", bitmap="gray75", fg="white", bg="black")
label3.pack()

label4 = tk.Label(root, text="Compound Label", compound="bottom", bitmap="error", fg="white", bg="black")
label4.pack()

label5 = tk.Label(root, text="Compound Label", compound="center", bitmap="info", fg="white", bg="black")
label5.pack()


#
root.mainloop()