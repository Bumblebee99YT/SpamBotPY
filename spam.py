import pyautogui, time
time.sleep(5)
f = open("beemoviescript.txt", 'r')
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")