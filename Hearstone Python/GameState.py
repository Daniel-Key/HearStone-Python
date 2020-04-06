import MyLogParser
import API
import collections
import Minion
import Weapon

def calculateHandCards(instance):
    instance.prevHandCards = instance.handCards.copy()
    instance.handCards.clear()
    tempDict = dict()

    for line in instance.optionList:
        if ((("zone=HAND" in line) or ("zone=DECK" in line)) and not (("error=REQ_NOT_MINION_JUST_PLAYED" in line) or ("error=REQ_YOUR_TURN" in line))):
            zonePos = int(line[line.index("zonePos=") + 8 : line.index("cardId=") - 1])
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            logID = line[line.index("id=") + 3 : line.index("zone=") - 1]

            #If the line doesn't contain the card ID, search the log for it
            if (cardID == ""):
                cardID = MyLogParser.lookupCardID(logID)
                #The zonePos number will also be incorrect so search the log for this too
                zonePos = int(MyLogParser.lookupZonePos(logID))

            if cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[cardID]
            else:
                cardInfo = API.requestCardInfo(cardID)
                instance.cardApiInfo[cardID] = cardInfo

            #Checks that the log ID isn't the last minion played (occurs when a charge minion is played, tag doesn't properly update)
            if str(logID) != str(instance.lastCardPlayedID):
                #Checks that the zonePos isn't zero (occurs when discovering cards on turn)
                if (zonePos == 0):
                    tempDict[20] = cardInfo
                #Checks that the zonePos isn't duplicate (occurs when drawing cards on turn)
                elif ((zonePos-1 in tempDict)) :
                    inPrev = False
                    for prevCard in instance.prevHandCards:
                        if (cardInfo == prevCard):
                            inPrev = True
                    if (inPrev):
                        tempDict[20] = (tempDict[zonePos-1])
                        tempDict[zonePos-1] = cardInfo
                    else:
                        tempDict[20] = cardInfo
                else:
                    tempDict[zonePos-1] = cardInfo

    #Sorting dictionary in order and transferring into list
    instance.handCards.clear()
    sortedHandCards = collections.OrderedDict(sorted(tempDict.items()))
    for i in sortedHandCards:
        instance.handCards.append(sortedHandCards[i])
    
    printHandCards(instance)


def addToMinionsOrWeapons(instance, line, isFriendly):
    cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
    logID = line[line.index("id=") + 3 : line.index("zone=")] 

    if (cardID == ""):
        cardID = MyLogParser.lookupCardID(logID)

    cardInfo = ""
    if cardID in instance.cardApiInfo:
        cardInfo = instance.cardApiInfo[cardID]
    else:
        cardInfo = API.requestCardInfo(cardID)
        instance.cardApiInfo[cardID] = cardInfo

    if("\"type\":\"Minion\"" in cardInfo):
        minion = Minion.Minion(instance, cardID, logID)
        if (isFriendly):
            newMinion = True
            for currentMinion in instance.friendlyMinions:
                if (currentMinion.logID == minion.logID):
                    newMinion = False
            if (newMinion):
                instance.friendlyMinions.append(minion)
        else:
            newMinion = True
            for currentMinion in instance.enemyMinions:
                if (currentMinion.logID == minion.logID):
                    newMinion = False
            if (newMinion):
                instance.enemyMinions.append(minion)
    elif("\"type\":\"Weapon\"" in cardInfo):
        weapon = Weapon.Weapon(instance, cardID, logID)
        if (isFriendly):
            newWeapon = True
            for currentWeapon in instance.friendlyWeapons:
                if (currentWeapon.logID == weapon.logID):
                    newWeapon = False
            if (newWeapon):
                instance.friendlyWeapons.append(weapon)
        else:
            newWeapon = True
            for currentWeapon in instance.enemyWeapons:
                if (currentWeapon.logID == weapon.logID):
                    newWeapon = False
            if (newWeapon):
                instance.enemyWeapons.append(weapon)
    

def printHandCards(instance):
    print("Hand cards: ", end="")
    for cardInfo in instance.handCards:
        card = cardInfo[cardInfo.index("cardId"):]
        print(str(card[card.index("name") + 7 : card.index("cardSet") - 3]) + ", ", end="")
    print(end="\n")
    print("-----------------------------------------------------------------")


def printBoardMinions(instance):
    if len(instance.enemyMinions) > 0 : print("Enemy minions: ", end="")
    for enemyMinion in instance.enemyMinions:
        try:
            cardInfo = ""
            if enemyMinion.cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[enemyMinion.cardID]
            else:
                cardInfo = API.requestCardInfo(enemyMinion.cardID)
                instance.cardApiInfo[enemyMinion.cardID] = cardInfo
            name = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
            print(str(name) + ", ", end="")
        except:
            print("failed enemy minion")
    if len(instance.enemyMinions) > 0 : print(end="\n")
    if len(instance.friendlyMinions) > 0 : print("Friendly minions: ", end="")
    for friendlyMinion in instance.friendlyMinions:
        try:
            cardInfo = ""
            if friendlyMinion.cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[friendlyMinion.cardID]
            else:
                cardInfo = API.requestCardInfo(friendlyMinion.cardID)
                instance.cardApiInfo[friendlyMinion.cardID] = cardInfo
            name = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
            print(str(name) + ", ", end="")
        except:
            print("failed friendly minion")
    if len(instance.friendlyMinions) > 0 : print(end="\n")
    if len(instance.enemyWeapons) > 0 : print("Enemy weapon: ", end="")
    for enemyWeapon in instance.enemyWeapons:
        try:
            cardInfo = ""
            if enemyWeapon.cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[enemyWeapon.cardID]
            else:
                cardInfo = API.requestCardInfo(enemyWeapon.cardID)
                instance.cardApiInfo[enemyWeapon.cardID] = cardInfo
            name = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
            print(str(name) + ", ", end="")
        except:
            print("failed enemy weapon")
    if len(instance.enemyWeapons) > 0 : print(end="\n")
    if len(instance.friendlyWeapons) > 0 : print("Friendly weapon: ", end="")
    for friendlyWeapon in instance.friendlyWeapons:
        try:
            cardInfo = ""
            if friendlyWeapon.cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[friendlyWeapon.cardID]
            else:
                cardInfo = API.requestCardInfo(friendlyWeapon.cardID)
                instance.cardApiInfo[friendlyWeapon.cardID] = cardInfo
            name = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
            print(str(name) + ", ", end="")
        except:
            print("failed friendly weapon")
    # print("Friendly weapons in play: ")
    # print(instance.friendlyWeaponsInPlay)
    if len(instance.friendlyWeapons) > 0 : print(end="\n")


def calculateBoardMinions(instance):
    for line in instance.optionList:
        if ("error=REQ_NOT_MINION_JUST_PLAYED" in line):
            addToMinionsOrWeapons(instance, line, True)
        elif ("zone=PLAY" in line and ("REQ_NOT_EXHAUSTED_ACTIVATE" in line or "error=REQ_ATTACKER_NOT_FROZEN " in line or "error=NONE" in line) and not "zonePos=0" in line and "player=1" in line):
            addToMinionsOrWeapons(instance, line, True)
        elif ("player=2" in line):
            addToMinionsOrWeapons(instance, line, False)
        elif ("type=END_TURN" not in line):
            logID = int(line[line.index("id=") + 3 : line.index("zone=") - 1])
            if (logID == instance.lastCardPlayedID):
                addToMinionsOrWeapons(instance, line, True)
        
        if ("cardId=HERO" in line and "player=1" in line and not "REQ_ATTACK_GREATER_THAN_0" in line):
            if len(instance.friendlyWeaponsInPlay) != 0:
                instance.friendlyWeapons.append(instance.friendlyWeaponsInPlay[0])

    printBoardMinions(instance)

def getHandSize(instance):
    return len(instance.handCards)
