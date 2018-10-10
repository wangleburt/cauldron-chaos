import ButtonLight
import ButtonControl
import TableConfig

class LobbyTable:
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        tableConfig = TableConfig.TABLES[tableNumber]
        self.light = ButtonLight.ButtonLight(tableConfig)
        self.button = ButtonControl.ButtonControl(tableConfig)
    
    def update(self, timeSinceLastUpdate):
        self.light.update(timeSinceLastUpdate)
        self.button.update()