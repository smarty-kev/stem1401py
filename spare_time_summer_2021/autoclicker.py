import pynput
import time

a = pynput.mouse.Controller()

time.sleep(5)


def spam_left():
    pass


for i in range(500):
    a.press(pynput.mouse.Button.left)
    a.release(pynput.mouse.Button.left)
time.sleep(1)
for i in range(500):
    a.press(pynput.mouse.Button.left)
    a.release(pynput.mouse.Button.left)
time.sleep(1)
for i in range(500):
    a.press(pynput.mouse.Button.left)
    a.release(pynput.mouse.Button.left)
time.sleep(1)
for i in range(500):
    a.press(pynput.mouse.Button.left)
    a.release(pynput.mouse.Button.left)
time.sleep(1)
for i in range(500):
    a.press(pynput.mouse.Button.left)
    a.release(pynput.mouse.Button.left)
time.sleep(1)
