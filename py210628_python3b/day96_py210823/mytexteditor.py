"""
my text editor

by : Kevin Liu
Last Modified : 23 August 2021
"""

from tkinter import *
from tkinter.ttk import Separator


def pinpoint_position(event):
    (row, column) = map(int, event.widget.index("end-1c").split("."))  # row = line
    status_text = f"Status: INSERT MODE  ROW:{row},COL:{column}"
    var.set(status_text)


def copy():
    global clipboard
    if 'Copied' not in var.get():
        var.set(var.get() + "       Copied.")
    clipboard = text_box.get("1.0", "end-1c")


def cut():
    pass


def paste():
    text_box.insert(END, clipboard)


def dark_mode():
    color = "dark gray"
    root.config(bg=color)
    text_frame.config(bg=color)
    text_box.config(bg=color)
    frame_toolbar.config(bg=color)
    status_bar.config(bg=color)
    frame_status.config(bg=color)
    theme_btn.config(text="Light Mode", command=light_mode)
    root.update()


def light_mode():
    color = "linen"
    root.config(bg=color)
    text_frame.config(bg=color)
    text_box.config(bg=color)
    frame_toolbar.config(bg=color)
    status_bar.config(bg=color)
    frame_status.config(bg=color)
    theme_btn.config(text="Dark Mode", command=dark_mode)
    root.update()


def new_file():
    pass


def open_file():
    pass


def save():
    pass


def save_as():
    pass


def change_font():
    global font
    if fonts.index(font) == len(fonts) - 1:
        font = fonts[0]
    else:
        font = fonts[fonts.index(font) + 1]
    font_var.set(font)
    entire_txt = text_box.get("1.0", "end-1c")
    # print(font)


# window specifications
root = Tk()
root.title("My Text Editor")
root.geometry("640x480+200+200")
root.config()


# toolbar
frame_toolbar = Frame(root, height=30)  # frame
frame_toolbar.pack(anchor=W)
clipboard = None
copy_btn = Button(frame_toolbar, text='Copy', command=copy)  # copy
copy_btn.pack(side=LEFT, padx=(5, 0))
frame_toolbar.bind_class("<<Copy>>", copy)
cut_btn = Button(frame_toolbar, text='Cut', command=cut)  # cut
cut_btn.pack(side=LEFT, padx=5)
paste_btn = Button(frame_toolbar, text='Paste', command=paste)  # paste
paste_btn.pack(side=LEFT, padx=5)
frame_toolbar.bind_class("<<Paste>>", paste)
theme_btn = Button(frame_toolbar, text='Dark mode', command=dark_mode)  # dark mode
theme_btn.pack(side=LEFT, padx=(0, 5))
font_label = Label(frame_toolbar, text="Font")  # font label
font_label.pack(side=LEFT, padx=(10, 0))
fonts = ("Helvetica", "Calibri", "Arial")  # families
font = fonts[0]; font_var = StringVar(); font_var.set(font)
family_btn = Button(frame_toolbar, textvariable=font_var, width=7, command=change_font)  # button to change font
family_btn.pack(side=LEFT, padx=5)

# text area
text_frame = Frame(root, height=30)  # frame
text_frame.pack(anchor=CENTER, fill=BOTH, expand=Y)
text_box = Text(text_frame, height=5, width=30)  # text box
text_box.pack(side=LEFT, fill=BOTH, expand=Y)


# scrollbar
vertical_scrollbar = Scrollbar(text_frame)  # scrollbar
vertical_scrollbar.pack(side=RIGHT, fill=Y)
vertical_scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=vertical_scrollbar.set)


# status area
frame_status = Frame(root, bg="light gray")  # frame
frame_status.pack(anchor=CENTER, fill=X)
sep = Separator(frame_status, orient=HORIZONTAL)  # separator
sep.pack(fill=X, padx=1)
var = StringVar()  # text variable for status
status_text = "Status: INSERT MODE"  # for mode and position
status_bar = Label(frame_status, textvariable=var, bg="light gray")
status_bar.pack(side=BOTTOM, anchor=S + W)
var.set(status_text)  # init text


# menu
menu_bar = Menu(root)  # main menu
file_menu = Menu(menu_bar, tearoff=0)  # main menu item - file
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=new_file)  # lvl 2 options
file_menu.add_command(label="Open File", command=open_file)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_command(label="Quit", command=root.destroy)


edit_menu = Menu(menu_bar, tearoff=False)  # main menu item - edit
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Copy", command=copy)  # lvl 2 options
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Paste", command=paste)


# set menu to window
root.config(menu=menu_bar)


# watching
text_box.bind("<KeyRelease>", pinpoint_position)


root.mainloop()
