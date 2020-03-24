import speech_recognition as sr
import VoiceCommands
import SimilarWords
import threading
    
r = sr.Recognizer()
mic = sr.Microphone()

recognisedText = ""

def recognise() :
    # To Do: ambient noise stuff
    text = "error"
    try:
        with mic as source:
            # , timeout=2.0
            audio = r.listen(source)
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        text = "error"
    return text

# def takeInputThreaded(instance, control):
#     takeInputThread = threading.Thread(target=takeInput, args=(instance, control), daemon=True)
#     takeInputThread.start()
#     return takeInputThread

def takeInput(instance, control):
    phrase = recognise()
    
    print("Recognised: " + phrase)

    phrase = phrase.lower()

    if (control == True):
        controlCommand(instance, phrase)
    else:
        feedbackCommand(instance, phrase)

def controlCommand(instance, phrase):

    # 
    # General commands
    #

    if (phrase in SimilarWords.exitVoice):
        VoiceCommands.quitProgram(instance)

    # 
    # Gameplay commands
    #

    elif (phrase in SimilarWords.endTurn):
        VoiceCommands.endTurn()

    # 
    # Menu commands
    #

    # Navigate from main menu to single player difficulty selection
    elif (phrase in SimilarWords.singlePlayer):
        VoiceCommands.singlePlayer()

    # Select single player difficulty
    #elif ("difficulty" in phrase):
    elif (any(x in phrase for x in SimilarWords.difficulty)):
        if (any(x in phrase for x in SimilarWords.normal)):
            VoiceCommands.selectDifficulty("normal")
        elif (any(x in phrase for x in SimilarWords.expert)):
            VoiceCommands.selectDifficulty("expert")
        else:
            print("difficulty not recognised")
    
    
    # Select from previous or next decks
    elif (any(x in phrase for x in SimilarWords.decks)):
        if (any(x in phrase for x in SimilarWords.previous)):
            VoiceCommands.prevDecks()
        if (any(x in phrase for x in SimilarWords.nextTheWord)):
            VoiceCommands.nextDecks()

    # Select deck
    elif (any(x in phrase for x in SimilarWords.deck)):
        if (any(x in phrase for x in SimilarWords.one)):
            VoiceCommands.selectDeck(1)
        elif (any(x in phrase for x in SimilarWords.two)):
            VoiceCommands.selectDeck(2)
        elif (any(x in phrase for x in SimilarWords.three)):
            VoiceCommands.selectDeck(3)
        elif (any(x in phrase for x in SimilarWords.four)):
            VoiceCommands.selectDeck(4)
        elif (any(x in phrase for x in SimilarWords.five)):
            VoiceCommands.selectDeck(5)
        elif (any(x in phrase for x in SimilarWords.six)):
            VoiceCommands.selectDeck(6)
        elif (any(x in phrase for x in SimilarWords.seven)):
            VoiceCommands.selectDeck(7)
        elif (any(x in phrase for x in SimilarWords.eight)):
            VoiceCommands.selectDeck(8)
        elif (any(x in phrase for x in SimilarWords.nine)):
            VoiceCommands.selectDeck(9)
    elif (any(x in phrase for x in SimilarWords.dec1)):
        VoiceCommands.selectDeck(1)
    elif (any(x in phrase for x in SimilarWords.dec2)):
        VoiceCommands.selectDeck(2)
    elif (any(x in phrase for x in SimilarWords.dec3)):
        VoiceCommands.selectDeck(3)
    elif (any(x in phrase for x in SimilarWords.dec4)):
        VoiceCommands.selectDeck(4)
    elif (any(x in phrase for x in SimilarWords.dec5)):
        VoiceCommands.selectDeck(5)
    elif (any(x in phrase for x in SimilarWords.dec6)):
        VoiceCommands.selectDeck(6)
    elif (any(x in phrase for x in SimilarWords.dec7)):
        VoiceCommands.selectDeck(4)
    elif (any(x in phrase for x in SimilarWords.dec8)):
        VoiceCommands.selectDeck(5)
    elif (any(x in phrase for x in SimilarWords.dec9)):
        VoiceCommands.selectDeck(6)

    # Select enemy
    elif (any(x in phrase for x in SimilarWords.opponent)):
        modifiedPhrase = phrase.replace('opponent', '')
        if (any(x in modifiedPhrase for x in SimilarWords.one)):
            VoiceCommands.selectOpponent(1)
        elif (any(x in modifiedPhrase for x in SimilarWords.two)):
            VoiceCommands.selectOpponent(2)
        elif (any(x in modifiedPhrase for x in SimilarWords.three)):
            VoiceCommands.selectOpponent(3)
        elif (any(x in modifiedPhrase for x in SimilarWords.four)):
            VoiceCommands.selectOpponent(4)
        elif (any(x in modifiedPhrase for x in SimilarWords.five)):
            VoiceCommands.selectOpponent(5)
        elif (any(x in modifiedPhrase for x in SimilarWords.six)):
            VoiceCommands.selectOpponent(6)
        elif (any(x in modifiedPhrase for x in SimilarWords.seven)):
            VoiceCommands.selectOpponent(7)
        elif (any(x in modifiedPhrase for x in SimilarWords.eight)):
            VoiceCommands.selectOpponent(8)
        elif (any(x in modifiedPhrase for x in SimilarWords.nine)):
            VoiceCommands.selectOpponent(9)

    # Start game
    elif ((any(x in phrase for x in SimilarWords.start)) and (any(x in phrase for x in SimilarWords.game))):
        VoiceCommands.startGame()

    # Play card to position
    elif ((any(x in phrase for x in SimilarWords.play)) and (any(x in phrase for x in SimilarWords.position))):
        cardNo = -1
        positionNo = -1

        if (any(("play " + x) in phrase for x in SimilarWords.one)):
            cardNo = 1
        elif (any(("play " + x) in phrase for x in SimilarWords.two)):
            cardNo = 2
        elif (any(("play " + x) in phrase for x in SimilarWords.three)):
            cardNo = 3
        elif (any(("play " + x) in phrase for x in SimilarWords.four)):
            cardNo = 4
        elif (any(("play " + x) in phrase for x in SimilarWords.five)):
            cardNo = 5
        elif (any(("play " + x) in phrase for x in SimilarWords.six)):
            cardNo = 6
        elif (any(("play " + x) in phrase for x in SimilarWords.seven)):
            cardNo = 7
        elif (any(("play " + x) in phrase for x in SimilarWords.eight)):
            cardNo = 8
        elif (any(("play " + x) in phrase for x in SimilarWords.nine)):
            cardNo = 9
        elif (any(("play " + x) in phrase for x in SimilarWords.ten)):
            cardNo = 10

        if (any(("position " + x) in phrase for x in SimilarWords.one)):
            positionNo = 1
        elif (any(("position " + x) in phrase for x in SimilarWords.two)):
            positionNo = 2
        elif (any(("position " + x) in phrase for x in SimilarWords.three)):
            positionNo = 3
        elif (any(("position " + x) in phrase for x in SimilarWords.four)):
            positionNo = 4
        elif (any(("position " + x) in phrase for x in SimilarWords.five)):
            positionNo = 5
        elif (any(("position " + x) in phrase for x in SimilarWords.six)):
            positionNo = 6
        elif (any(("position " + x) in phrase for x in SimilarWords.seven)):
            positionNo = 7

        if (cardNo != -1 and positionNo != -1):
            VoiceCommands.playCardToPosition(instance, cardNo, positionNo)
    
    # Play card
    # elif ("play card" in phrase or "play cod" in phrase or "play clyde" in phrase or "play cars" in phrase or "play hard" in phrase):
    elif ("play" in phrase):
        if (any(x in phrase for x in SimilarWords.one)):
            VoiceCommands.playCard(instance, 1, True)
        elif (any(x in phrase for x in SimilarWords.two)):
            VoiceCommands.playCard(instance, 2, True)
        elif (any(x in phrase for x in SimilarWords.three)):
            VoiceCommands.playCard(instance, 3, True)
        elif (any(x in phrase for x in SimilarWords.four)):
            VoiceCommands.playCard(instance, 4, True)
        elif (any(x in phrase for x in SimilarWords.five)):
            VoiceCommands.playCard(instance, 5, True)
        elif (any(x in phrase for x in SimilarWords.six)):
            VoiceCommands.playCard(instance, 6, True)
        elif (any(x in phrase for x in SimilarWords.seven)):
            VoiceCommands.playCard(instance, 7, True)
        elif (any(x in phrase for x in SimilarWords.eight)):
            VoiceCommands.playCard(instance, 8, True)
        elif (any(x in phrase for x in SimilarWords.nine)):
            VoiceCommands.playCard(instance, 9, True)
        elif (any(x in phrase for x in SimilarWords.ten)):
            VoiceCommands.playCard(instance, 10, True)
    elif (any(x in phrase for x in SimilarWords.playCardTwo)):
        VoiceCommands.playCard(instance, 2, True)

    # Attack with minion or hero
    elif (any(x in phrase for x in SimilarWords.attack)):
        friendlyNo = -1
        enemyNo = -1
        if (any(("friendly " + x) in phrase for x in SimilarWords.zero)):
            friendlyNo = 0
        elif (any(("friendly " + x) in phrase for x in SimilarWords.one)):
            friendlyNo = 1
        elif (any(("friendly " + x) in phrase for x in SimilarWords.two)):
            friendlyNo = 2
        elif (any(("friendly " + x) in phrase for x in SimilarWords.three)):
            friendlyNo = 3
        elif (any(("friendly " + x) in phrase for x in SimilarWords.four)):
            friendlyNo = 4
        elif (any(("friendly " + x) in phrase for x in SimilarWords.five)):
            friendlyNo = 5
        elif (any(("friendly " + x) in phrase for x in SimilarWords.six)):
            friendlyNo = 6
        elif (any(("friendly " + x) in phrase for x in SimilarWords.seven)):
            friendlyNo = 7

        if (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.zero)):
            enemyNo = 0
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.one)):
            enemyNo = 1
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.two)):
            enemyNo = 2
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.three)):
            enemyNo = 3
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.four)):
            enemyNo = 4
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.five)):
            enemyNo = 5
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.six)):
            enemyNo = 6
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.seven)):
            enemyNo = 7

        if (friendlyNo != -1 and enemyNo != -1):
            VoiceCommands.attack(instance, friendlyNo, enemyNo)

    # Attack the enemy hero with all minions
    elif (any(x in phrase for x in SimilarWords.allFace)):
        VoiceCommands.face(instance)

    # Target a card
    elif (any(x in phrase for x in SimilarWords.target)):
        targetNo = -1
        friendly = True
        if (any(("friendly " + x) in phrase for x in SimilarWords.zero)):
            targetNo = 0
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.one)):
            targetNo = 1
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.two)):
            targetNo = 2
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.three)):
            targetNo = 3
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.four)):
            targetNo = 4
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.five)):
            targetNo = 5
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.six)):
            targetNo = 6
            friendly = True
        elif (any(("friendly " + x) in phrase for x in SimilarWords.seven)):
            targetNo = 7
            friendly = True           
        
        if (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.zero)):
            targetNo = 0
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.one)):
            targetNo = 1
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.two)):
            targetNo = 2
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.three)):
            targetNo = 3
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.four)):
            targetNo = 4
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.five)):
            targetNo = 5
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.six)):
            targetNo = 6
            friendly = False
        elif (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.seven)):
            targetNo = 7
            friendly = False

        if (targetNo != -1):
            VoiceCommands.target(instance, targetNo, friendly)

    # Make mulligan choices
    elif (any(x in phrase for x in SimilarWords.mulligan)):
        if (any(x in phrase for x in SimilarWords.confirm)):
            VoiceCommands.mulliganConfirm()
        else:
            cards = []
            if (any(x in phrase for x in SimilarWords.one)):
                cards.append(1)
            if (any(x in phrase for x in SimilarWords.two)):
                cards.append(2)
            if (any(x in phrase for x in SimilarWords.three)):
                cards.append(3)
            if (any(x in phrase for x in SimilarWords.four)):
                cards.append(4)
            VoiceCommands.mulligan(instance, cards)

    # Hero power
    elif (any(x in phrase for x in SimilarWords.heroPower)):
        VoiceCommands.heroPower()


    # Choose from discover or choose one
    elif (any(x in phrase for x in SimilarWords.choose)):
        if (("<b>Choose One -</b>") in instance.lastCardPlayed):
            # Choose from 'choose one' 
            if (any(x in phrase for x in SimilarWords.choose)):
                if (any(x in phrase for x in SimilarWords.one)):
                        VoiceCommands.chooseOne(1)
                if (any(x in phrase for x in SimilarWords.two)):
                    VoiceCommands.chooseOne(2)
        else:
            if (any(x in phrase for x in SimilarWords.hide) or (any(x in phrase for x in SimilarWords.show))):
                VoiceCommands.discover(-1)
            else:
                if (any(x in phrase for x in SimilarWords.one)):
                        VoiceCommands.discover(1)
                if (any(x in phrase for x in SimilarWords.two)):
                    VoiceCommands.discover(2)
                if (any(x in phrase for x in SimilarWords.three)):
                    VoiceCommands.discover(3)
    elif (any(x in phrase for x in SimilarWords.chooseThree)):
        VoiceCommands.discover(3)


    # Cancel targeted card
    elif (any(x in phrase for x in SimilarWords.cancel)):
        VoiceCommands.cancel()


def specifyHandCardStat(instance, phrase, line):
    if (any(x in phrase for x in SimilarWords.stats)):
        statsToSpeak = ["cost", "attack", "health"]
        VoiceCommands.speakCardStats(instance, line, statsToSpeak)
    elif (any(x in phrase for x in SimilarWords.cost)
        or any(x in phrase for x in SimilarWords.attack)
        or any(x in phrase for x in SimilarWords.health)
        or any(x in phrase for x in SimilarWords.durability)):
        statsToSpeak = []
        if (any(x in phrase for x in SimilarWords.cost)):
            statsToSpeak.append("cost")
        if (any(x in phrase for x in SimilarWords.attack)):
            statsToSpeak.append("attack")
        if (any(x in phrase for x in SimilarWords.health)):
            statsToSpeak.append("health")
        if (any(x in phrase for x in SimilarWords.durability)):
            statsToSpeak.append("durability")
        VoiceCommands.speakCardStats(instance, line, statsToSpeak)
    elif (any(x in phrase for x in SimilarWords.text)):
        VoiceCommands.speakCardText(instance, line)
    elif (any(x in phrase for x in SimilarWords.attributes)):
        VoiceCommands.speakCardAttributes(instance, line)
    else:
        VoiceCommands.speakCardName(instance, line)


def feedbackCommand(instance, phrase):
    print()

    #Speaking hand cards
    if (any(x in phrase for x in SimilarWords.hand)):
        if (any(x in phrase for x in SimilarWords.allSet)):
            VoiceCommands.speakAllHandCards(instance)
        elif ((len(instance.handCards) > 0) and (any(x in phrase for x in SimilarWords.one))):
            line = instance.handCards[0]
            specifyHandCardStat(instance, phrase, line) 
        elif ((len(instance.handCards) > 1) and (any(x in phrase for x in SimilarWords.two))):
            line = instance.handCards[1]
            specifyHandCardStat(instance, phrase, line) 
        elif ((len(instance.handCards) > 2) and (any(x in phrase for x in SimilarWords.three))):
            line = instance.handCards[2]
            specifyHandCardStat(instance, phrase, line) 
        elif ((len(instance.handCards) > 3) and (any(x in phrase for x in SimilarWords.four))):
            line = instance.handCards[3]
            specifyHandCardStat(instance, phrase, line)  
        elif ((len(instance.handCards) > 4) and (any(x in phrase for x in SimilarWords.five))):
            line = instance.handCards[4]
            specifyHandCardStat(instance, phrase, line)  
        elif ((len(instance.handCards) > 5) and (any(x in phrase for x in SimilarWords.six))):
            line = instance.handCards[5]
            specifyHandCardStat(instance, phrase, line)  
        elif ((len(instance.handCards) > 6) and (any(x in phrase for x in SimilarWords.seven))):
            line = instance.handCards[6]
            specifyHandCardStat(instance, phrase, line)  
        elif ((len(instance.handCards) > 7) and (any(x in phrase for x in SimilarWords.eight))):
            line = instance.handCards[7]
            specifyHandCardStat(instance, phrase, line)  
        elif ((len(instance.handCards) > 8) and (any(x in phrase for x in SimilarWords.nine))):
            line = instance.handCards[8]
            specifyHandCardStat(instance, phrase, line)  
        elif ((len(instance.handCards) > 9) and (any(x in phrase for x in SimilarWords.ten))):
            line = instance.handCards[9]
            specifyHandCardStat(instance, phrase, line)  
    elif (any(x in phrase for x in SimilarWords.handAll)):
        VoiceCommands.speakAllHandCards(instance)


    #Speaking board minions
    elif (any(x in phrase for x in SimilarWords.board)):
        if (any(x in phrase for x in SimilarWords.allSet)):
            VoiceCommands.speakAllBoardMinions(instance)
        elif ((len(instance.friendlyMinions) > 0) and (any(("friendly " + x) in phrase for x in SimilarWords.one))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 1)
        elif ((len(instance.friendlyMinions) > 1) and (any(("friendly " + x) in phrase for x in SimilarWords.two))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 2)
        elif ((len(instance.friendlyMinions) > 2) and (any(("friendly " + x) in phrase for x in SimilarWords.three))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 3)
        elif ((len(instance.friendlyMinions) > 3) and (any(("friendly " + x) in phrase for x in SimilarWords.four))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 4)
        elif ((len(instance.friendlyMinions) > 4) and (any(("friendly " + x) in phrase for x in SimilarWords.five))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 5)
        elif ((len(instance.friendlyMinions) > 5) and (any(("friendly " + x) in phrase for x in SimilarWords.six))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 6)
        elif ((len(instance.friendlyMinions) > 6) and (any(("friendly " + x) in phrase for x in SimilarWords.seven))):
            VoiceCommands.speakFriendlyBoardMinion(instance, 7)

        elif ((len(instance.enemyMinions) > 0) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.one))):
            VoiceCommands.speakEnemyBoardMinion(instance, 1)
        elif ((len(instance.enemyMinions) > 1) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.two))):
            VoiceCommands.speakEnemyBoardMinion(instance, 2)
        elif ((len(instance.enemyMinions) > 2) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.three))):
            VoiceCommands.speakEnemyBoardMinion(instance, 3)
        elif ((len(instance.enemyMinions) > 3) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.four))):
            VoiceCommands.speakEnemyBoardMinion(instance, 4)
        elif ((len(instance.enemyMinions) > 4) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.five))):
            VoiceCommands.speakEnemyBoardMinion(instance, 5)
        elif ((len(instance.enemyMinions) > 5) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.six))):
            VoiceCommands.speakEnemyBoardMinion(instance, 6)
        elif ((len(instance.enemyMinions) > 6) and (any((("enemy " + x) or ("anime " + x)) in phrase for x in SimilarWords.seven))):
            VoiceCommands.speakEnemyBoardMinion(instance, 7)
    print() 