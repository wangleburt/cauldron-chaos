
import wiringpi

# light state enum
OFF = 0
ON = 1
CYCLE_BLINK = 2
CYCLE_FLICKER = 3

# cycle state enum
CYCLE_STATE_OFF = 0
CYCLE_STATE_ON = 1

# seconds
BLINK_CYCLE_TIME = 1
FLICKER_CYCLE_TIME = 0.2

class ButtonLight:
    def __init__(self, tableConfig):
        self._lightState = OFF
        self._cycleState = CYCLE_STATE_OFF
        self._cycleCountdown = 0
        self._cycleTime = 0
        self._tableConfig = tableConfig
        return
    
    def update(self, timeSinceLastUpdate):
        if self._cycleTime == 0:
            return
        self._cycleCountdown -= timeSinceLastUpdate
        if (self._cycleCountdown <= 0):
            self._cycleCountdown = self._cycleTime
            if self._cycleState == CYCLE_STATE_OFF:
                self._lightOn()
                self._cycleState = CYCLE_STATE_ON
            elif self._cycleState == CYCLE_STATE_ON:
                self._lightOff()
                self._cycleState = CYCLE_STATE_OFF
        
    
    def setLightState(self, lightState):
        self._lightState = lightState
        if lightState == OFF:
            self._lightOff()
            self._cycleTime = 0
            
        elif lightState == ON:
            self._lightOn()
            self._cycleTime = 0
            
        elif lightState == CYCLE_BLINK:
            self._lightOff()
            self._cycleState = CYCLE_STATE_OFF
            self._cycleTime = BLINK_CYCLE_TIME
            self._cycleCountdown = self._cycleTime
            
        elif lightState == CYCLE_FLICKER:
            self._lightOff()
            self._cycleState = CYCLE_STATE_OFF
            self._cycleTime = FLICKER_CYCLE_TIME
            self._cycleCountdown = self._cycleTime
        return
        
    
    def _lightOn(self):
        pin = self._tableConfig.lightPin
        wiringpi.digitalWrite(pin, 1)
    
    def _lightOff(self):
        pin = self._tableConfig.lightPin
        wiringpi.digitalWrite(pin, 0)