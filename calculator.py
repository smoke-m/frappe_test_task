import os

import time
import pyautogui


def calculator():
    """
    Открывает приложение Калькулятор
    Выполняет автоматизированные действия,
    чтобы сложить два числа (12 + 7)
    """
    # Запуск только с помощью pyautogui
    # pyautogui.press("winleft", _pause=True)
    # time.sleep(2)
    # pyautogui.typewrite("calc", interval=0.2)
    # time.sleep(0.5)
    # pyautogui.press("enter")

    # Запуск только с помощью os
    os.system("calc")

    time.sleep(2)
    pyautogui.press("1")
    time.sleep(0.5)
    pyautogui.press("2")
    time.sleep(0.5)
    pyautogui.press("+")
    time.sleep(0.5)
    pyautogui.press("7")
    time.sleep(0.5)
    pyautogui.press("enter")
    time.sleep(0.5)
    pyautogui.press("esc")


def pyautogui_click(img_png):
    """Функция кликов."""
    pyautogui.click(pyautogui.locateCenterOnScreen(img_png, confidence=0.9))


def emulator():
    """
    Эмуляции кликов по кнопкам 1, 2, +, 7, =
    в интерфейсе калькулятора.
    """
    pyautogui_click("screenshots/calc1key.png")
    pyautogui_click("screenshots/calc2key.png")
    pyautogui_click("screenshots/calcPluskey.png")
    pyautogui_click("screenshots/calc7key.png")
    pyautogui_click("screenshots/calcEqukey.png")
    pyautogui_click("screenshots/calcEsckey.png")


if __name__ == '__main__':
    calculator()
    emulator()
