
import wiringpi

ACTUATOR_RELAY_1 = 20
ACTUATOR_RELAY_2 = 21
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
TABLES[1].lightPin = BUTTON_1_LIGHT
TABLES[1].signalPin = BUTTON_1_SIGNAL
TABLES[2].lightPin = BUTTON_2_LIGHT
TABLES[2].signalPin = BUTTON_2_SIGNAL
TABLES[3].lightPin = BUTTON_3_LIGHT
TABLES[3].signalPin = BUTTON_3_SIGNAL
