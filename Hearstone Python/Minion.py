import API
class Minion:
    cardID = ""
    logID = ""
    attack = -1
    maxHealth = -1
    currentHealth = -1

    def __init__(self, instance, cardID, logID):
        self.cardID = cardID
        self.logID = logID

        cardInfo = ""
        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        commaIndexes = [x for x, v in enumerate(cardInfo) if v == ',']
        attackIndex = None
        for index in commaIndexes:
            if (index > cardInfo.index("\"attack\":") + 9):
                attackIndex = index
                break

        healthIndex = None
        for index in commaIndexes:
            if (index > cardInfo.index("\"health\":") + 9):
                healthIndex = index
                break

        self.attack = cardInfo[cardInfo.index("\"attack\":") + 9: attackIndex]
        self.maxHealth = cardInfo[cardInfo.index("\"health\":") + 9: healthIndex]
        
        self.currentHealth = self.maxHealth

    def __str__(self):
        return str("cardID: " + str(self.cardID) + ", logID: " + str(self.logID))

    # Attributes/effects?