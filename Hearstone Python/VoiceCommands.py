import MouseControl
import API
import time

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

def selectDifficulty(difficulty):
    if (difficulty == "normal"):
        MouseControl.moveClickFraction(0.75, 0.2)
    else:
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


# Play game
def startGame():
    MouseControl.moveClickFraction(0.75, 0.85)

def playCardMouseFraction(x, y):
    MouseControl.moveMouseDownFraction(x, y)
    MouseControl.moveMouseUpFraction(0.5, 0.47)

def playCard(instance, number):
    # for i in instance.handCards:
    #     print(i)
    instance.lastCardPlayed = str(instance.handCards[number-1])
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


def playCardToPositionMouseFraction(x1, y1, x2, y2):
    MouseControl.moveMouseDownFraction(x1, y1)
    MouseControl.moveMouseUpFraction(x2, y2)


def playCardToPosition(instance, cardNumber, positionNumber):
    largechunkoftext = 1


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

def speakAllHandCards(instance):
    for i in instance.handCards:
        line = instance.handCards[i]
        speakCardName(instance, line)

def speakFriendlyBoardMinion(instance, number):
    cardID = instance.friendlyMinions[number-1]
    cardInfo = ""

    if cardID in instance.cardApiInfo:
        cardInfo = instance.cardApiInfo[cardID]
    else:
        cardInfo = API.requestCardInfo(cardID)
        instance.cardApiInfo[cardID] = cardInfo

    speakCardName(instance, cardInfo)

def speakEnemyBoardMinion(instance, number):
    cardID = instance.enemyMinions[number-1]
    cardInfo = ""

    if cardID in instance.cardApiInfo:
        cardInfo = instance.cardApiInfo[cardID]
    else:
        cardInfo = API.requestCardInfo(cardID)
        instance.cardApiInfo[cardID] = cardInfo

    speakCardName(instance, cardInfo)

def speakAllBoardMinions(instance):
    speakString(instance, "Friendly minions")
    for i in range(len(instance.friendlyMinions)):
        cardID = instance.friendlyMinions[i]
        cardInfo = ""

        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        speakCardName(instance, cardInfo)
        
    speakString(instance, "Enemy minions")
    for i in range(len(instance.enemyMinions)):
        cardID = instance.enemyMinions[i]
        cardInfo = ""

        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        speakCardName(instance, cardInfo)
