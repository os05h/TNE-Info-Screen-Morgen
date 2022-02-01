import pyautogui

# Get the size of the primary monitor.
screenWidth, screenHeight = pyautogui.size()

# Get the XY position of the mouse.
currentMouseX, currentMouseY = pyautogui.position()

pyautogui.hotkey('ctrl', 'tab')
