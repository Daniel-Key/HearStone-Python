import MouseControl
import time

class VoiceCommands:

    programRunning = True
    mouseControl = MouseControl.MouseControl()

    #
    # General commands
    #

    def quitProgram(self):
        #Python globals are broken on a whole new level of broken
        VoiceCommands.programRunning = False
    
    # 
    # Game commands
    #

    def endTurn(self):
        self.mouseControl.clickFraction(0.82, 0.45)

    # 
    # Menu commands
    #

    # Navigate to the single player hero selection screen
    def singlePlayer(self):
        self.mouseControl.clickFraction(0.5, 0.35)

    def selectDifficulty(self, difficulty):
        if (difficulty == "normal"):
            self.mouseControl.clickFraction(0.75, 0.2)
        else:
            self.mouseControl.clickFraction(0.75, 0.27)
        time.sleep(0.1)
        self.mouseControl.clickFraction(0.75, 0.85)
        time.sleep(1)

    # Select deck
    def selectDeck(self, number):
        if (number == 1):
            self.mouseControl.clickFraction(0.25, 0.25)
        elif (number == 2):
            self.mouseControl.clickFraction(0.4, 0.25)
        elif (number == 3):
            self.mouseControl.clickFraction(0.5, 0.25)
        elif (number == 4):
            self.mouseControl.clickFraction(0.25, 0.45)
        elif (number == 5):
            self.mouseControl.clickFraction(0.4, 0.45)
        elif (number == 6):
            self.mouseControl.clickFraction(0.5, 0.45)
        elif (number == 7):
            self.mouseControl.clickFraction(0.25, 0.7)
        elif (number == 8):
            self.mouseControl.clickFraction(0.4, 0.7)
        elif (number == 9):
            self.mouseControl.clickFraction(0.5, 0.7)
            time.sleep(0.1)
            
        self.mouseControl.clickFraction(0.75, 0.85)
            

    # Select enemy
    def selectOpponent(self, number):
        if (number == 1):
            self.mouseControl.clickFraction(0.75, 0.1)
        elif (number == 2):
            self.mouseControl.clickFraction(0.75, 0.18)
        elif (number == 3):
            self.mouseControl.clickFraction(0.75, 0.23)
        elif (number == 4):
            self.mouseControl.clickFraction(0.75, 0.28)
        elif (number == 5):
            self.mouseControl.clickFraction(0.75, 0.35)
        elif (number == 6):
            self.mouseControl.clickFraction(0.75, 0.42)
        elif (number == 7):
            self.mouseControl.clickFraction(0.75, 0.50)
        elif (number == 8):
            self.mouseControl.clickFraction(0.75, 0.55)
        elif (number == 9):
            self.mouseControl.clickFraction(0.75, 0.62)


    # Play game
    def playGame(self):
        self.mouseControl.clickFraction(0.75, 0.85)