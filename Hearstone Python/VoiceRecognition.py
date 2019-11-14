import speech_recognition as sr
import VoiceCommands
class VoiceRecognition:
    
    r = sr.Recognizer()
    mic = sr.Microphone()
    voiceCommands = VoiceCommands.VoiceCommands()

    def recognise(self) :
        # To Do: ambient noise stuff
        text = "error"
        try:
            with self.mic as source:
                # , timeout=2.0
                audio = self.r.listen(source)
            text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            text = "error"
        return text

    def takeInput(self):
        phrase = self.recognise()
        print("Recognised: " + phrase)

        # 
        # General commands
        #

        if (phrase == "exit voice"):
            self.voiceCommands.quitProgram()

        # 
        # Gameplay commands
        #

        elif (phrase == "end turn" or phrase == "and turn" or phrase == "entertain" or phrase == "nth term" or phrase == "Anton"):
            self.voiceCommands.endTurn()

        # 
        # Menu commands
        #

        # Navigate from main menu to single player deck selection
        elif (phrase == "single player"):
            self.voiceCommands.singlePlayer()
        
        # Select deck
        elif ("deck" in phrase or "dick" in phrase or "next" in phrase or "text" in phrase or "tech" in phrase or "EK" in phrase or "Jet" in phrase):
            if ("1" in phrase or "one" in phrase):
                self.voiceCommands.selectDeck(1)
            elif ("2" in phrase or "two" in phrase or "too" in phrase or "to" in phrase):
                self.voiceCommands.selectDeck(2)
            elif ("3" in phrase or "three" in phrase or "free" in phrase):
                self.voiceCommands.selectDeck(3)
            elif ("4" in phrase or "four" in phrase or "for" in phrase):
                self.voiceCommands.selectDeck(4)
            elif ("5" in phrase or "five" in phrase):
                self.voiceCommands.selectDeck(5)
            elif ("6" in phrase or "six" in phrase):
                self.voiceCommands.selectDeck(6)
            elif ("7" in phrase or "seven" in phrase or "for" in phrase):
                self.voiceCommands.selectDeck(7)
            elif ("8" in phrase or "eight" in phrase):
                self.voiceCommands.selectDeck(8)
            elif ("9" in phrase or "nine" in phrase):
                self.voiceCommands.selectDeck(9)
        elif ("dec1" in phrase or "daquan" in phrase):
            self.voiceCommands.selectDeck(1)
        elif ("dec2" in phrase or "bectu" in phrase):
            self.voiceCommands.selectDeck(2)
        elif ("dec3" in phrase or "Dec free" in phrase):
            self.voiceCommands.selectDeck(3)
        elif ("dec4" in phrase):
            self.voiceCommands.selectDeck(4)
        elif ("dec5" in phrase):
            self.voiceCommands.selectDeck(5)
        elif ("dec6" in phrase):
            self.voiceCommands.selectDeck(6)
        elif ("dec7" in phrase):
            self.voiceCommands.selectDeck(4)
        elif ("dec8" in phrase):
            self.voiceCommands.selectDeck(5)
        elif ("dec9" in phrase):
            self.voiceCommands.selectDeck(6)

        # Select enemy
        elif ("opponent" in phrase or "appointment" in phrase or "exponent" in phrase):
            if ("1" in phrase):
                self.voiceCommands.selectOpponent(1)
            elif ("2" in phrase or "two" in phrase):
                self.voiceCommands.selectOpponent(2)
            elif ("3" in phrase or "three" in phrase or "free" in phrase):
                self.voiceCommands.selectOpponent(3)
            elif ("4" in phrase or "four" in phrase or "for" in phrase):
                self.voiceCommands.selectOpponent(4)
            elif ("5" in phrase or "five" in phrase):
                self.voiceCommands.selectOpponent(5)
            elif ("6" in phrase or "six" in phrase):
                self.voiceCommands.selectOpponent(6)
            elif ("7" in phrase or "seven" in phrase or "for" in phrase):
                self.voiceCommands.selectOpponent(7)
            elif ("8" in phrase or "eight" in phrase):
                self.voiceCommands.selectOpponent(8)
            elif ("9" in phrase or "nine" in phrase):
                self.voiceCommands.selectOpponent(9)

        # Play game
        elif ("play game" in phrase):
            self.voiceCommands.playGame()
