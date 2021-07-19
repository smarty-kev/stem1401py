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
root.geometry("800x450-300+200")

root.configure(bg="#ddddff")

root.mainloop()
