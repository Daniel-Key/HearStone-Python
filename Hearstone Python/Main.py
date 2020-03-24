import API
import GameState
import MyLogParser
import VoiceRecognition
import MouseControl
import VoiceCommands
import Instance
import AudioOut
import keyboard

# hslog stuff
# from datetime import datetime, time, timedelta
# from io import StringIO
# from aniso8601 import parse_datetime
# from hearthstone.enums import (
# 	CardType, ChoiceType, GameTag, OptionType,
# 	PlayReq, PlayState, PowerType, State, Step, Zone
# )
# from hslog import LogParser, packets
# from hslog.exceptions import ParsingError
# from hslog.parser import parse_initial_tag

# logParser.checkForLogFileUpdates()
# print(voiceRecognition.recognise())
# mouseControl.click(100, 100)
# mouseControl.clickFraction(0.1, 0.1)
# voiceCommands.endTurn()

# Enter virtual environment: .\env\Scripts\activate

instance = Instance.Instance()
try:
    open(MyLogParser.path)
except:
    open(MyLogParser.path, "x")
inputReady = False

def loop(): 
    global inputReady
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
            break
    
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