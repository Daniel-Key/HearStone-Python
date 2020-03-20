import MyLogParser
import API

def calculateHandCards(instance):
    instance.prevHandCards = instance.handCards.copy()
    instance.handCards.clear()

    for line in instance.optionList:
        if ((("zone=HAND" in line) or ("zone=DECK" in line)) and not (("error=REQ_NOT_MINION_JUST_PLAYED" in line) or ("error=REQ_YOUR_TURN" in line))):
            zonePos = int(line[line.index("zonePos=") + 8 : line.index("cardId=") - 1])
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            
            #If the line doesn't contain the card ID, search the log for it
            if (cardID == ""):
                logID = line[line.index("id=") : line.index("zone=")]
                cardID = MyLogParser.lookupCardID(logID)
                #The zonePos number will also be incorrect so search the log for this too
                zonePos = int(MyLogParser.lookupZonePos(logID))

            if cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[cardID]
            else:
                cardInfo = API.requestCardInfo(cardID)
                instance.cardApiInfo[cardID] = cardInfo

            #Checks that the cardID isn't in the friendly board minions (occurs when a chard minion is played, tag doesn't properly update)
            if cardID not in instance.friendlyMinions:
                #Checks that the zonePos isn't duplicate (occurs when drawing cards on turn), if it is adds the new card to the end
                if ((zonePos-1 in instance.handCards) and (zonePos != 0)) :
                    inPrev = False
                    for prevCard in instance.prevHandCards:
                        if (cardInfo == instance.prevHandCards[prevCard]):
                            inPrev = True
                    if (inPrev):
                        instance.handCards[len(instance.handCards)] = instance.handCards[zonePos-1]
                        instance.handCards[zonePos-1] = cardInfo
                    else:
                        instance.handCards[len(instance.handCards)] = cardInfo
                else:
                    instance.handCards[zonePos - 1] = cardInfo

    #Sorting dictionary in order
    tempHandCards = {}
    sortedHandCards = sorted(instance.handCards)
    for i in sortedHandCards:
        tempHandCards[i] = instance.handCards[i]
    instance.handCards = tempHandCards
    
    for i in instance.handCards:
        cardInfo = instance.handCards[i]
        card = cardInfo[cardInfo.index("cardId"):]
        print(card[card.index("name") + 7 : card.index("cardSet") - 3])
    print()


def calculateBoardMinions(instance):
    instance.friendlyMinions.clear()
    instance.enemyMinions.clear()
    for line in instance.optionList:
        if ("error=REQ_NOT_MINION_JUST_PLAYED" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            instance.friendlyMinions.append(cardID)
        elif ("zone=PLAY" in line and ("REQ_NOT_EXHAUSTED_ACTIVATE" in line or "error=REQ_ATTACKER_NOT_FROZEN " in line or "error=NONE" in line) and not "zonePos=0" in line and "player=1" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            instance.friendlyMinions.append(cardID)
        elif ("zonePos=0" not in line and "player=2" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            if (cardID == ""):
                logID = line[line.index("id=") : line.index("zone=")]
                cardID = MyLogParser.lookupCardID(logID)
            instance.enemyMinions.append(cardID)
        elif ("type=END_TURN" not in line):
            logID = int(line[line.index("id=") + 3 : line.index("zone=") - 1])
            if (logID == instance.lastCardPlayedID):
                cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
                instance.friendlyMinions.append(cardID)
   
    # print(instance.enemyMinions)
    # print(instance.friendlyMinions)
    # print()

def getHandSize(instance):
    return len(instance.handCards)
    
    
# TO DO: Look a bit more into existing log parser, could save some time