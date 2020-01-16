import speech_recognition as sr
import VoiceCommands
    
r = sr.Recognizer()
mic = sr.Microphone()

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

    if (phrase == "exit voice"):
        VoiceCommands.quitProgram()

    # 
    # Gameplay commands
    #

    elif (phrase == "end turn" or phrase == "and turn" or phrase == "entertain" or phrase == "nth term" or phrase == "anton" or phrase == "enstone" or phrase == "and 10" or phrase == "enter"):
        VoiceCommands.endTurn()

    # 
    # Menu commands
    #

    # Navigate from main menu to single player difficulty selection
    elif (phrase == "single player"):
        VoiceCommands.singlePlayer()

    # Select single player difficulty
    elif ("difficulty" in phrase):
        if ("normal" in phrase):
            VoiceCommands.selectDifficulty("normal")
        elif ("expert" in phrase):
            VoiceCommands.selectDifficulty("expert")
        else:
            print("difficulty not recognised")
    
    # Select deck
    elif ("deck" in phrase or "dick" in phrase or "next" in phrase or "text" in phrase or "tech" in phrase or "ek" in phrase or "jet" in phrase):
        if ("1" in phrase or "one" in phrase):
            VoiceCommands.selectDeck(1)
        elif ("2" in phrase or "two" in phrase or "too" in phrase or "to" in phrase):
            VoiceCommands.selectDeck(2)
        elif ("3" in phrase or "three" in phrase or "free" in phrase):
            VoiceCommands.selectDeck(3)
        elif ("4" in phrase or "four" in phrase or "for" in phrase):
            VoiceCommands.selectDeck(4)
        elif ("5" in phrase or "five" in phrase):
            VoiceCommands.selectDeck(5)
        elif ("6" in phrase or "six" in phrase):
            VoiceCommands.selectDeck(6)
        elif ("7" in phrase or "seven" in phrase):
            VoiceCommands.selectDeck(7)
        elif ("8" in phrase or "eight" in phrase or "ate" in phrase):
            VoiceCommands.selectDeck(8)
        elif ("9" in phrase or "nine" in phrase):
            VoiceCommands.selectDeck(9)
    elif ("dec1" in phrase or "daquan" in phrase):
        VoiceCommands.selectDeck(1)
    elif ("dec2" in phrase or "bectu" in phrase):
        VoiceCommands.selectDeck(2)
    elif ("dec3" in phrase or "dec free" in phrase):
        VoiceCommands.selectDeck(3)
    elif ("dec4" in phrase):
        VoiceCommands.selectDeck(4)
    elif ("dec5" in phrase):
        VoiceCommands.selectDeck(5)
    elif ("dec6" in phrase):
        VoiceCommands.selectDeck(6)
    elif ("dec7" in phrase):
        VoiceCommands.selectDeck(4)
    elif ("dec8" in phrase or "decade" in phrase):
        VoiceCommands.selectDeck(5)
    elif ("dec9" in phrase):
        VoiceCommands.selectDeck(6)

    # Select enemy
    elif ("opponent" in phrase or "appointment" in phrase or "exponent" in phrase):
        if ("1" in phrase):
            VoiceCommands.selectOpponent(1)
        elif ("2" in phrase or "two" in phrase or "to" in phrase):
            VoiceCommands.selectOpponent(2)
        elif ("3" in phrase or "three" in phrase or "free" in phrase):
            VoiceCommands.selectOpponent(3)
        elif ("4" in phrase or "four" in phrase or "for" in phrase):
            VoiceCommands.selectOpponent(4)
        elif ("5" in phrase or "five" in phrase):
            VoiceCommands.selectOpponent(5)
        elif ("6" in phrase or "six" in phrase):
            VoiceCommands.selectOpponent(6)
        elif ("7" in phrase or "seven" in phrase):
            VoiceCommands.selectOpponent(7)
        elif ("8" in phrase or "eight" in phrase or "ate" in phrase):
            VoiceCommands.selectOpponent(8)
        elif ("9" in phrase or "nine" in phrase):
            VoiceCommands.selectOpponent(9)

    # Start game
    elif ("start" in phrase and "game" in phrase):
        VoiceCommands.startGame()

    # Play card
    # elif ("play card" in phrase or "play cod" in phrase or "play clyde" in phrase or "play cars" in phrase or "play hard" in phrase):
    elif ("play" in phrase):
        if ("1" in phrase or "one" in phrase):
            VoiceCommands.playCard(instance, 1)
        elif ("2" in phrase or "two" in phrase or "to" in phrase):
            VoiceCommands.playCard(instance, 2)
        elif ("3" in phrase or "three" in phrase or "free" in phrase):
            VoiceCommands.playCard(instance, 3)
        elif ("4" in phrase or "four" in phrase or "for" in phrase):
            VoiceCommands.playCard(instance, 4)
        elif ("5" in phrase or "five" in phrase):
            VoiceCommands.playCard(instance, 5)
        elif ("6" in phrase or "six" in phrase):
            VoiceCommands.playCard(instance, 6)
        elif ("7" in phrase or "seven" in phrase):
            VoiceCommands.playCard(instance, 7)
        elif ("8" in phrase or "eight" in phrase or "ate" in phrase):
            VoiceCommands.playCard(instance, 8)
        elif ("9" in phrase or "nine" in phrase): 
            VoiceCommands.playCard(instance, 9)
        elif ("10" in phrase or "ten" in phrase):
            VoiceCommands.playCard(instance, 10)
    elif ("play cartoon" in phrase):
        VoiceCommands.playCard(instance, 2)

    # Attack with minion or hero
    elif ("attack" in phrase or "a tack" in phrase or "tech" in phrase):
        friendlyNo = -1
        enemyNo = -1
        if ("friendly 0" in phrase or "friendly zero" in phrase):
            friendlyNo = 0
        elif ("friendly 1" in phrase or "friendly one" in phrase):
            friendlyNo = 1
        elif ("friendly 2" in phrase or "friendly two" in phrase or "friendly to" in phrase):
            friendlyNo = 2
        elif ("friendly 3" in phrase or "friendly three" in phrase or "friendly free" in phrase):
            friendlyNo = 3
        elif ("friendly 4" in phrase or "friendly four" in phrase or "friendly for" in phrase):
            friendlyNo = 4
        elif ("friendly 5" in phrase or "friendly five" in phrase):
            friendlyNo = 5
        elif ("friendly 6" in phrase or "friendly six" in phrase):
            friendlyNo = 6
        elif ("friendly 7" in phrase or "friendly seven" in phrase):
            friendlyNo = 7
        elif ("friendly 8" in phrase or "friendly eight" in phrase or "friendly ate" in phrase):
            friendlyNo = 8
        elif ("friendly 9" in phrase or "friendly nine" in phrase):
            friendlyNo = 9
        elif ("friendly 10" in phrase or "friendly ten" in phrase):
            friendlyNo = 10

        if ("enemy 0" in phrase or "enemy zero" in phrase or "anime 0" in phrase or "anime zero" in phrase):
            enemyNo = 0
        elif ("enemy 1" in phrase or "enemy one" in phrase or "anyone" in phrase or "anime 1" in phrase or "anime one" in phrase):
            enemyNo = 1
        elif ("enemy 2" in phrase or "enemy two" in phrase or "enemy to" in phrase or "anime 2" in phrase or "anime two" in phrase or "anime to" in phrase):
            enemyNo = 2
        elif ("enemy 3" in phrase or "enemy three" in phrase or "enemy free" in phrase or "anime 3" in phrase or "anime three" in phrase or "anime free" in phrase):
            enemyNo = 3
        elif ("enemy 4" in phrase or "enemy four" in phrase or "enemy for" in phrase or "anime 4" in phrase or "anime four" in phrase or "anime for" in phrase):
            enemyNo = 4
        elif ("enemy 5" in phrase or "enemy five" in phrase or "anime 5" in phrase or "anime five" in phrase):
            enemyNo = 5
        elif ("enemy 6" in phrase or "enemy six" in phrase or "anime 6" in phrase or "anime six" in phrase):
            enemyNo = 6
        elif ("enemy 7" in phrase or "enemy seven" in phrase or "anime 7" in phrase or "anime seven" in phrase):
            enemyNo = 7
        elif ("enemy 8" in phrase or "enemy eight" in phrase or "enemy ate" in phrase or "anime 8" in phrase or "anime eight" in phrase or "anime ate" in phrase):
            enemyNo = 8
        elif ("enemy 9" in phrase or "enemy nine" in phrase or "anime 9" in phrase or "anime nine" in phrase):
            enemyNo = 9
        elif ("enemy 10" in phrase or "enemy ten" in phrase or "anime 10" in phrase or "anime ten" in phrase):
            enemyNo = 10

        if (friendlyNo != -1 and enemyNo != -1):
            VoiceCommands.attack(instance, friendlyNo, enemyNo)

    # Attack the enemy hero with all minions
    elif ("all face" in phrase or "altace" in phrase or "old face" in phrase):
        VoiceCommands.face(instance)

    # Target a card
    elif ("target" in phrase):
        targetNo = -1
        friendly = True
        if ("friendly 0" in phrase or "friendly zero" in phrase):
            targetNo = 0
            friendly = True
        elif ("friendly 1" in phrase or "friendly one" in phrase):
            targetNo = 1
            friendly = True
        elif ("friendly 2" in phrase or "friendly two" in phrase or "friendly to" in phrase):
            targetNo = 2
            friendly = True
        elif ("friendly 3" in phrase or "friendly three" in phrase or "friendly free" in phrase):
            targetNo = 3
            friendly = True
        elif ("friendly 4" in phrase or "friendly four" in phrase or "friendly for" in phrase):
            targetNo = 4
            friendly = True
        elif ("friendly 5" in phrase or "friendly five" in phrase):
            targetNo = 5
            friendly = True
        elif ("friendly 6" in phrase or "friendly six" in phrase):
            targetNo = 6
            friendly = True
        elif ("friendly 7" in phrase or "friendly seven" in phrase):
            targetNo = 7
            friendly = True
        elif ("friendly 8" in phrase or "friendly eight" in phrase or "friendly ate" in phrase):
            targetNo = 8
            friendly = True
        elif ("friendly 9" in phrase or "friendly nine" in phrase):
            targetNo = 9
            friendly = True
        elif ("friendly 10" in phrase or "friendly ten" in phrase):
            targetNo = 10
            friendly = True            
        
        if ("enemy 0" in phrase or "enemy zero" in phrase or "anime 0" in phrase or "anime zero" in phrase):
            targetNo = 0
            friendly = False
        elif ("enemy 1" in phrase or "enemy one" in phrase or "anyone" in phrase or "anime 1" in phrase or "anime one" in phrase):
            targetNo = 1
            friendly = False
        elif ("enemy 2" in phrase or "enemy two" in phrase or "enemy to" in phrase or "anime 2" in phrase or "anime two" in phrase or "anime to" in phrase):
            targetNo = 2
            friendly = False
        elif ("enemy 3" in phrase or "enemy three" in phrase or "enemy free" in phrase or "anime 3" in phrase or "anime three" in phrase or "anime free" in phrase):
            targetNo = 3
            friendly = False
        elif ("enemy 4" in phrase or "enemy four" in phrase or "enemy for" in phrase or "anime 4" in phrase or "anime four" in phrase or "anime for" in phrase):
            targetNo = 4
            friendly = False
        elif ("enemy 5" in phrase or "enemy five" in phrase or "anime 5" in phrase or "anime five" in phrase):
            targetNo = 5
            friendly = False
        elif ("enemy 6" in phrase or "enemy six" in phrase or "anime 6" in phrase or "anime six" in phrase):
            targetNo = 6
            friendly = False
        elif ("enemy 7" in phrase or "enemy seven" in phrase or "anime 7" in phrase or "anime seven" in phrase):
            targetNo = 7
            friendly = False
        elif ("enemy 8" in phrase or "enemy eight" in phrase or "enemy ate" in phrase or "anime 8" in phrase or "anime eight" in phrase or "anime ate" in phrase):
            targetNo = 8
            friendly = False
        elif ("enemy 9" in phrase or "enemy nine" in phrase or "anime 9" in phrase or "anime nine" in phrase):
            targetNo = 9
            friendly = False
        elif ("enemy 10" in phrase or "enemy ten" in phrase or "anime 10" in phrase or "anime ten" in phrase):
            targetNo = 10
            friendly = False

        if (targetNo != -1):
            VoiceCommands.target(instance, targetNo, friendly)

    # Make mulligan choices
    elif ("mulligan" in phrase or "Milligan" in phrase):
        if ("confirm" in phrase):
            VoiceCommands.mulliganConfirm()
        else:
            cards = []
            if ("1" in phrase or "one" in phrase):
                cards.append(1)
            if ("2" in phrase or "two" in phrase or "to" in phrase):
                cards.append(2)
            if ("3" in phrase or "three" in phrase or "free" in phrase):
                cards.append(3)
            if ("4" in phrase or "four" in phrase or "for" in phrase):
                cards.append(4)
            VoiceCommands.mulligan(instance, cards)

    # Hero power
    elif ("hero power" in phrase):
        VoiceCommands.heroPower()


    # Choose from discover
    elif ("choose" in phrase or "cheese" in phrase):
        if ("hide" in phrase or "show" in phrase):
            VoiceCommands.discover(-1)
        else:
            if ("1" in phrase or "one" in phrase):
                    VoiceCommands.discover(1)
            if ("2" in phrase or "two" in phrase or "to" in phrase):
                VoiceCommands.discover(2)
            if ("3" in phrase or "three" in phrase or "free" in phrase):
                VoiceCommands.discover(3)
    elif ("shrewsbury" in phrase):
        VoiceCommands.discover(3)

    # Cancel targeted card
    elif ("cancel" in phrase):
        VoiceCommands.cancel()


def feedbackCommand(instance, phrase):
    print()
    if ("hand" in phrase or "and" in phrase):
        if ("all" in phrase):
            VoiceCommands.readAllHandCards(instance)
        elif ((len(instance.handCards) > 0) and (("one" in phrase) or ("1" in phrase))):
            line = instance.handCards[0]
            VoiceCommands.readCardName(instance, line)

    if ("handle" in phrase):
        for i in instance.handCards:
            line = instance.handCards[i]
            VoiceCommands.readCardName(instance, line)
    print()