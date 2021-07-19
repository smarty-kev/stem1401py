"""
Tkinter
a label counter
config()
after()
def a function in another function
global scope, global variable
recursive function
high order function (filter, map)
"""
from tkinter import *
def run_counter(digit):
    """
    execute the counter and show current number on the Label
    :param digit: the label with which it display numbers
    :return:
    """
    def counting():
        global counter
        counter += 1
        digit.config(text=str(counter))
        digit.after(1000, counting)
    counting()
# main program
root = Tk()
root.title('Python GUI - Label position')
root.geometry("{}x{}+200+240".format(640, 480))
root.configure(bg='#ddddff')
# label object
digit_label = Label(root,
              bg = "seagreen",
              fg = 'white',
              height = 3,
              width = 10,
              font = "Helvetic 30 bold")
digit_label.pack()
# counting
counter = 0
run_counter(digit_label)
root.mainloop()