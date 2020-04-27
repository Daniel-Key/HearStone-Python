import API
import GameState
import MyLogParser
import VoiceRecognition
import MouseControl
import VoiceCommands
import Instance
import AudioOut
import keyboard

instance = Instance.Instance()
try:
    open(MyLogParser.path)
except:
    x = open(MyLogParser.path, "x")
    x.close()
    open(MyLogParser.path)
inputReady = False

def loop(): 
    global inputReady
    MyLogParser.checkForGameStart(instance)
    while (instance.programRunning): 
        MyLogParser.checkForLogFileUpdates(instance)
        if not inputReady:
            AudioOut.bingThreaded()
            inputReady = True

        try:
            if keyboard.is_pressed(' '): 
                print("check")
                AudioOut.baBingThreaded()
                VoiceRecognition.takeInput(instance, True)
                inputReady = False
            elif keyboard.is_pressed('\b'): 
                print("check")
                AudioOut.baBingThreaded()
                inputReady = False
                VoiceRecognition.takeInput(instance, False)
            elif keyboard.is_pressed('q'):
                print("quit")
                break
            else:
                pass
        except Exception as e:
            print("Exception: ")
            print(e)
            # break
    
    print("Program exiting")

loop()


# import ctypes
# user32 = ctypes.windll.user32
# screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
# import pyautogui
# print(pyautogui.position().x / screensize[0])
# print(pyautogui.position().y / screensize[1])











# parser = LogParser()
# for line in open("D:/Hearthstone/Logs/Power.log"):
#     parser.read_line(line)
# parser.flush()

# packet_tree = parser.games[0]
# game = packet_tree.export().game