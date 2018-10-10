
BUFFER_THRESHOLD = 5

class ButtonControl:
    def __init__(self):
        self._buttonState = False
        self._stateBuffer = []
        self._didClickButton = False
    
    def update(self):
        buttonState = self._getButtonState()
        if len(self._stateBuffer) > 0:
            self._stateBuffer.append(buttonState)
            self._checkStateBuffer()
        elif buttonState != self._buttonState:
            self._stateBuffer.append(buttonState)
        return
    
    def _checkStateBuffer(self):
        differentStates = 0
        sameStates = 0
        for i in range(len(self._stateBuffer)):
            if self._stateBuffer[i] == self._buttonState:
                sameStates += 1
            else:
                differentStates += 1
        
        if sameStates >= BUFFER_THRESHOLD:
            self._stateBuffer[:] = []
            return
        
        if differentStates >= BUFFER_THRESHOLD:
            if self._buttonState:
                self._didClickButton = True
                self._buttonState = False
            else:
                self._buttonState = True
            self._stateBuffer[:] = []
            return
    
    def didClickButton(self):
        if self._didClickButton:
            self._didClickButton = False
            return True
        else:
            return False
    
    def _getButtonState(self):
        # use wiring to read button
        return False

