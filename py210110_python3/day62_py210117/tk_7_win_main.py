"""
to create a main window
to set a title
to set image icon
to set size
to set initial position
background image
"""

import tkinter as tk

root = tk.Tk()

# settings
root.title('Python GUI - Title')
root.iconbitmap('IMG_2408.ico')


root.configure(bg="#ddddff")

sw = root.winfo_screenwidth()
sh = root.winfo_screenheight()

ww = 800
wh = 450

top_left_width = int(sw/2 - ww/2)
top_left_height = int(sh/2 - wh/2)

root.geometry(f"{ww}x{wh}+{top_left_width}+{top_left_height}")

print(root.winfo_screenmmwidth())
print(root.winfo_screenmmheight())

root.mainloop()
