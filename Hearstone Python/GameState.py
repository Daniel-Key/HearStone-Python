import MyLogParser
import API
import collections
import Minion

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
    
    # for cardInfo in instance.handCards:
    #     card = cardInfo[cardInfo.index("cardId"):]
    #     print(card[card.index("name") + 7 : card.index("cardSet") - 3])
    # print()


def calculateBoardMinions(instance):
    instance.friendlyMinions.clear()
    instance.enemyMinions.clear()
    for line in instance.optionList:
        if ("error=REQ_NOT_MINION_JUST_PLAYED" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            logID = line[line.index("id=") + 3 : line.index("zone=")]
            if (cardID == ""):
                cardID = MyLogParser.lookupCardID(logID)
            minion = Minion.Minion(cardID, logID)
            instance.friendlyMinions.append(minion)
        elif ("zone=PLAY" in line and ("REQ_NOT_EXHAUSTED_ACTIVATE" in line or "error=REQ_ATTACKER_NOT_FROZEN " in line or "error=NONE" in line) and not "zonePos=0" in line and "player=1" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            logID = line[line.index("id=") + 3 : line.index("zone=")]
            if (cardID == ""):
                cardID = MyLogParser.lookupCardID(logID)
            minion = Minion.Minion(cardID, logID)
            instance.friendlyMinions.append(minion)
        elif ("zonePos=0" not in line and "player=2" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            logID = line[line.index("id=") + 3 : line.index("zone=")]
            if (cardID == ""):
                cardID = MyLogParser.lookupCardID(logID)
            minion = Minion.Minion(cardID, logID)
            instance.friendlyMinions.append(minion)
        elif ("type=END_TURN" not in line):
            logID = int(line[line.index("id=") + 3 : line.index("zone=") - 1])
            if (logID == instance.lastCardPlayedID):
                cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
                if (cardID == ""):
                    cardID = MyLogParser.lookupCardID(logID)
                minion = Minion.Minion(cardID, logID)
                instance.friendlyMinions.append(minion)
   
    for enemyMinion in instance.enemyMinions:
        try:
            cardInfo = instance.cardApiInfo[enemyMinion.cardID]
            name = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
            print(name)
        except:
            print("rip")
    for friendlyMinion in instance.friendlyMinions:
        try:
            cardInfo = instance.cardApiInfo[friendlyMinion.cardID]
            name = cardInfo[cardInfo.index("\"name\":\"") + 8: cardInfo.index("\",\"cardSet")]
            print(name)
        except:
            print("rip")
        
    # print(instance.enemyMinions)
    # print(instance.friendlyMinions)
    # print()

def getHandSize(instance):
    return len(instance.handCards)
    
    
# TO DO: Look a bit more into existing log parser, could save some time