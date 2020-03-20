from playsound import playsound
import time
import threading

# Play a short 'bing' sound
def bing():
    playsound('./Sounds/bing.wav')

def bingThreaded():
    bingThread = threading.Thread(target=bing, args=(), daemon=True)
    bingThread.start()
