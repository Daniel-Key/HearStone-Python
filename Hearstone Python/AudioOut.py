from playsound import playsound
import time
import threading

# Play a short 'bing' sound
def bing():
    playsound('./Sounds/bing.wav')

def baBing():
    playsound('./Sounds/baBing.wav')

def bingThreaded():
    bingThread = threading.Thread(target=bing, args=(), daemon=True)
    bingThread.start()

def baBingThreaded():
    baBingThread = threading.Thread(target=baBing, args=(), daemon=True)
    baBingThread.start()

