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

def takeInput():
    phrase = recognise()
    print("Recognised: " + phrase)

    # 
    # General commands
    #

    if (phrase == "exit voice"):
        voiceCommands.quitProgram()

    # 
    # Gameplay commands
    #

    elif (phrase == "end turn" or phrase == "and turn" or phrase == "entertain" or phrase == "nth term" or phrase == "Anton"):
        voiceCommands.endTurn()

    # 
    # Menu commands
    #

    # Navigate from main menu to single player difficulty selection
    elif (phrase == "single player"):
        voiceCommands.singlePlayer()

    # Select single player difficulty
    elif ("difficulty" in phrase):
        if ("normal" in phrase):
            voiceCommands.selectDifficulty("normal")
        elif ("expert" in phrase):
            voiceCommands.selectDifficulty("expert")
        else:
            print("difficulty not recognised")
    
    # Select deck
    elif ("deck" in phrase or "dick" in phrase or "next" in phrase or "text" in phrase or "tech" in phrase or "EK" in phrase or "Jet" in phrase):
        if ("1" in phrase or "one" in phrase):
            voiceCommands.selectDeck(1)
        elif ("2" in phrase or "two" in phrase or "too" in phrase or "to" in phrase):
            voiceCommands.selectDeck(2)
        elif ("3" in phrase or "three" in phrase or "free" in phrase):
            voiceCommands.selectDeck(3)
        elif ("4" in phrase or "four" in phrase or "for" in phrase):
            voiceCommands.selectDeck(4)
        elif ("5" in phrase or "five" in phrase):
            voiceCommands.selectDeck(5)
        elif ("6" in phrase or "six" in phrase):
            voiceCommands.selectDeck(6)
        elif ("7" in phrase or "seven" in phrase or "for" in phrase):
            voiceCommands.selectDeck(7)
        elif ("8" in phrase or "eight" in phrase):
            voiceCommands.selectDeck(8)
        elif ("9" in phrase or "nine" in phrase):
            voiceCommands.selectDeck(9)
    elif ("dec1" in phrase or "daquan" in phrase):
        voiceCommands.selectDeck(1)
    elif ("dec2" in phrase or "bectu" in phrase):
        voiceCommands.selectDeck(2)
    elif ("dec3" in phrase or "Dec free" in phrase):
        voiceCommands.selectDeck(3)
    elif ("dec4" in phrase):
        voiceCommands.selectDeck(4)
    elif ("dec5" in phrase):
        voiceCommands.selectDeck(5)
    elif ("dec6" in phrase):
        voiceCommands.selectDeck(6)
    elif ("dec7" in phrase):
        voiceCommands.selectDeck(4)
    elif ("dec8" in phrase or "decade" in phrase):
        voiceCommands.selectDeck(5)
    elif ("dec9" in phrase):
        voiceCommands.selectDeck(6)

    # Select enemy
    elif ("opponent" in phrase or "appointment" in phrase or "exponent" in phrase):
        if ("1" in phrase):
            voiceCommands.selectOpponent(1)
        elif ("2" in phrase or "two" in phrase or "to" in phrase):
            voiceCommands.selectOpponent(2)
        elif ("3" in phrase or "three" in phrase or "free" in phrase):
            voiceCommands.selectOpponent(3)
        elif ("4" in phrase or "four" in phrase or "for" in phrase):
            voiceCommands.selectOpponent(4)
        elif ("5" in phrase or "five" in phrase):
            voiceCommands.selectOpponent(5)
        elif ("6" in phrase or "six" in phrase):
            voiceCommands.selectOpponent(6)
        elif ("7" in phrase or "seven" in phrase or "for" in phrase):
            voiceCommands.selectOpponent(7)
        elif ("8" in phrase or "eight" in phrase):
            voiceCommands.selectOpponent(8)
        elif ("9" in phrase or "nine" in phrase):
            voiceCommands.selectOpponent(9)

    # Play game
    elif ("play game" in phrase):
        voiceCommands.playGame()
