import API
import GameState
import LogParser
import VoiceRecognition
import MouseControl
import VoiceCommands
import keyboard

class Main():

    # logParser.checkForLogFileUpdates()
    # print(voiceRecognition.recognise())
    # mouseControl.click(100, 100)
    # mouseControl.clickFraction(0.1, 0.1)
    # voiceCommands.endTurn()

    api = API.API()
    gameState = GameState.GameState()
    logParser = LogParser.LogParser()
    voiceRecognition = VoiceRecognition.VoiceRecognition()
    mouseControl = MouseControl.MouseControl()
    voiceCommands = VoiceCommands.VoiceCommands()

    def loop(self):
        while (self.voiceCommands.programRunning): 
            self.logParser.checkForLogFileUpdates()

            try:  
                if keyboard.is_pressed(' '): 
                    print("check")
                    self.voiceRecognition.takeInput()
                elif keyboard.is_pressed('q'):
                    print("quit")
                    break
                else:
                    pass
            except:
                print("ERROR- program exiting")
                break
        
        print("Program exiting")


main = Main()
main.loop()

        

    