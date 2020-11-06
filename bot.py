import pyautogui, time 
time.sleep(10)
f = open ("tiojano.txt", 'r')
for word in f:
    pyautogui.hotkey("win")
    pyautogui.typewrite('chrome', interval=0.50)
    pyautogui.press("enter", interval=1.0, _pause=True)
    pyautogui.typewrite('twitter.com')
    pyautogui.press("enter", interval=5.0)
    pyautogui.press("n", interval=5.0)
    pyautogui.typewrite(word)
    pyautogui.hotkey("ctrl","enter")