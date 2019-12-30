import MouseControl
import time

programRunning = True

#
# General commands
#

def quitProgram():
    VoiceCommands.programRunning = False

# 
# Game commands
#

def endTurn():
    MouseControl.clickFraction(0.82, 0.45)

# 
# Menu commands
#

# Navigate to the single player hero selection screen
def singlePlayer():
    MouseControl.clickFraction(0.5, 0.35)

def selectDifficulty(difficulty):
    if (difficulty == "normal"):
        MouseControl.clickFraction(0.75, 0.2)
    else:
        MouseControl.clickFraction(0.75, 0.27)
    time.sleep(0.1)
    MouseControl.clickFraction(0.75, 0.85)
    time.sleep(1)

# Select deck
def selectDeck(number):
    if (number == 1):
        MouseControl.clickFraction(0.25, 0.25)
    elif (number == 2):
        MouseControl.clickFraction(0.4, 0.25)
    elif (number == 3):
        MouseControl.clickFraction(0.5, 0.25)
    elif (number == 4):
        MouseControl.clickFraction(0.25, 0.45)
    elif (number == 5):
        MouseControl.clickFraction(0.4, 0.45)
    elif (number == 6):
        MouseControl.clickFraction(0.5, 0.45)
    elif (number == 7):
        MouseControl.clickFraction(0.25, 0.7)
    elif (number == 8):
        MouseControl.clickFraction(0.4, 0.7)
    elif (number == 9):
        MouseControl.clickFraction(0.5, 0.7)
        time.sleep(0.1)
        
    MouseControl.clickFraction(0.75, 0.85)
        

# Select enemy
def selectOpponent(number):
    if (number == 1):
        MouseControl.clickFraction(0.75, 0.1)
    elif (number == 2):
        MouseControl.clickFraction(0.75, 0.18)
    elif (number == 3):
        MouseControl.clickFraction(0.75, 0.23)
    elif (number == 4):
        MouseControl.clickFraction(0.75, 0.28)
    elif (number == 5):
        MouseControl.clickFraction(0.75, 0.35)
    elif (number == 6):
        MouseControl.clickFraction(0.75, 0.42)
    elif (number == 7):
        MouseControl.clickFraction(0.75, 0.50)
    elif (number == 8):
        MouseControl.clickFraction(0.75, 0.55)
    elif (number == 9):
        MouseControl.clickFraction(0.75, 0.62)


# Play game
def playGame():
    MouseControl.clickFraction(0.75, 0.85)