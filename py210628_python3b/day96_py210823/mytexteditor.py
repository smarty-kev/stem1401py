"""
my text editor
by : Kevin Liu
Last Modified : 23 August 2021
"""

from tkinter import *
from tkinter.ttk import Separator
from tkinter import font


def pinpoint_position(event):
    (row, column) = map(int, event.widget.index("end-1c").split("."))  # row = line
    status_text = f"Status: INSERT MODE  ROW:{row},COL:{column}"
    var.set(status_text)


def copy(event):
    global clipboard
    if 'Copied' not in var.get():
        var.set(var.get() + "       Copied.")
    clipboard = text_box.selection_get()


def cut(event):
    if text_box.selection_get():
        text_box.delete("sel.first", "sel.last")


def paste(event):
    position = text_box.index(INSERT)
    text_box.insert(position, clipboard)


def dark_mode():
    color = "dark gray"
    root.config(bg=color)
    text_frame.config(bg=color); text_box.config(bg=color)
    frame_toolbar.config(bg=color)
    copy_btn.config(bg=color); cut_btn.config(bg=color); paste_btn.config(bg=color)
    theme_btn.config(bg=color); family_btn.config(bg=color); size_label.config(bg=color)
    font_add_size.config(bg=color); font_sub_size.config(bg=color)
    font_label.config(bg=color); size_label.config(bg=color)
    status_bar.config(bg=color); frame_status.config(bg=color)
    theme_btn.config(text="Light Mode", command=light_mode)
    root.update()


def light_mode():
    color = "linen"
    root.config(bg=color)
    text_frame.config(bg=color); text_box.config(bg=color)
    frame_toolbar.config(bg=color)
    copy_btn.config(bg=color); cut_btn.config(bg=color); paste_btn.config(bg=color)
    theme_btn.config(bg=color); family_btn.config(bg=color); size_label.config(bg=color)
    font_add_size.config(bg=color); font_sub_size.config(bg=color)
    font_label.config(bg=color); size_label.config(bg=color)
    status_bar.config(bg=color); frame_status.config(bg=color)
    theme_btn.config(text="Dark Mode", command=dark_mode)
    root.update()


def new_file():
    text_box.delete("1.0", END)


def open_file():
    pass


def save():
    pass


def save_as():
    pass


def change_font():
    global font_family
    if font_families.index(font_family) == len(font_families) - 1:
        font_family = font_families[0]
    else:
        font_family = font_families[font_families.index(font_family) + 1]
    font_family_var.set(font_family)
    font_settings.config(family=font_family)
    text_box.config(font=font_settings)


def add_size():
    global size
    size += 1
    size_var.set(size)
    font_settings.config(size=size)


def sub_size():
    global size
    if size != 1:  # to not make text smaller than size 1
        size -= 1
    size_var.set(size)
    font_settings.config(size=size)


# window specifications
root = Tk()
root.title("My Text Editor | Kevin Liu")
root.geometry("640x480+200+200")
root.config(bg="linen")


# toolbar
frame_toolbar = Frame(root, height=30, bg="linen")  # frame
frame_toolbar.pack(anchor=W)
clipboard = ""
copy_btn = Button(frame_toolbar, text='Copy', bg="linen", command=lambda: copy(False))  # copy
copy_btn.pack(side=LEFT, padx=(5, 0))
root.bind("<Control-Key-c>", copy)
cut_btn = Button(frame_toolbar, text='Cut', bg="linen", command=lambda: cut(False))  # cut
cut_btn.pack(side=LEFT, padx=5)
root.bind("<Control-Key-x>", cut)
paste_btn = Button(frame_toolbar, text='Paste', bg="linen", command=lambda: paste(False))  # paste
paste_btn.pack(side=LEFT, padx=5)
root.bind("<Control-Key-v>", paste)
theme_btn = Button(frame_toolbar, text='Dark mode', bg="linen", command=dark_mode)  # dark mode
theme_btn.pack(side=LEFT, padx=(0, 5))
font_label = Label(frame_toolbar, text="Font", bg="linen")  # font label
font_label.pack(side=LEFT, padx=(10, 0))
font_families = ("Calibri", "Damascus", "Rockwell")  # families, you add as many as you want
font_family = font_families[0]  # default family
font_family_var = StringVar(); font_family_var.set(font_family)
family_btn = Button(frame_toolbar, textvariable=font_family_var, width=7, bg="linen", command=change_font)  # button to change font
family_btn.pack(side=LEFT, padx=5)
size = 12  # default size
size_var = IntVar(); size_var.set(size)
size_label = Label(frame_toolbar, textvariable=size_var, bg="linen")  # font size label
font_add_size = Button(frame_toolbar, text="+", width=7, font=(None, 8), bg="linen", command=add_size)  # add size button
font_sub_size = Button(frame_toolbar, text="-", width=7, font=(None, 8), bg="linen", command=sub_size)  # subtract size button
font_add_size.pack(side=LEFT, padx=5)  # first pack + button
size_label.pack(side=LEFT, padx=5)  # second pack label showing current size
font_sub_size.pack(side=LEFT, padx=5)  # finally pack - button


font_settings = font.Font(family=font_family, size=size)  # default font settings


# text area
text_frame = Frame(root, height=30, bg="linen")  # frame
text_frame.pack(anchor=CENTER, fill=BOTH, expand=Y)
text_box = Text(text_frame, height=5, width=30, bg="linen")  # text box
text_box.config(font=font_settings)  # apply default font settings
text_box.pack(side=LEFT, fill=BOTH, expand=Y)


# scrollbar
vertical_scrollbar = Scrollbar(text_frame, bg="linen")  # scrollbar
vertical_scrollbar.pack(side=RIGHT, fill=Y)
vertical_scrollbar.config(command=text_box.yview)
text_box.config(yscrollcommand=vertical_scrollbar.set)


# status area
frame_status = Frame(root, bg="linen")  # frame
frame_status.pack(anchor=CENTER, fill=X)
sep = Separator(frame_status, orient=HORIZONTAL)  # separator
sep.pack(fill=X, padx=1)
var = StringVar()  # text variable for status
status_text = "Status: INSERT MODE"  # for mode and position
status_bar = Label(frame_status, textvariable=var, bg="linen")
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


# mainloop
root.mainloop()
