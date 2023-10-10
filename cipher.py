import time
import pyautogui
import webbrowser


txt_file_path = "cipher.txt"


webbrowser.open("https://cipher.fan/user/ekmekdavasi")

line_number = 0
while True:
    with open(txt_file_path, "r") as f:
        lines = f.readlines()

    if line_number < len(lines):
        line = lines[line_number].strip()
        line_number += 1

        time.sleep(5)
        pyautogui.click(x=875, y=640)

        time.sleep(2)
        pyautogui.typewrite(line)

        time.sleep(2)
        pyautogui.click(x=1515, y=378)
        time.sleep(20)
    else:
        time.sleep(60)


