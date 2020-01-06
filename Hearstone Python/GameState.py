import MyLogParser
import API

def calculateHandCards(instance):
    instance.handCards.clear()

    for line in instance.optionList:
        if ((("zone=HAND" in line) or ("zone=DECK" in line)) and not (("error=REQ_NOT_MINION_JUST_PLAYED" in line) or ("error=REQ_YOUR_TURN" in line))):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            zonePos = int(line[line.index("zonePos=") + 8 : line.index("cardId=") - 1])
            
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

            #Checks that the zonePos isn't duplicate (occurs when drawing cards on turn), if it is adds the card to the end
            if ((zonePos-1 in instance.handCards) and (zonePos != 0)) :
                instance.handCards[len(instance.handCards)+1] = cardInfo
            else :
                instance.handCards[zonePos - 1] = cardInfo

    #Sorting dictionary in order
    tempHandCards = {}
    sortedHandCards = sorted(instance.handCards)
    for i in sortedHandCards:
        tempHandCards[i] = instance.handCards[i]
    instance.handCards = tempHandCards
    
    # for i in instance.handCards:
    #     cardInfo = instance.handCards[i]
    #     card = cardInfo[cardInfo.index("cardId"):]
    #     print(card[card.index("name") + 7 : card.index("cardSet") - 3])
    # print()


def calculateBoardMinions(instance):
    for line in instance.optionList:
        if ("error=REQ_NOT_MINION_JUST_PLAYED" in line):
            print(line)

def getHandSize(instance):
    return len(instance.handCards)
    
    
# TO DO: Look a bit more into existing log parser, could save some time