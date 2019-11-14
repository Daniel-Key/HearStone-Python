class GameState:
    mulliganInProgress = False
    mulliganComplete = False
    mulliganList = []
    handCards = []

    def calculateHandCards(self, optionList):
        self.handCards.clear()
        