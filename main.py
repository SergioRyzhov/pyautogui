import os
import pyautogui
import time

def open_calculator():
    platform = os.name
    if platform == 'nt':  # Windows
        os.system('start calc')
    elif platform == 'posix':  # macOS и Linux
        if os.uname().sysname == 'Darwin':  # macOS
            os.system('open -a Calculator')
        else:  # Linux
            os.system('gnome-calculator')  # для GNOME
    else:
        raise EnvironmentError("Unsupported OS")

def click_button(image, confidence=0.9):
    location = pyautogui.locateOnScreen(image, confidence=confidence)
    if location:
        pyautogui.click(pyautogui.center(location))
    else:
        raise FileNotFoundError(f"кнопка {image} не найдена")

def main():
    open_calculator()
    time.sleep(3)

    try:
        click_button('1.png')
        click_button('2.png')
        click_button('plus.png')
        click_button('7.png')
        click_button('equals.png')
    except FileNotFoundError as e:
        print(e)
        print("изображения находятся в другой папке")

if __name__ == '__main__':
    main()
