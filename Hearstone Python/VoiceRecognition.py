import speech_recognition as sr
class VoiceRecognition:
    
    r = sr.Recognizer()
    mic = sr.Microphone()

    def recognise(self) :
        text = "error"
        try:
            with self.mic as source:
                audio = self.r.listen(source)
            text = self.r.recognize_google(audio)
        except sr.UnknownValueError:
            text = "error"
        return text
