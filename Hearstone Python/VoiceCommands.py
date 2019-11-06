import MouseControl

class VoiceCommands:

    mouseControl = MouseControl.MouseControl()

    def endTurn(self):
        self.mouseControl.clickFraction(0.82, 0.45)