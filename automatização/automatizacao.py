import pyautogui

pyautogui.press("Win")
pyautogui.sleep(1)
pyautogui.write("Google Chrome", interval= 0.2)
pyautogui.sleep(1)
pyautogui.press("Enter")
pyautogui.sleep(3)
pyautogui.press("Win")
pyautogui.write("Visual Studio Code", interval= 0.2)
pyautogui.press("Enter")
pyautogui.sleep(3)
pyautogui.hotkey("alt", "f4")