import pyautogui
import time

def incriment(level):
    pyautogui.moveTo(1461, 111)
    
    pyautogui.click()
    
    for i in range(0,10):
        pyautogui.press('delete')
    
    pyautogui.typewrite(str(level))
    
    pyautogui.press('enter')
    
    pyautogui.moveTo(1701, 434)
    
    pyautogui.click()
    
for i in range(0,3):
    incriment(i)
    time.sleep(5)