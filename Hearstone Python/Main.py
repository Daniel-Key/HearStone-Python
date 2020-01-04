import API
import GameState
import MyLogParser
import VoiceRecognition
import MouseControl
import VoiceCommands
import Instance
import keyboard

# from hslog import LogParser

# logParser.checkForLogFileUpdates()
# print(voiceRecognition.recognise())
# mouseControl.click(100, 100)
# mouseControl.clickFraction(0.1, 0.1)
# voiceCommands.endTurn()

instance = Instance.Instance()

def loop():
    while (VoiceCommands.programRunning): 
        # MyLogParser.checkForLogFileUpdates(instance)

        try:  
            if keyboard.is_pressed(' '): 
                print("check")
                VoiceRecognition.takeInput()
            elif keyboard.is_pressed('q'):
                print("quit")
                break
            else:
                pass
        except:
            print("ERROR- program exiting")
            break
    
    print("Program exiting")

loop()