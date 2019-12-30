import API
import GameState
import LogParser
import VoiceRecognition
import MouseControl
import VoiceCommands
import Instance
import keyboard

# logParser.checkForLogFileUpdates()
# print(voiceRecognition.recognise())
# mouseControl.click(100, 100)
# mouseControl.clickFraction(0.1, 0.1)
# voiceCommands.endTurn()

instance = Instance.Instance()

def loop():
    while (VoiceCommands.programRunning): 
        LogParser.checkForLogFileUpdates(instance)

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

        

    