import API
import GameState
import LogParser
import VoiceRecognition
import MouseControl
import VoiceCommands

class Main:
    api = API.API()
    gameState = GameState.GameState()
    logParser = LogParser.LogParser()
    voiceRecognition = VoiceRecognition.VoiceRecognition()
    mouseControl = MouseControl.MouseControl()
    voiceCommands = VoiceCommands.VoiceCommands()
    # logParser.checkForLogFileUpdates()
    # print(voiceRecognition.recognise())
    # mouseControl.click(100, 100)
    # mouseControl.clickFraction(0.1, 0.1)
    # voiceCommands.endTurn()
    while (True):
        test = voiceRecognition.recognise()
        print("tick")
        if (test == "end turn" or test == "and turn" or test == "entertain"):
            voiceCommands.endTurn()
        else:
            print(test)