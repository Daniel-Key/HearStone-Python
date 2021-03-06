import MouseControl
import API
import time
import re

from gtts import gTTS 
import os
import playsound

#
# General commands
#

def quitProgram(instance):
    instance.programRunning = False

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
    time.sleep(0.1)
    MouseControl.moveClickFraction(0.5, 0.35)

def selectDifficulty(difficulty):
    if (difficulty == "normal"):
        # MouseControl.moveClickFraction(0.73, 0.13)
        MouseControl.moveClickFraction(0.75, 0.2)
    else:
        # MouseControl.moveClickFraction(0.73, 0.13)
        MouseControl.moveClickFraction(0.75, 0.27)
    time.sleep(0.1)
    MouseControl.moveClickFraction(0.75, 0.85)
    time.sleep(1)

# Select from first screen of decks
def prevDecks():
    MouseControl.moveClickFraction(0.15, 0.48)

# Select from second screen of decks
def nextDecks():
    MouseControl.moveClickFraction(0.59, 0.48)

# Select deck
def selectDeck(number):
    if (number == 1):
        MouseControl.moveClickFraction(0.25, 0.25)
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
    elif (number == 10):
        MouseControl.moveClickFraction(0.75, 0.68)


# Play game
def startGame():
    MouseControl.moveClickFraction(0.75, 0.85)

def playCardMouseFraction(x, y, releaseMouse):
    MouseControl.moveMouseDownFraction(x, y)
    if releaseMouse:
        MouseControl.moveMouseUpFraction(0.5, 0.47)

def playCard(instance, number, releaseMouse):
    # for i in instance.handCards:
    #     print(i)
    instance.lastCardPlayed = str(instance.handCards[number-1])
    if ((number > 10) or (number > len(instance.handCards))):
        print("Invalid card to play")
    elif (len(instance.handCards) == 1):
        if (number == 1):
            playCardMouseFraction(0.48, 0.93, releaseMouse)
    elif (len(instance.handCards) == 2):
        if (number == 1):
            playCardMouseFraction(0.45, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.52, 0.93, releaseMouse)
    elif (len(instance.handCards) == 3):
        if (number == 1):
            playCardMouseFraction(0.41, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.48, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.55, 0.93, releaseMouse)
    elif (len(instance.handCards) == 4):
        if (number == 1):
            playCardMouseFraction(0.38, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.45, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.51, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.58, 0.93, releaseMouse)
    elif (len(instance.handCards) == 5):
        if (number == 1):
            playCardMouseFraction(0.37, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.43, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.48, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.54, 0.93, releaseMouse)
        if (number == 5):
            playCardMouseFraction(0.59, 0.93, releaseMouse)
    elif (len(instance.handCards) == 6):
        if (number == 1):
            playCardMouseFraction(0.36, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.40, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.44, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.50, 0.93, releaseMouse)
        if (number == 5):
            playCardMouseFraction(0.55, 0.93, releaseMouse)
        if (number == 6):
            playCardMouseFraction(0.60, 0.93, releaseMouse)
    elif (len(instance.handCards) == 7):
        if (number == 1):
            playCardMouseFraction(0.34, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.39, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.44, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.48, 0.93, releaseMouse)
        if (number == 5):
            playCardMouseFraction(0.53, 0.93, releaseMouse)
        if (number == 6):
            playCardMouseFraction(0.56, 0.93, releaseMouse)
        if (number == 7):
            playCardMouseFraction(0.60, 0.93, releaseMouse)
    elif (len(instance.handCards) == 8):
        if (number == 1):
            playCardMouseFraction(0.34, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.38, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.42, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.46, 0.93, releaseMouse)
        if (number == 5):
            playCardMouseFraction(0.49, 0.93, releaseMouse)
        if (number == 6):
            playCardMouseFraction(0.54, 0.93, releaseMouse)
        if (number == 7):
            playCardMouseFraction(0.57, 0.93, releaseMouse)
        if (number == 8):
            playCardMouseFraction(0.61, 0.93, releaseMouse)
    elif (len(instance.handCards) == 9):
        if (number == 1):
            playCardMouseFraction(0.33, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.38, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.41, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.44, 0.93, releaseMouse)
        if (number == 5):
            playCardMouseFraction(0.47, 0.93, releaseMouse)
        if (number == 6):
            playCardMouseFraction(0.51, 0.93, releaseMouse)
        if (number == 7):
            playCardMouseFraction(0.55, 0.93, releaseMouse)
        if (number == 8):
            playCardMouseFraction(0.58, 0.93, releaseMouse)
        if (number == 9):
            playCardMouseFraction(0.62, 0.93, releaseMouse)
    elif (len(instance.handCards) == 10):
        if (number == 1):
            playCardMouseFraction(0.33, 0.93, releaseMouse)
        if (number == 2):
            playCardMouseFraction(0.36, 0.93, releaseMouse)
        if (number == 3):
            playCardMouseFraction(0.39, 0.93, releaseMouse)
        if (number == 4):
            playCardMouseFraction(0.42, 0.93, releaseMouse)
        if (number == 5):
            playCardMouseFraction(0.45, 0.93, releaseMouse)
        if (number == 6):
            playCardMouseFraction(0.49, 0.93, releaseMouse)
        if (number == 7):
            playCardMouseFraction(0.52, 0.93, releaseMouse)
        if (number == 8):
            playCardMouseFraction(0.55, 0.93, releaseMouse)
        if (number == 9):
            playCardMouseFraction(0.58, 0.93, releaseMouse)
        if (number == 10):
            playCardMouseFraction(0.62, 0.93, releaseMouse)


def playCardToPosition(instance, cardNumber, positionNumber):
    playCard(instance, cardNumber, False)
    if ((positionNumber > 7) or (positionNumber > (len(instance.friendlyMinions)+1))):
        print("Invalid minion position")
    elif(len(instance.friendlyMinions) == 7):
        print("Max number of friendly minions on board")
    else:
        #Friendly minion positions  
        if (len(instance.friendlyMinions) == 0):
            if (positionNumber == 1):
                x1 = 0.5
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 1):
            if (positionNumber == 1):
                x1 = 0.47
                y1 = 0.55
            elif (positionNumber == 2):
                x1 = 0.54
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 2):
            if (positionNumber == 1):
                x1 = 0.43
                y1 = 0.55
            elif (positionNumber == 2):
                x1 = 0.5
                y1 = 0.55
            elif (positionNumber == 3):
                x1 = 0.58
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 3):
            if (positionNumber == 1):
                x1 = 0.39
                y1 = 0.55
            elif (positionNumber == 2):
                x1 = 0.47
                y1 = 0.55
            elif (positionNumber == 3):
                x1 = 0.54
                y1 = 0.55
            elif (positionNumber == 4):
                x1 = 0.61
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 4):
            if (positionNumber == 1):
                x1 = 0.36
                y1 = 0.55
            elif (positionNumber == 2):
                x1 = 0.43
                y1 = 0.55
            elif (positionNumber == 3):
                x1 = 0.5
                y1 = 0.55
            elif (positionNumber == 4):
                x1 = 0.58
                y1 = 0.55
            elif (positionNumber == 5):
                x1 = 0.65
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 5):
            if (positionNumber == 1):
                x1 = 0.32
                y1 = 0.55
            elif (positionNumber == 2):
                x1 = 0.39
                y1 = 0.55
            elif (positionNumber == 3):
                x1 = 0.47
                y1 = 0.55
            elif (positionNumber == 4):
                x1 = 0.54
                y1 = 0.55
            elif (positionNumber == 5):
                x1 = 0.61
                y1 = 0.55
            elif (positionNumber == 6):
                x1 = 0.68
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 6):
            if (positionNumber == 1):
                x1 = 0.28
                y1 = 0.55
            elif (positionNumber == 2):
                x1 = 0.36
                y1 = 0.55
            elif (positionNumber == 3):
                x1 = 0.43
                y1 = 0.55
            elif (positionNumber == 4):
                x1 = 0.5
                y1 = 0.55
            elif (positionNumber == 5):
                x1 = 0.58
                y1 = 0.55
            elif (positionNumber == 6):
                x1 = 0.65
                y1 = 0.55
            elif (positionNumber == 7):
                x1 = 0.72
                y1 = 0.55
        MouseControl.mouseDownFraction(x1, y1)
        MouseControl.mouseUpFraction(x1, y1)


def makeAttackMouseFraction(x1, y1, x2, y2):
    MouseControl.moveMouseDownFraction(x1, y1)
    MouseControl.moveMouseUpFraction(x2, y2)  


#Number 0 is face
def attack(instance, friendlyNumber, enemyNumber):
    x1 = -1
    y1 = -1
    x2 = -1
    y2 = -1

    if ((friendlyNumber > 7) or (friendlyNumber > len(instance.friendlyMinions))):
        print("Invalid friendly minion")
    elif ((enemyNumber > 7) or (enemyNumber > len(instance.enemyMinions))):
        print("Invalid enemy minion")
    else:
        #Friendly minion positions
        if (len(instance.friendlyMinions) == 0):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
        elif (len(instance.friendlyMinions) == 1):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.5
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 2):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.47
                y1 = 0.55
            elif (friendlyNumber == 2):
                x1 = 0.54
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 3):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.43
                y1 = 0.55
            elif (friendlyNumber == 2):
                x1 = 0.5
                y1 = 0.55
            elif (friendlyNumber == 3):
                x1 = 0.58
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 4):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.39
                y1 = 0.55
            elif (friendlyNumber == 2):
                x1 = 0.47
                y1 = 0.55
            elif (friendlyNumber == 3):
                x1 = 0.54
                y1 = 0.55
            elif (friendlyNumber == 4):
                x1 = 0.61
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 5):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.36
                y1 = 0.55
            elif (friendlyNumber == 2):
                x1 = 0.43
                y1 = 0.55
            elif (friendlyNumber == 3):
                x1 = 0.5
                y1 = 0.55
            elif (friendlyNumber == 4):
                x1 = 0.58
                y1 = 0.55
            elif (friendlyNumber == 5):
                x1 = 0.65
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 6):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.32
                y1 = 0.55
            elif (friendlyNumber == 2):
                x1 = 0.39
                y1 = 0.55
            elif (friendlyNumber == 3):
                x1 = 0.47
                y1 = 0.55
            elif (friendlyNumber == 4):
                x1 = 0.54
                y1 = 0.55
            elif (friendlyNumber == 5):
                x1 = 0.61
                y1 = 0.55
            elif (friendlyNumber == 6):
                x1 = 0.68
                y1 = 0.55
        elif (len(instance.friendlyMinions) == 7):
            if (friendlyNumber == 0):
                x1 = 0.5
                y1 = 0.75
            elif (friendlyNumber == 1):
                x1 = 0.28
                y1 = 0.55
            elif (friendlyNumber == 2):
                x1 = 0.36
                y1 = 0.55
            elif (friendlyNumber == 3):
                x1 = 0.43
                y1 = 0.55
            elif (friendlyNumber == 4):
                x1 = 0.5
                y1 = 0.55
            elif (friendlyNumber == 5):
                x1 = 0.58
                y1 = 0.55
            elif (friendlyNumber == 6):
                x1 = 0.65
                y1 = 0.55
            elif (friendlyNumber == 7):
                x1 = 0.72
                y1 = 0.55

        #Enemy minion positions
        if (len(instance.enemyMinions) == 0):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
        elif (len(instance.enemyMinions) == 1):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.5
                y2 = 0.38
        elif (len(instance.enemyMinions) == 2):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.47
                y2 = 0.38
            elif (enemyNumber == 2):
                x2 = 0.54
                y2 = 0.38
        elif (len(instance.enemyMinions) == 3):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.43
                y2 = 0.38
            elif (enemyNumber == 2):
                x2 = 0.5
                y2 = 0.38
            elif (enemyNumber == 3):
                x2 = 0.58
                y2 = 0.38
        elif (len(instance.enemyMinions) == 4):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.39
                y2 = 0.38
            elif (enemyNumber == 2):
                x2 = 0.47
                y2 = 0.38
            elif (enemyNumber == 3):
                x2 = 0.54
                y2 = 0.38
            elif (enemyNumber == 4):
                x2 = 0.61
                y2 = 0.38
        elif (len(instance.enemyMinions) == 5):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.36
                y2 = 0.38
            elif (enemyNumber == 2):
                x2 = 0.43
                y2 = 0.38
            elif (enemyNumber == 3):
                x2 = 0.5
                y2 = 0.38
            elif (enemyNumber == 4):
                x2 = 0.58
                y2 = 0.38
            elif (enemyNumber == 5):
                x2 = 0.65
                y2 = 0.38
        elif (len(instance.enemyMinions) == 6):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.32
                y2 = 0.38
            elif (enemyNumber == 2):
                x2 = 0.39
                y2 = 0.38
            elif (enemyNumber == 3):
                x2 = 0.47
                y2 = 0.38
            elif (enemyNumber == 4):
                x2 = 0.54
                y2 = 0.38
            elif (enemyNumber == 5):
                x2 = 0.61
                y2 = 0.38
            elif (enemyNumber == 6):
                x2 = 0.68
                y2 = 0.38
        elif (len(instance.enemyMinions) == 7):
            if (enemyNumber == 0):
                x2 = 0.5
                y2 = 0.19
            elif (enemyNumber == 1):
                x2 = 0.28
                y2 = 0.38
            elif (enemyNumber == 2):
                x2 = 0.36
                y2 = 0.38
            elif (enemyNumber == 3):
                x2 = 0.43
                y2 = 0.38
            elif (enemyNumber == 4):
                x2 = 0.5
                y2 = 0.38
            elif (enemyNumber == 5):
                x2 = 0.58
                y2 = 0.38
            elif (enemyNumber == 6):
                x2 = 0.65
                y2 = 0.38
            elif (enemyNumber == 7):
                x2 = 0.72
                y2 = 0.38

    if (x1 != -1 and y1 != -1 and x2 != -1 and y2 != -1):
        makeAttackMouseFraction(x1, y1, x2, y2)

#TO DO: Make this smart and only attack with available minions?
#FACE!
def face(instance):
    attack(instance, 0, 0)
    for i in range(len(instance.friendlyMinions)):
        attack(instance, i+1, 0)

#Target card
def target(instance, targetNo, friendly):
    if (friendly):
        if ((targetNo > 7) or (targetNo > len(instance.friendlyMinions))):
            print("Invalid friendly minion")
        else:
            actualFriendlyMinionLen = -1
            if ("\"type\":\"Minion\"" in instance.lastCardPlayed):
                actualFriendlyMinionLen = len(instance.friendlyMinions) + 1
            else:
                actualFriendlyMinionLen = len(instance.friendlyMinions)
            x1 = -1
            y1 = -1
            #Friendly minion positions
            if (actualFriendlyMinionLen == 0):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
            elif (actualFriendlyMinionLen == 1):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.5
                    y1 = 0.55
            elif (actualFriendlyMinionLen == 2):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.47
                    y1 = 0.55
                elif (targetNo == 2):
                    x1 = 0.54
                    y1 = 0.55
            elif (actualFriendlyMinionLen == 3):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.43
                    y1 = 0.55
                elif (targetNo == 2):
                    x1 = 0.5
                    y1 = 0.55
                elif (targetNo == 3):
                    x1 = 0.58
                    y1 = 0.55
            elif (actualFriendlyMinionLen == 4):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.39
                    y1 = 0.55
                elif (targetNo == 2):
                    x1 = 0.47
                    y1 = 0.55
                elif (targetNo == 3):
                    x1 = 0.54
                    y1 = 0.55
                elif (targetNo == 4):
                    x1 = 0.61
                    y1 = 0.55
            elif (actualFriendlyMinionLen == 5):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.36
                    y1 = 0.55
                elif (targetNo == 2):
                    x1 = 0.43
                    y1 = 0.55
                elif (targetNo == 3):
                    x1 = 0.5
                    y1 = 0.55
                elif (targetNo == 4):
                    x1 = 0.58
                    y1 = 0.55
                elif (targetNo == 5):
                    x1 = 0.65
                    y1 = 0.55
            elif (actualFriendlyMinionLen == 6):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.32
                    y1 = 0.55
                elif (targetNo == 2):
                    x1 = 0.39
                    y1 = 0.55
                elif (targetNo == 3):
                    x1 = 0.47
                    y1 = 0.55
                elif (targetNo == 4):
                    x1 = 0.54
                    y1 = 0.55
                elif (targetNo == 5):
                    x1 = 0.61
                    y1 = 0.55
                elif (targetNo == 6):
                    x1 = 0.68
                    y1 = 0.55
            elif (actualFriendlyMinionLen == 7):
                if (targetNo == 0):
                    x1 = 0.5
                    y1 = 0.75
                elif (targetNo == 1):
                    x1 = 0.28
                    y1 = 0.55
                elif (targetNo == 2):
                    x1 = 0.36
                    y1 = 0.55
                elif (targetNo == 3):
                    x1 = 0.43
                    y1 = 0.55
                elif (targetNo == 4):
                    x1 = 0.5
                    y1 = 0.55
                elif (targetNo == 5):
                    x1 = 0.58
                    y1 = 0.55
                elif (targetNo == 6):
                    x1 = 0.65
                    y1 = 0.55
                elif (targetNo == 7):
                    x1 = 0.72
                    y1 = 0.55
            
            MouseControl.moveClickFraction(x1, y1)
    else:
        if ((targetNo > 7) or (targetNo > len(instance.enemyMinions))):
            print("Invalid enemy minion")
        else:
            x2 = -1
            y2 = -1
            #Enemy minion positions
        if (len(instance.enemyMinions) == 0):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
        elif (len(instance.enemyMinions) == 1):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.5
                y2 = 0.38
        elif (len(instance.enemyMinions) == 2):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.47
                y2 = 0.38
            elif (targetNo == 2):
                x2 = 0.54
                y2 = 0.38
        elif (len(instance.enemyMinions) == 3):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.43
                y2 = 0.38
            elif (targetNo == 2):
                x2 = 0.5
                y2 = 0.38
            elif (targetNo == 3):
                x2 = 0.58
                y2 = 0.38
        elif (len(instance.enemyMinions) == 4):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.39
                y2 = 0.38
            elif (targetNo == 2):
                x2 = 0.47
                y2 = 0.38
            elif (targetNo == 3):
                x2 = 0.54
                y2 = 0.38
            elif (targetNo == 4):
                x2 = 0.61
                y2 = 0.38
        elif (len(instance.enemyMinions) == 5):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.36
                y2 = 0.38
            elif (targetNo == 2):
                x2 = 0.43
                y2 = 0.38
            elif (targetNo == 3):
                x2 = 0.5
                y2 = 0.38
            elif (targetNo == 4):
                x2 = 0.58
                y2 = 0.38
            elif (targetNo == 5):
                x2 = 0.65
                y2 = 0.38
        elif (len(instance.enemyMinions) == 6):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.32
                y2 = 0.38
            elif (targetNo == 2):
                x2 = 0.39
                y2 = 0.38
            elif (targetNo == 3):
                x2 = 0.47
                y2 = 0.38
            elif (targetNo == 4):
                x2 = 0.54
                y2 = 0.38
            elif (targetNo == 5):
                x2 = 0.61
                y2 = 0.38
            elif (targetNo == 6):
                x2 = 0.68
                y2 = 0.38
        elif (len(instance.enemyMinions) == 7):
            if (targetNo == 0):
                x2 = 0.5
                y2 = 0.19
            elif (targetNo == 1):
                x2 = 0.28
                y2 = 0.38
            elif (targetNo == 2):
                x2 = 0.36
                y2 = 0.38
            elif (targetNo == 3):
                x2 = 0.43
                y2 = 0.38
            elif (targetNo == 4):
                x2 = 0.5
                y2 = 0.38
            elif (targetNo == 5):
                x2 = 0.58
                y2 = 0.38
            elif (targetNo == 6):
                x2 = 0.65
                y2 = 0.38
            elif (targetNo == 7):
                x2 = 0.72
                y2 = 0.38
            
        MouseControl.moveClickFraction(x2, y2)


#Make mulligan choices
def mulligan(instance, cards):
    print(cards)
    if (len(instance.mulliganList) == 3):
        if (1 in cards):
            MouseControl.moveClickFraction(0.32, 0.47)
        if (2 in cards):
            MouseControl.moveClickFraction(0.5, 0.47)
        if (3 in cards):
            MouseControl.moveClickFraction(0.68, 0.47)
    else:
        if (1 in cards):
            MouseControl.moveClickFraction(0.3, 0.47)
        if (2 in cards):
            MouseControl.moveClickFraction(0.44, 0.47)
        if (3 in cards):
            MouseControl.moveClickFraction(0.57, 0.47)
        if (4 in cards):
            MouseControl.moveClickFraction(0.70, 0.47)


#Confirm mulligan choices
def mulliganConfirm():
    MouseControl.moveClickFraction(0.5, 0.79)


#Use hero power
def heroPower():
    MouseControl.moveClickFraction(0.59, 0.75)


#Discover card (only works with 3 currently)
def discover(number):
    #Show/hide options
    if (number == -1):
        MouseControl.moveClickFraction(0.28, 0.76)
    elif (number == 1):
        MouseControl.moveClickFraction(0.29, 0.49)
    elif (number == 2):
        MouseControl.moveClickFraction(0.5, 0.49)
    elif (number == 3):
        MouseControl.moveClickFraction(0.71, 0.49)

#Choose card (from Druid choose one), only works for two currently
def chooseOne(number):
    if (number == 1):
        MouseControl.moveClickFraction(0.37, 0.49)
    elif (number == 2):
        MouseControl.moveClickFraction(0.62, 0.49)

#Cancel targeted card
def cancel():
    MouseControl.rightClick()






#
# Auditory feedback
#

def speakString(instance, line):
    print(line)
    speech = gTTS(text = line, lang = "en", slow = False)
    speech.save("text.mp3")
    playsound.playsound("text.mp3", True)
    os.remove("text.mp3")

def speakCardName(instance, line):
    name = line[line.index("\"name\":\"") + 8: line.index("\",\"cardSet")]
    speakString(instance, name)

def speakCardStats(instance, line, statsToSpeak):
    cardType = "" 
    try:
        cardType = line[line.index("\"type\":\"") + 8: line.index("\",\"faction")]
    except:
        None
    if (cardType == ""):
        try:
            cardType = line[line.index("\"type\":\"") + 8: line.index("\",\"rarity")]
        except:
            None
    if (cardType == ""):
        try:
            cardType = line[line.index("\"type\":\"") + 8: line.index("\",\"cost")]
        except:
            None

    # If card is a minion, speak cost, attack and health
    if cardType == "Minion":
        statsString = ""
        if ("cost" in statsToSpeak):
            cost = line[line.index("\"cost\":") + 7: line.index(",\"attack")]
            costString = str(", cost " + cost)
            statsString += costString
        if ("attack" in statsToSpeak):
            attack = line[line.index("\"attack\":") + 9: line.index(",\"health")]
            attackString = str(", attack " + attack)
            statsString += attackString
        if ("health" in statsToSpeak):
            try:
                health = line[line.index("\"health\":") + 9: line.index(",\"text")]
            except:
                health = line[line.index("\"health\":") + 9: line.index(",\"flavor")]
            healthString = str(", health " + health)
            statsString += healthString
        if (statsString != ""):
            speakString(instance, statsString)
        else:
            print("Invalid statistic(s) to speak for minion")
   
    # If card is a spell, speak cost
    elif cardType == "Spell":
        statsString = ""
        if ("cost" in statsToSpeak):
            cost = line[line.index("\"cost\":") + 7: line.index(",\"text")]
            statsString = str("cost " + cost)
            speakString(instance, statsString)
        else:
            print("Invalid statistic(s) to speak for spell")
    # If card is a weapon, speak cost, attack and durability
    elif cardType == "Weapon":
        statsString = ""
        if ("cost" in statsToSpeak):
            cost = line[line.index("\"cost\":") + 7: line.index(",\"attack")]
            costString = str(", cost " + cost)
            statsString += costString
        if ("attack" in statsToSpeak):
            attack = line[line.index("\"attack\":") + 9: line.index(",\"durability")]
            attackString = str(", attack " + attack)
            statsString += attackString
        if ("durability" in statsToSpeak):
            durability = ""
            try:
                durability = line[line.index("\"durability\":") + 13: line.index(",\"text")]
            except:
                durability = line[line.index("\"durability\":") + 13: line.index(",\"playerClass")]
            durabilityString = str(", durability " + durability)
            statsString += durabilityString
        if (statsString != ""):
            speakString(instance, statsString)
        else:
            print("Invalid statistic(s) to speak for weapon")


def speakCardText(instance, line):
    text = ""
    try:
        text = line[line.index("\"text\":\"") + 8: line.index("\",\"flavor")]
    except:
        speakString(instance, "None")
        print("Card does not have any text")
    text = re.sub('<[^>]+>', '', text)
    text = re.sub('\[[^>]+\]', '', text)
    text = text.replace('$', '')
    text = text.replace('_', ' ')
    text = text.replace('/', ' ')
    text = text.replace('\\n', ' ')
    text = text.replace('\\', '')
    if (text != ""):
        speakString(instance, text)


def speakAllHandCards(instance):
    stringToSpeak = ""
    for line in instance.handCards:
        name = line[line.index("\"name\":\"") + 8: line.index("\",\"cardSet")]
        stringToSpeak += name
        stringToSpeak += ", "
    speakString(instance, stringToSpeak)

def speakBoardMinion(instance, isFriendly, number, speak):
    minion = "" 
    if isFriendly == True:
        minion = instance.friendlyMinions[number-1]
    else:
        minion = instance.enemyMinions[number-1]
    cardID = minion.cardID
    cardInfo = ""

    if cardID in instance.cardApiInfo:
        cardInfo = instance.cardApiInfo[cardID]
    else:
        cardInfo = API.requestCardInfo(cardID)
        instance.cardApiInfo[cardID] = cardInfo
    
    speechString = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
    speechString += (", attack: " + str(minion.attack))
    speechString += (", health: " + str(minion.currentHealth))
    if (speak):
        speakString(instance, speechString)
    else:
        speechString += ", "
        return speechString

def speakAllBoardMinions(instance):
    speechString = ""
    speechString += "Friendly minions: "
    if (len(instance.friendlyMinions) == 0):
        speechString += "None "
    for i in range(len(instance.friendlyMinions)):
        speechString += speakBoardMinion(instance, True, i, False)
        
    speechString += "Enemy minions: "
    if (len(instance.enemyMinions) == 0):
        speechString += "None "
    for i in range(len(instance.enemyMinions)):
        speechString += speakBoardMinion(instance, False, i, False)

    speakString(instance, speechString)

def speakFriendlyWeapon(instance):
    if len(instance.friendlyWeapons) == 0:
        speakString(instance, "No friendly weapon")
    else:
        weapon = instance.friendlyWeapons[0]
        cardID = weapon.cardID
        cardInfo = ""

        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo
        
        speechString = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
        speechString += (", attack: " + weapon.attack)
        speechString += (", durability: " + weapon.durability)
        speakString(instance, speechString)
        
def speakEnemyWeapon(instance):
    if len(instance.enemyWeapons) == 0:
        speakString(instance, "No enemy weapon")
    else:
        weapon = instance.enemyWeapons[0]
        cardID = weapon.cardID
        cardInfo = ""

        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo
        
        speechString = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
        speechString += (", attack: " + str(weapon.attack))
        speechString += (", durability: " + str(weapon.durability))
        speakString(instance, speechString)

def speakHandOptions(instance):
    print(instance.handCards)