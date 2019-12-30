import pyautogui
import re
import ctypes
import time

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def click(x,y):
    pyautogui.click(x, y)

def clickFraction(x,y):
    pyautogui.click(screensize[0]*x, screensize[1]*y)
