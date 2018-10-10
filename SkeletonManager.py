
import wiringpi

ACTUATOR_RELAY_1 = 20
ACTUATOR_RELAY_2 = 21

def setupPinModes():
    wiringpi.pinMode(ACTUATOR_RELAY_1, 1)
    wiringpi.pinMode(ACTUATOR_RELAY_2, 1)
    return

def skeletonUp():
    wiringpi.digitalWrite(ACTUATOR_RELAY_1, 1)
    wiringpi.digitalWrite(ACTUATOR_RELAY_2, 0)
    return

def skeletonDown():
    wiringpi.digitalWrite(ACTUATOR_RELAY_1, 0)
    wiringpi.digitalWrite(ACTUATOR_RELAY_2, 1)
    return