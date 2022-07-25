import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 3  # in seconds
resume_key = Key.f5
pause_key = Key.f4
exit_key = Key.f6
#  ==========================

pause = True
running = True


def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")
        exit()


def display_controls():
    print("// AutoClicker by iSayChris")
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t F5 = Resume")
    print("\t F4 = Pause")
    print("\t F6 = Exit")
    print("-----------------------------------------------------")
    print('Press F5 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
