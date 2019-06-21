import pyautogui

def incriment_voltages(level):
    '''This is function I made that incriments voltage using myDAQ troublshoot
    test panel, which has an analog output tab, which allows you to change the
    output voltage of a channel, which is what we do here to use as a heater'''
    pyautogui.moveTo(1461, 111)
    
    pyautogui.click()
    
    for i in range(0,10):
        pyautogui.press('delete')
    
    pyautogui.typewrite(str(level))
    
    pyautogui.press('enter')
    
    pyautogui.moveTo(1701, 434)
    
    pyautogui.click()
    
incriment_voltages(1)