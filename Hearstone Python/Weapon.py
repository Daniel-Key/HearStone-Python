import API
class Weapon:
    cardID = ""
    logID = ""
    attack = -1
    durability = -1

    def __init__(self, instance, cardID, logID):
        self.cardID = cardID
        self.logID = logID

        cardInfo = ""
        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        self.attack = cardInfo[cardInfo.index("\"attack\":") + 9: cardInfo.index(",\"durability")]
        try:
            self.durability = cardInfo[cardInfo.index("\"durability\":") + 13: cardInfo.index(",\"text")]
        except:
            self.durability = cardInfo[cardInfo.index("\"durability\":") + 13: cardInfo.index(",\"playerClass")]

    def __str__(self):
        return str("cardID: " + str(self.cardID) + ", logID: " + str(self.logID) + "attack: " + str(self.attack) + ", durability: " + str(self.durability))

    def __eq__(self, other):
        return ((self.cardID, self.logID) ==
                (other.cardID, other.logID))

    # Attributes/effects?