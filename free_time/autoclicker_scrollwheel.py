"""

"""

import pynput
import keyboard

mouse = pynput.mouse.Controller()


def click():
    mouse.press(pynput.mouse.Button.left)
    mouse.release(pynput.mouse.Button.left)


keyboard.on_press("q", click)
