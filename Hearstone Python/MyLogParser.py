import GameState
import API
import Weapon

path = "D:/Hearthstone/Logs/Power.log"
# path = "C:/Program Files (x86)/Hearthstone/Logs/Power.log"

# Process log file line
def processLogFileLine(instance, line) :
    # if (instance.preMulligan):
    #     if ("Block Start=(null)" in line):
    #         instance.preMulligan = False
    if ("PlayerID=1, PlayerName=" in line):
        instance.playerName = line[line.index("Name=")+5:-1]
    if ("option " in line) :
        if ("option 0 " in line and len(instance.optionList) != 0):
            instance.optionList.clear()
        instance.optionList.append(line)
    if ("BLOCK_START" in line or "Block Start=(null)" in line) :
        if (len(instance.optionList) != 0):
            GameState.calculateBoardMinions(instance)
            GameState.calculateHandCards(instance)
            instance.optionList.clear()
    # if ("-   Entities" in line):
    #     if (instance.preMulligan == True or len(instance.preMulliganList) == 0):
    #         instance.preMulligan = True
    #         instance.preMulliganList.append(line)
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
    if ("tag=LAST_CARD_PLAYED" in line and instance.playerName in line):
        instance.lastCardPlayedID = int(line[line.index("value=") + 6:])
    if ("PowerTaskList.DebugPrintPower() -     TAG_CHANGE Entity=GameEntity tag=NEXT_STEP value=BEGIN_MULLIGAN" in line):
        instance.mulliganComplete = True
        # for i in instance.preMulliganList:
        #     print(i[i.index("entityName=") + 11 : i.index(" id=")])
        # for i in instance.mulliganList:
        #     card = i[i.index("cardId"):]
        #     print(card[card.index("name") + 7 : card.index("cardSet") - 3])
        # print()
    if ("TAG_CHANGE" in line and "zone=HAND" in line and "player=1" in line and "tag=ZONE value=PLAY" in line):
        cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
        logID = line[line.index("id=") + 3 : line.index("zone=")]
        if (cardID == ""):
            cardID = lookupCardID(logID)

        cardInfo = ""
        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        if("\"type\":\"Weapon\"" in cardInfo):
            weapon = Weapon.Weapon(instance, cardID, logID)
            instance.friendlyWeaponsInPlay.append(weapon)
    if ("FULL_ENTITY - Updating [entityName=Wicked Knife" in line and "zone=PLAY zonePos=0 cardId=CS2_082 player=1] CardID=CS2_082" in line):
        cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
        logID = line[line.index("id=") + 3 : line.index("zone=")]
        if (cardID == ""):
            cardID = lookupCardID(logID)

        cardInfo = ""
        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        weapon = Weapon.Weapon(instance, cardID, logID)
        instance.friendlyWeaponsInPlay.append(weapon)
    if ("TAG_CHANGE" in line and "zone=PLAY" in line and "player=1" in line and "tag=ZONE value=GRAVEYARD" in line):
        if (len(instance.friendlyWeaponsInPlay) > 0):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            logID = line[line.index("id=") + 3 : line.index("zone=")]
            if (cardID == ""):
                cardID = lookupCardID(logID)

            cardInfo = ""
            if cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[cardID]
            else:
                cardInfo = API.requestCardInfo(cardID)
                instance.cardApiInfo[cardID] = cardInfo

            if("\"type\":\"Weapon\"" in cardInfo):
                weaponToRemove = Weapon.Weapon(cardID, logID)
                for weapon in instance.friendlyWeaponsInPlay:
                    if weapon == weaponToRemove:
                        weaponToRemove = weapon
                instance.friendlyWeaponsInPlay.remove(weaponToRemove)
    if ("TAG_CHANGE" in line and "tag=DAMAGE" in line and "zone=PLAY" in line):
        logID = line[line.index("id=") + 3 : line.index("zone=")]
        
        thisMinion = ""
        for minion in instance.friendlyMinions:
            if minion.logID == logID:
                thisMinion = minion
        for minion in instance.enemyMinions:
            if minion.logID == logID:
                thisMinion = minion

        damage = line[line.index("value=") + 6:]
        thisMinion.currentHealth = int(thisMinion.maxHealth) - int(damage)

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
        logIDStr = "id=" + logID
        if ((logIDStr in line) and ("SHOW_ENTITY " in line)):
            cardID = line[line.index("CardID") + 7 : -1]
            return cardID

def lookupZonePos(logID):
    for line in open(path):
        logIDStr = "id=" + logID
        if (logIDStr in line and "tag=ZONE_POSITION" in line):
            return line[line.index("value=") + 6 : len(line) - 1]