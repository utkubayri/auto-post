import time
import pyautogui
import webbrowser


txt_file_path = "cipher.txt"


webbrowser.open("https://cipher.fan/user/ekmekdavasi") # profil linkiniz ile değiştirmeniz gerek

line_number = 0
while True:
    with open(txt_file_path, "r") as f:
        lines = f.readlines()

    if line_number < len(lines):
        line = lines[line_number].strip()
        line_number += 1

        # KONUMLAR "pyautogui.position()" kodu ile tespit edilip aşağıda uygun yerlere işlenir
        time.sleep(5)
        pyautogui.click(x=875, y=640) # cipher butonu konumunu buraya girmeniz gerekmekte

        time.sleep(2)
        pyautogui.typewrite(line) # kopyaladığını yapıştırır

        time.sleep(2)
        pyautogui.click(x=1515, y=378)  # yapıştırdıktan sonra cipher basıp postu atar. postu gönderdiğimiz cipher butonunun konumunu buraya gireriz
        time.sleep(20)
    else:
        time.sleep(60)


