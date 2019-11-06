import pyautogui
import pywintypes
import win32gui
import re
import ctypes
import time

#From https://stackoverflow.com/questions/2090464/python-window-activation, will edit for own use later
class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)

    def set_foreground(self):
        """put the window in the foreground"""
        win32gui.SetForegroundWindow(self._handle)
        win32gui.SetActiveWindow(self._handle)


class MouseControl:
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    w = WindowMgr()

    def focusWindow(self):
        self.w.find_window_wildcard(".*Hearthstone.*")
        self.w.set_foreground()
    
    def click(self,x,y):
        pyautogui.click(x, y)
  
    def clickFraction(self,x,y):
        self.focusWindow()
        time.sleep(0.05)
        pyautogui.click(self.screensize[0]*x, self.screensize[1]*y)
