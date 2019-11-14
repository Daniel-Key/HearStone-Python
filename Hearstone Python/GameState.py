class GameState:
    mulliganInProgress = False
    mulliganComplete = False
    mulliganList = []
    handCards = []

    def calculateHandCards(self, optionList):
        # Clears the handCards list
        self.handCards.clear()

        for line in optionList:
            if ((("zone=HAND" in line) or ("zone=DECK" in line)) and not (("error=REQ_NOT_MINION_JUST_PLAYED" in line) or ("error=REQ_YOUR_TURN" in line))):
                cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
                print(cardID)
        
    # TO DO: Look a bit more into existing log parser, could save some time