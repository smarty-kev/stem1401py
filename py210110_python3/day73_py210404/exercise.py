"""
1. First there is a label with a number as text
2. below, there is 3 buttons
3. The most right button is the exit button, which closes the widget when pressed
4. In the middle, when pressed, the button increases the number on the label by 2
5. At the most left, the button reduces the number on the label by 2 when clicked
6. The limit to increase is 10 and to decrease is -10. When it reaches 10, the + button becomes disabled.
When it reaches -10, the - button becomes disabled.
"""

# tkinter module
from tkinter import *


# add
def print_number(number):
    print(numbers[number])

# sub
# def print_number(number):
#   print(numbers[number])




# widget specifications
root = Tk()
root.title("Kevin L. Homework")
root.geometry("800x450+200+200")
root.config(bg="gray85")


# number list
numbers = []

# ask user to input N numbers
num = int(input("Please enter a number, a button with the number will be created. When clicked, the number will be echoed on console: "))
print("If you do not wish to add more numbers, type: done")
numbers.append(num)
while True:
    num = input('Please enter a number, or "done" if you are finished: ')
    if num == "done":
        break
    numbers.append(int(num))
# print(numbers)


Button(text="Exit", command=root.destroy).pack(pady=20, padx=15, anchor=S, side=RIGHT)
for i in range(len(numbers)):
    Button(text=numbers[i], command=lambda num=i: print_number(num)).pack(pady=20, padx=15, anchor=S, side=RIGHT)


# mainloop
root.mainloop()

