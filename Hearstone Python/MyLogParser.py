import GameState
import API
import Weapon
import Minion

path = "D:/Hearthstone/Logs/Power.log"
# path = "C:/Program Files (x86)/Hearthstone/Logs/Power.log"

# Process log file line
def processLogFileLine(instance, line, lineNo) :
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
            GameState.calculateOptions(instance)
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
        instance.lastCardPlayedID = str(int(line[line.index("value=") + 6:])) + " "

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
            cardID = lookupCardID(instance, logID)

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
            cardID = lookupCardID(instance, logID)

        cardInfo = ""
        if cardID in instance.cardApiInfo:
            cardInfo = instance.cardApiInfo[cardID]
        else:
            cardInfo = API.requestCardInfo(cardID)
            instance.cardApiInfo[cardID] = cardInfo

        weapon = Weapon.Weapon(instance, cardID, logID)
        instance.friendlyWeaponsInPlay.append(weapon)

    if ("TAG_CHANGE" in line and "zone=PLAY" in line and "tag=ZONE value=GRAVEYARD" in line):
            cardID = line[line.index("cardId=") + 7 : line.index("player=") - 1]
            logID = line[line.index("id=") + 3 : line.index("zone=")]
            zonePos = line[line.index("zonePos=") + 8 : line.index("cardId=")]

            if (cardID == ""):
                cardID = lookupCardID(instance, logID)

            cardInfo = ""
            if cardID in instance.cardApiInfo:
                cardInfo = instance.cardApiInfo[cardID]
            else:
                cardInfo = API.requestCardInfo(cardID)
                instance.cardApiInfo[cardID] = cardInfo

            if("\"type\":\"Weapon\"" in cardInfo):
                if ("player=1" in line):
                    if (len(instance.friendlyWeaponsInPlay) > 0):
                        weaponToRemove = Weapon.Weapon(instance, cardID, logID)
                        for weapon in instance.friendlyWeaponsInPlay:
                            if weapon == weaponToRemove:
                                weaponToRemove = weapon
                        instance.friendlyWeaponsInPlay.remove(weaponToRemove)
                        instance.friendlyWeapons.clear()
                else:
                    if (len(instance.enemyWeapons) > 0):
                        weaponToRemove = Weapon.Weapon(instance, cardID, logID)
                        for weapon in instance.enemyWeapons:
                            if weapon == weaponToRemove:
                                weaponToRemove = weapon
                        instance.enemyWeapons.remove(weaponToRemove)
            elif("\"type\":\"Minion\"" in cardInfo):
                if ("player=1" in line):
                    if (len(instance.friendlyMinions) > 0):
                        minionToRemove = Minion.Minion(instance, cardID, logID, zonePos)
                        for minion in instance.friendlyMinions:
                            if minion == minionToRemove:
                                minionToRemove = minion
                        try:
                            instance.friendlyMinions.remove(minionToRemove)
                        except:
                            None
                else:
                    if (len(instance.enemyMinions) > 0):
                        minionToRemove = Minion.Minion(instance, cardID, logID, zonePos)
                        for minion in instance.enemyMinions:
                            if minion == minionToRemove:
                                minionToRemove = minion
                        try:
                            instance.enemyMinions.remove(minionToRemove)
                        except:
                            None

    if ("TAG_CHANGE" in line and "tag=DAMAGE" in line and "zone=PLAY" in line):
        logID = line[line.index("id=") + 3 : line.index("zone=")]
        
        thisMinion = ""
        minionFound = False
        for minion in instance.friendlyMinions:
            if minion.logID == logID:
                thisMinion = minion
                minionFound = True
        for minion in instance.enemyMinions:
            if minion.logID == logID:
                thisMinion = minion
                minionFound = True

        if (minionFound):
            damage = line[line.index("value=") + 6:]
            thisMinion.currentHealth = int(thisMinion.maxHealth) - int(damage)

    if ("TAG_CHANGE" in line and "tag=ZONE_POSITION" in line and "Entity=[entityName=" in line):
        logID = line[line.index("id=") + 3 : line.index("zone=")]
        zonePos = line[line.index("value=") + 6 :]
        
        friendlyChanged = False
        enemyChanged = False
        for minion in instance.friendlyMinions:
            if minion.logID == logID:
                minion.zonePos = zonePos
                friendlyChanged = True
        for minion in instance.enemyMinions:
            if minion.logID == logID:
                minion.zonePos = zonePos
                enemyChanged = True

        if (friendlyChanged):
            instance.friendlyMinions.sort(key=lambda x: x.zonePos)
        if (enemyChanged):
            instance.enemyMinions.sort(key=lambda x: x.zonePos)

    if ("TAG_CHANGE Entity=[entityName=" in line and "tag=ATK" in line):
        logID = line[line.index("id=") + 3 : line.index("zone=")]
        attack = line[line.index("value=") + 6 :]

        for minion in instance.friendlyMinions:
            if minion.logID == logID:
                minion.attack = attack
        for minion in instance.enemyMinions:
            if minion.logID == logID:
                minion.attack = attack
        for weapon in instance.friendlyWeapons:
            if weapon.logID == logID:
                weapon.attack = attack
        for weapon in instance.enemyWeapons:
            if weapon.logID == logID:
                weapon.attack = attack

    if ("TAG_CHANGE Entity=GameEntity tag=STEP value=FINAL_GAMEOVER" in line):
        instance.logFileGameStart = lineNo
        instance.reset()

# Will be in main loop looking for game state changes
def checkForLogFileUpdates(instance):
    thisLength = 0
    for line in open(path):
        thisLength = thisLength + 1
        # If line has not yet been processed
        if ((thisLength > instance.logFileGameStart) and (thisLength > instance.logLength)):
            processLogFileLine(instance, line, thisLength)
            instance.logLength = thisLength
    # Resetting logFileGameStart if log is cleared by game
    # E.g. if app opened before new game started, so log cleared mid-run
    if instance.logLength < instance.logFileGameStart:
        instance.logFileGameStart = 0
    # Resetting logLength if log is cleared by game
    # E.g. if app opened before new game started, so log cleared mid-run
    if (thisLength < instance.logLength):
        instance.logLength = thisLength


def checkForGameStart(instance):
    lineNo = 0
    for line in open(path):
        lineNo = lineNo + 1
        if ("TAG_CHANGE Entity=GameEntity tag=STEP value=FINAL_GAMEOVER" in line):
            instance.logFileGameStart = lineNo


def lookupCardID(instance, logID):
    logIDStr = "id=" + logID
    thisLength = 0
    for line in open(path):
        thisLength = thisLength + 1
        if ((thisLength > instance.logFileGameStart) and (logIDStr in line) and ("SHOW_ENTITY " in line)):
            cardID = line[line.index("CardID") + 7 : -1]
            return cardID


def lookupZonePos(instance, zonePos):
    thisLength = 0
    for line in open(path):
        thisLength = thisLength + 1
        zonePosStr = "id=" + zonePos
        if ((thisLength > instance.logFileGameStart) and zonePosStr in line and "tag=ZONE_POSITION" in line):
            return line[line.index("value=") + 6 : len(line) - 1]


            
        