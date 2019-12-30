# import LogParser

def calculateHandCards(instance, optionList):
    # Clears the handCards list
    instance.handCards.clear()

    for line in optionList:
        if ((("zone=HAND" in line) or ("zone=DECK" in line)) and not (("error=REQ_NOT_MINION_JUST_PLAYED" in line) or ("error=REQ_YOUR_TURN" in line))):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            zonePos = line[line.index("zonePos=") + 8 : line.index("cardId=") - 1]
            #If the line doesn't contain the card ID, search the log for it
            if (cardID == ""):
                print("potato")
                logID = line[line.index("id=") : line.index("zone=") - 1]
                # cardID = LogParser.lookupCardID(logID)
            print(cardID)
    
# TO DO: Look a bit more into existing log parser, could save some time