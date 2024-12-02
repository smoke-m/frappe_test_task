import time
import pyautogui


def calculator():
    pyautogui.press("winleft", _pause=True)
    time.sleep(0.5)
    pyautogui.typewrite("calc", interval=0.2)
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(2)
    pyautogui.press("12")
    time.sleep(0.5)
    pyautogui.press("+")
    time.sleep(0.5)
    pyautogui.press("7")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("esc")


def emulator():
    # button_1_location = pyautogui.locateOnScreen(
    #     "calc1key.png", confidence=0.9
    #     )
    # button1_x, button1_y = pyautogui.center(button_1_location)
    button1_x, button1_y = pyautogui.locateCenterOnScreen(
        "screenshots/calc1key.png"
    )
    pyautogui.click(button1_x, button1_y)


if __name__ == '__main__':
    emulator()
