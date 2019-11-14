import GameState
import API
class LogParser():
    # path = "D:/Hearthstone/Logs/Power.log"
    path = "C:/Program Files (x86)/Hearthstone/Logs/Power.log"
    logLength = 0
    optionList = []
    gameState = GameState.GameState()

    # Process log file line
    def processLogFileLine(self, line) :
        if ("option " in line) :
            self.optionList.append(line)
        if ("BLOCK_START" in line) :
            if (len(self.optionList) != 0):
                self.gameState.calculateHandCards(self.optionList)
                self.optionList.clear()
        if ("SHOW_ENTITY - Updating Entity=[entityName=UNKNOWN ENTITY [cardType=INVALID]" in line):
            GameState.mulliganInProgress = True
            cardIdIndex = line.index("CardID=") + 7
            cardID = line[cardIdIndex:]
            cardID = cardID[:len(cardID)-1]
            # String cardInfo = API.callAPI(cardID);
            # requestCardInfo = Main.api.requestCardInfo
            # cardInfo = requestCardInfo(cardID)
            #print(cardInfo)
            # mulliganList.add(cardInfo);
            # String card = cardInfo.substring(cardInfo.indexOf("cardId"));
            # System.out.println(card.substring(card.indexOf("name") + 7, card.indexOf("imgGold") - 3));

        if ("PowerTaskList.DebugPrintPower() -     TAG_CHANGE Entity=GameEntity tag=NEXT_STEP value=BEGIN_MULLIGAN" in line):
            GameState.mulliganComplete = True

    # Will be in main loop looking for game state changes
    def checkForLogFileUpdates(self):
        thisLength = 0
        for line in open(self.path):
            thisLength = thisLength + 1
            # If line has not yet been processed
            if (thisLength > self.logLength):
                self.processLogFileLine(line)
                LogParser.logLength = thisLength