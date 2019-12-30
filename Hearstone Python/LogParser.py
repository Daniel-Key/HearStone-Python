import GameState
import API

path = "D:/Hearthstone/Logs/Power.log"
# path = "C:/Program Files (x86)/Hearthstone/Logs/Power.log"

# Process log file line
def processLogFileLine(instance, line) :
    if ("option " in line) :
        instance.optionList.append(line)
    if ("BLOCK_START" in line) :
        if (len(instance.optionList) != 0):
            GameState.calculateHandCards(instance, instance.optionList)
            instance.optionList.clear()
    if ("SHOW_ENTITY - Updating Entity=[entityName=UNKNOWN ENTITY [cardType=INVALID]" in line):
        GameState.mulliganInProgress = True
        cardIdIndex = line.index("CardID=") + 7
        cardID = line[cardIdIndex:]
        cardID = cardID[:len(cardID)-1]
        # cardInfo = API.callAPI(cardID);
        # print(cardID)
        cardInfo = API.requestCardInfo(cardID)
        # mulliganList.add(cardInfo);
        # String card = cardInfo.substring(cardInfo.indexOf("cardId"));
        # System.out.println(card.substring(card.indexOf("name") + 7, card.indexOf("imgGold") - 3));

    if ("PowerTaskList.DebugPrintPower() -     TAG_CHANGE Entity=GameEntity tag=NEXT_STEP value=BEGIN_MULLIGAN" in line):
        GameState.mulliganComplete = True

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
        if (line.contains(logID) and line.contains("SHOW_ENTITY ")):
            cardID = line[line.index("CardID") + 7]
            return cardID