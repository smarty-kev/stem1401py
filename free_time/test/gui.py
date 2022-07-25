"""

"""
from tkinter import *


def open_password_generator_window():
    main_window.destroy()
    password_generator_window = Tk()
    password_generator_window.title("Password Generator")
    password_generator_window.geometry("800x450+200+200")
    password_generator_window.configure(bg="white")


def open_password_manager_window():
    main_window.destroy()
    password_manager_window = Tk()
    password_manager_window.title("Password Manager")
    password_manager_window.geometry("800x450+200+200")
    password_manager_window.configure(bg="white")


main_window = Tk()
main_window.title("Main Window")
main_window.geometry("800x450+200+200")
main_window.configure(bg="white")


# labels
button_open_password_generator = Button(main_window, text="Password Generator", command=open_password_generator_window)
button_open_password_manager = Button(main_window, text="Password Manager", command=open_password_manager_window)
button_open_password_generator.pack(padx=20, pady=20)
button_open_password_manager.pack(padx=20, pady=20)
