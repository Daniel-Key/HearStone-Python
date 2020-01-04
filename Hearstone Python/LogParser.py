import GameState
import API

path = "D:/Hearthstone/Logs/Power.log"
# path = "C:/Program Files (x86)/Hearthstone/Logs/Power.log"

# Process log file line
def processLogFileLine(instance, line) :
    if ("option " in line) :
        if ("option 0 " in line and len(instance.optionList) != 0):
            instance.optionList.clear()
        instance.optionList.append(line)
    if ("BLOCK_START" in line) :
        if (len(instance.optionList) != 0):
            GameState.calculateHandCards(instance, instance.optionList)
            instance.optionList.clear()
    #TO DO: Get mulligan choice information (should be easy from log)
    if ("SHOW_ENTITY - Updating Entity=[entityName=UNKNOWN ENTITY [cardType=INVALID]" in line):
        instance.mulliganInProgress = True
        cardIdIndex = line.index("CardID=") + 7
        cardID = line[cardIdIndex:]
        cardID = cardID[:len(cardID)-1]
        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo
        instance.mulliganList.append(cardInfo)

    if ("PowerTaskList.DebugPrintPower() -     TAG_CHANGE Entity=GameEntity tag=NEXT_STEP value=BEGIN_MULLIGAN" in line):
        instance.mulliganComplete = True
        for i in instance.mulliganList:
            card = i[i.index("cardId"):]
            print(card[card.index("name") + 7 : card.index("cardSet") - 3])

# Will be in main loop looking for game state changes
def checkForLogFileUpdates(instance):
    thisLength = 0
    for line in open(path):
        thisLength = thisLength + 1
        # If line has not yet been processed
        if (thisLength > instance.logLength):
            processLogFileLine(instance, line)
            instance.logLength = thisLength

def lookupCardID(logID):
    for line in open(path):
        if ((logID in line) and ("SHOW_ENTITY " in line)):
            cardID = line[line.index("CardID") + 7 : -1]
            return cardID

def lookupZonePos(logID):
    for line in open(path):
        if (logID in line and "tag=ZONE_POSITION" in line):
            return line[line.index("value=") + 6 : len(line) - 1]