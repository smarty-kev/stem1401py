"""
to create a main window
to set a title
to set image icon
to set size
to set initial position

.png
.jpg
.bmp
.gif

step 1. choose an image
square 32x32, 16x16

step 2. copy to working folder

step 3. convert to 'ico' format (.ico)
"""

import tkinter as tk

root = tk.Tk()

# settings
root.title('Python GUI - Title')
root.iconbitmap('IMG_2408.ico')
root.geometry("800x450-300+200") # to set size + to set initial position

# widget


root.mainloop()
