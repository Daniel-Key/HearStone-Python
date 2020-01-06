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
    MouseControl.moveClickFraction(0.82, 0.45)

# 
# Menu commands
#

# Navigate to the single player hero selection screen
def singlePlayer():
    MouseControl.moveClickFraction(0.5, 0.35)

def selectDifficulty(difficulty):
    if (difficulty == "normal"):
        MouseControl.moveClickFraction(0.75, 0.2)
    else:
        MouseControl.moveClickFraction(0.75, 0.27)
    time.sleep(0.1)
    MouseControl.moveClickFraction(0.75, 0.85)
    time.sleep(1)

# Select deck
def selectDeck(number):
    if (number == 1):
        MouseControl.moveClickFraction(0.25, 0.25)
        #TO DO: DRAG AND DROP CARD
    elif (number == 2):
        MouseControl.moveClickFraction(0.4, 0.25)
    elif (number == 3):
        MouseControl.moveClickFraction(0.5, 0.25)
    elif (number == 4):
        MouseControl.moveClickFraction(0.25, 0.45)
    elif (number == 5):
        MouseControl.moveClickFraction(0.4, 0.45)
    elif (number == 6):
        MouseControl.moveClickFraction(0.5, 0.45)
    elif (number == 7):
        MouseControl.moveClickFraction(0.25, 0.7)
    elif (number == 8):
        MouseControl.moveClickFraction(0.4, 0.7)
    elif (number == 9):
        MouseControl.moveClickFraction(0.5, 0.7)
        time.sleep(0.1)
        
    MouseControl.moveClickFraction(0.75, 0.85)
        

# Select enemy
def selectOpponent(number):
    if (number == 1):
        MouseControl.moveClickFraction(0.75, 0.1)
    elif (number == 2):
        MouseControl.moveClickFraction(0.75, 0.18)
    elif (number == 3):
        MouseControl.moveClickFraction(0.75, 0.23)
    elif (number == 4):
        MouseControl.moveClickFraction(0.75, 0.28)
    elif (number == 5):
        MouseControl.moveClickFraction(0.75, 0.35)
    elif (number == 6):
        MouseControl.moveClickFraction(0.75, 0.42)
    elif (number == 7):
        MouseControl.moveClickFraction(0.75, 0.50)
    elif (number == 8):
        MouseControl.moveClickFraction(0.75, 0.55)
    elif (number == 9):
        MouseControl.moveClickFraction(0.75, 0.62)


# Play game
def playGame():
    MouseControl.moveClickFraction(0.75, 0.85)

def playCardMouseFraction(x, y):
    MouseControl.moveMouseDownFraction(x, y)
    MouseControl.moveMouseUpFraction(0.5, 0.47)

def playCard(instance, number):
    if ((number > 10) or (number > len(instance.handCards))):
        print("Invalid card to play")
    elif (len(instance.handCards) == 1):
        if (number == 1):
            playCardMouseFraction(0.48, 0.93)
    elif (len(instance.handCards) == 2):
        if (number == 1):
            playCardMouseFraction(0.45, 0.93)
        if (number == 2):
            playCardMouseFraction(0.52, 0.93)
    elif (len(instance.handCards) == 3):
        if (number == 1):
            playCardMouseFraction(0.41, 0.93)
        if (number == 2):
            playCardMouseFraction(0.48, 0.93)
        if (number == 3):
            playCardMouseFraction(0.55, 0.93)
    elif (len(instance.handCards) == 4):
        if (number == 1):
            playCardMouseFraction(0.38, 0.93)
        if (number == 2):
            playCardMouseFraction(0.45, 0.93)
        if (number == 3):
            playCardMouseFraction(0.51, 0.93)
        if (number == 4):
            playCardMouseFraction(0.58, 0.93)
    elif (len(instance.handCards) == 5):
        if (number == 1):
            playCardMouseFraction(0.37, 0.93)
        if (number == 2):
            playCardMouseFraction(0.43, 0.93)
        if (number == 3):
            playCardMouseFraction(0.48, 0.93)
        if (number == 4):
            playCardMouseFraction(0.54, 0.93)
        if (number == 5):
            playCardMouseFraction(0.59, 0.93)
    elif (len(instance.handCards) == 6):
        if (number == 1):
            playCardMouseFraction(0.36, 0.93)
        if (number == 2):
            playCardMouseFraction(0.40, 0.93)
        if (number == 3):
            playCardMouseFraction(0.44, 0.93)
        if (number == 4):
            playCardMouseFraction(0.50, 0.93)
        if (number == 5):
            playCardMouseFraction(0.55, 0.93)
        if (number == 6):
            playCardMouseFraction(0.60, 0.93)
    elif (len(instance.handCards) == 7):
        if (number == 1):
            playCardMouseFraction(0.34, 0.93)
        if (number == 2):
            playCardMouseFraction(0.39, 0.93)
        if (number == 3):
            playCardMouseFraction(0.44, 0.93)
        if (number == 4):
            playCardMouseFraction(0.48, 0.93)
        if (number == 5):
            playCardMouseFraction(0.53, 0.93)
        if (number == 6):
            playCardMouseFraction(0.56, 0.93)
        if (number == 7):
            playCardMouseFraction(0.60, 0.93)
    elif (len(instance.handCards) == 8):
        if (number == 1):
            playCardMouseFraction(0.34, 0.93)
        if (number == 2):
            playCardMouseFraction(0.38, 0.93)
        if (number == 3):
            playCardMouseFraction(0.42, 0.93)
        if (number == 4):
            playCardMouseFraction(0.46, 0.93)
        if (number == 5):
            playCardMouseFraction(0.49, 0.93)
        if (number == 6):
            playCardMouseFraction(0.54, 0.93)
        if (number == 7):
            playCardMouseFraction(0.57, 0.93)
        if (number == 8):
            playCardMouseFraction(0.61, 0.93)
    elif (len(instance.handCards) == 9):
        if (number == 1):
            playCardMouseFraction(0.33, 0.93)
        if (number == 2):
            playCardMouseFraction(0.38, 0.93)
        if (number == 3):
            playCardMouseFraction(0.41, 0.93)
        if (number == 4):
            playCardMouseFraction(0.44, 0.93)
        if (number == 5):
            playCardMouseFraction(0.47, 0.93)
        if (number == 6):
            playCardMouseFraction(0.51, 0.93)
        if (number == 7):
            playCardMouseFraction(0.55, 0.93)
        if (number == 8):
            playCardMouseFraction(0.58, 0.93)
        if (number == 9):
            playCardMouseFraction(0.62, 0.93)
    elif (len(instance.handCards) == 10):
        if (number == 1):
            playCardMouseFraction(0.33, 0.93)
        if (number == 2):
            playCardMouseFraction(0.36, 0.93)
        if (number == 3):
            playCardMouseFraction(0.39, 0.93)
        if (number == 4):
            playCardMouseFraction(0.42, 0.93)
        if (number == 5):
            playCardMouseFraction(0.45, 0.93)
        if (number == 6):
            playCardMouseFraction(0.49, 0.93)
        if (number == 7):
            playCardMouseFraction(0.52, 0.93)
        if (number == 8):
            playCardMouseFraction(0.55, 0.93)
        if (number == 9):
            playCardMouseFraction(0.58, 0.93)
        if (number == 10):
            playCardMouseFraction(0.62, 0.93)

#Number 0 is face
def attack(instance, friendlyNumber, enemyNumber):
    print("placeholder")
    # if ((number > 10) or (number > len(instance.handCards))):
    #     print("Invalid card to play")
    # elif (len(instance.handCards) == 1):
    #     if (number == 1):
    #         playCardMouseFraction(0.48, 0.93)