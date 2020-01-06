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

def takeInput(instance):
    phrase = recognise()
    print("Recognised: " + phrase)

    phrase = phrase.lower()

    # 
    # General commands
    #

    if (phrase == "exit voice"):
        VoiceCommands.quitProgram()

    # 
    # Gameplay commands
    #

    elif (phrase == "end turn" or phrase == "and turn" or phrase == "entertain" or phrase == "nth term" or phrase == "anton"):
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
        elif ("7" in phrase or "seven" in phrase or "for" in phrase):
            VoiceCommands.selectDeck(7)
        elif ("8" in phrase or "eight" in phrase):
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
        elif ("7" in phrase or "seven" in phrase or "for" in phrase):
            VoiceCommands.selectOpponent(7)
        elif ("8" in phrase or "eight" in phrase):
            VoiceCommands.selectOpponent(8)
        elif ("9" in phrase or "nine" in phrase):
            VoiceCommands.selectOpponent(9)

    # Play game
    elif ("play" in phrase and "game" in phrase):
        VoiceCommands.playGame()


    # Play card
    elif ("play card" in phrase or "play cod" in phrase or "play clyde" in phrase):
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
        elif ("7" in phrase or "seven" in phrase or "for" in phrase):
            VoiceCommands.playCard(instance, 7)
        elif ("8" in phrase or "eight" in phrase):
            VoiceCommands.playCard(instance, 8)
        elif ("9" in phrase or "nine" in phrase): 
            VoiceCommands.playCard(instance, 9)
        elif ("10" in phrase or "ten" in phrase):
            VoiceCommands.playCard(instance, 10)
    elif ("play cartoon" in phrase):
        VoiceCommands.playCard(instance, 2)
