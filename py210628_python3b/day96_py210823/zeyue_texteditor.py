"""
[Final Quiz]
Date: 2021-08-23
Design at least 3 major features for a text editor
Do a quick research on the Internet if you need some ideas or references
Save your project as 'mytexteditor'
Share your project to github
Post your URL of your remote git repository to SLACK
Due date: 2021-08-31
Hints:
Self-study on font family, size, weight of text widget in Tkinter
"""

# import
from tkinter import *
from tkinter import font


# functions
def set_font(local_font_name):
    global font_name
    font_name.set(local_font_name)
    font_settings.config(family=local_font_name)


def set_size(local_size):
    global size
    size.set(local_size)
    font_settings.config(size=local_size)


def set_weight(local_weight):
    global weight
    weight.set(local_weight)
    font_settings.config(weight=local_weight)


# main window
root = Tk()
root.title("My Text Editor | Ze Yue Li | V1.0")
root.geometry("640x480+200+200")

# default values
font_name = StringVar()
size = StringVar()
weight = StringVar()
default_font_name = 'Helvetica'
default_size = 12
default_weight = 'normal'
font_settings = font.Font(family=default_font_name, size=default_size, weight=default_weight)
fonts = ['Calibri', 'Courier New', 'Helvetica', 'Times New Roman']
sizes = ['8', '10', '11', '12', '16', '24']
weights = ['normal', 'bold']

menu_bar = Menu(root)

# menus
font_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Font family", menu=font_menu)

for i in fonts:
    font_menu.add_command(label=i, command=lambda a=i: set_font(a))

size_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Font size", menu=size_menu)

for i in sizes:
    size_menu.add_command(label=i, command=lambda a=i: set_size(a))

weight_menu = Menu(menu_bar)
menu_bar.add_cascade(label="Font weight", menu=weight_menu)

for i in weights:
    weight_menu.add_command(label=i, command=lambda a=i: set_weight(a))

# text box
text_frame = Frame(root)
text_frame.pack(fill=BOTH, expand=Y)

text = Text(text_frame, height=5, width=30)
text.config(font=font_settings)
text.pack(side=LEFT, fill=BOTH, expand=Y)

scrollbar = Scrollbar(text_frame)
scrollbar.pack(side=RIGHT, fill=Y)
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)

# labels (for testing)
# font_label = Label(root, textvariable=font_name)
# font_label.pack(side=BOTTOM)
#
# size_label = Label(root, textvariable=size)
# size_label.pack(side=BOTTOM)
#
# weight_label = Label(root, textvariable=weight)
# weight_label.pack(side=BOTTOM)

root.config(menu=menu_bar)

root.mainloop()