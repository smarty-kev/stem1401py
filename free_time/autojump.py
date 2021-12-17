from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

time.sleep(5)


def spam_left():
    pass


while True:
    keyboard.press(Key.space)
    keyboard.release(Key.space)
    time.sleep(1)
