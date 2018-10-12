
import wiringpi

BUTTON_0_SIGNAL = 17
BUTTON_0_LIGHT = 27
BUTTON_1_SIGNAL = 22
BUTTON_1_LIGHT = 5
BUTTON_2_SIGNAL = 6 
BUTTON_2_LIGHT = 13
BUTTON_3_SIGNAL = 19
BUTTON_3_LIGHT = 26

def setupPinModes():
    wiringpi.pinMode(BUTTON_0_SIGNAL, 0)
    wiringpi.pinMode(BUTTON_0_LIGHT, 1)
    wiringpi.pinMode(BUTTON_1_LIGHT, 1)
    wiringpi.pinMode(BUTTON_2_SIGNAL, 0)
    wiringpi.pinMode(BUTTON_2_LIGHT, 1)
    wiringpi.pinMode(BUTTON_3_SIGNAL, 0)
    wiringpi.pinMode(BUTTON_3_LIGHT, 1)

class TableConfig:
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        return

TABLES = [TableConfig(tableNumber) for tableNumber in [0,1,2,3]]
TABLES[0].lightPin = BUTTON_0_LIGHT
TABLES[0].signalPin = BUTTON_0_SIGNAL
TABLES[0].name = "Joe"
TABLES[0].joinSound = "sfx/joe-hi.wav"
TABLES[0].winSound = "sfx/joe-yay.wav"
TABLES[0].bonusSound = "sfx/joe-bonus.wav"
TABLES[0].lightColor = [232,87,0]
TABLES[1].lightPin = BUTTON_1_LIGHT
TABLES[1].signalPin = BUTTON_1_SIGNAL
TABLES[1].name = "Cassie"
TABLES[1].joinSound = "sfx/cassie-hi.wav"
TABLES[1].winSound = "sfx/cassie-yay.wav"
TABLES[1].bonusSound = "sfx/cassie-bonus.wav"
TABLES[1].lightColor = [0,255,162]
TABLES[2].lightPin = BUTTON_2_LIGHT
TABLES[2].signalPin = BUTTON_2_SIGNAL
TABLES[2].name = "Zombo"
TABLES[2].joinSound = "sfx/zombo-hi2.wav"
TABLES[2].winSound = "sfx/zombo-yay2.wav"
TABLES[2].bonusSound = "sfx/zombo-bonus2.wav"
TABLES[2].lightColor = [42,255,0]
TABLES[3].lightPin = BUTTON_3_LIGHT
TABLES[3].signalPin = BUTTON_3_SIGNAL
TABLES[3].name = "Willow"
TABLES[3].joinSound = "sfx/willow-hi.wav"
TABLES[3].winSound = "sfx/willow-yay.wav"
TABLES[3].bonusSound = "sfx/willow-bonus.wav"
TABLES[3].lightColor = [255,193,6]