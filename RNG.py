import pyautogui
import keyboard

while True:
    pyautogui.moveTo(2449, 1118)
    pyautogui.click(2449, 1118)
    pyautogui.moveTo(1597, 1149)
    pyautogui.click(1597, 1149)
    pyautogui.moveTo(2067, 833)
    pyautogui.click(2067, 833)
    
    if keyboard.is_pressed("t"):  # if you press T
        print("Loop stopped!")
        break
