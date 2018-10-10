import ButtonLight
import ButtonControl

class LobbyTable:
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        self.light = ButtonLight.ButtonLight()
        self.button = ButtonControl.ButtonControl()
    
    def update(self, timeSinceLastUpdate):
        self.light.update(timeSinceLastUpdate)
        self.button.update()