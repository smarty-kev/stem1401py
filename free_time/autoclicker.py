import pynput
import time

a = pynput.mouse.Controller()

time.sleep(5)


def spam_left():
    pass


while True:
    a.press(pynput.mouse.Button.left)
    a.release(pynput.mouse.Button.left)
    time.sleep(0.00000001)
