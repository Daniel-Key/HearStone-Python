import pyautogui
import re
import ctypes
import time

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def click(x, y):
    pyautogui.click(x, y)

def clickFraction(x, y):
    pyautogui.click(screensize[0]*x, screensize[1]*y)

def moveToFraction(x, y):
    pyautogui.moveTo(screensize[0]*x, screensize[1]*y, 0.5)

def mouseDownFraction(x, y):
    pyautogui.mouseDown(screensize[0]*x, screensize[1]*y)

def mouseUpFraction(x, y):
    pyautogui.mouseUp(screensize[0]*x, screensize[1]*y)

def moveClickFraction(x, y):
    moveToFraction(x, y)
    clickFraction(x, y)

def moveMouseDownFraction(x, y):
    moveToFraction(x, y)
    mouseDownFraction(x, y)

def moveMouseUpFraction(x, y):
    moveToFraction(x, y)
    mouseUpFraction(x, y)




# pyautogui can't be as specific as reqiured, stutters and stops between commands
# Just going with smooth movement for now

# #Speeds up at start and slows down at end because I'm paranoid
# def moveToFraction(x, y):
#     targetX = screensize[0]*x
#     targetY = screensize[1]*y

#     xDistance = targetX - pyautogui.position().x
#     yDistance = targetY - pyautogui.position().y

#     #3/10s speedup
#     pyautogui.moveTo(pyautogui.position().x + xDistance/28, pyautogui.position().y + yDistance/28, (1/7))
#     pyautogui.moveTo(pyautogui.position().x + xDistance/14, pyautogui.position().y + yDistance/14, (1/7))
#     pyautogui.moveTo(pyautogui.position().x + (3*xDistance)/28, pyautogui.position().y + (3*yDistance)/28, (1/7))

#     #4/10s constant

#     #3/10s slowdown

#     # pyautogui.moveTo(x, y, duration=1)
