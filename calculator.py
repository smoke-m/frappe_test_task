import os
from time import sleep

from pyautogui import click
from pyautogui import locateCenterOnScreen
from pyautogui import press

# словарь соответствия команд к скринам
cmd_img = dict(
    [
        ("+", "screenshots/calcPluskey.png"),
        ("-", "screenshots/calcMinuskey.png"),
        ("*", "screenshots/calcMultkey.png"),
        ("/", "screenshots/calcDividkey.png"),
        ("enter", "screenshots/calcEqukey.png"),
        ("esc", "screenshots/calcEsckey.png"),
        ("0", "screenshots/calcNulkey.png"),
        ("1", "screenshots/calc1key.png"),
        ("2", "screenshots/calc2key.png"),
        ("3", "screenshots/calc3key.png"),
        ("4", "screenshots/calc4key.png"),
        ("5", "screenshots/calc5key.png"),
        ("6", "screenshots/calc6key.png"),
        ("7", "screenshots/calc7key.png"),
        ("8", "screenshots/calc8key.png"),
        ("9", "screenshots/calc9key.png"),
    ]
)


def keyboard(task: tuple) -> None:
    """
    Открывает приложение Калькулятор.
    Выполняет задачу с помощью клавиатуры.
    """
    # Запуск только с помощью pyautogui
    # press("winleft", _pause=True)
    # sleep(2)
    # typewrite("calc", interval=0.2)
    # sleep(0.5)
    # press("enter")

    # Запуск только с помощью os
    os.system("calc")
    sleep(2)

    for btn in task:
        press(btn)
        sleep(0.5)


def mouse(task: tuple) -> None:
    """
    Открывает приложение Калькулятор.
    Выполняет задачу с помощью мыши.
    """
    os.system("calc")
    sleep(2)

    for btn in task:
        click(locateCenterOnScreen(cmd_img.get(btn), confidence=0.9))
        sleep(0.5)


if __name__ == '__main__':
    # в переменную task заносим действия
    task = ("1", "2", "+", "7", "enter")
    keyboard(task)
    mouse(task)
