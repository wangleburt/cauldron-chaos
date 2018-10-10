import SoundManager
import LobbyTable
import ButtonLight
import ButtonControl
import SkeletonManager
from time import sleep

TIME_PER_CYCLE = 0.005

class LobbyController:
    def __init__(self, soundManager):
        self._soundManager = soundManager
        self._tables = [LobbyTable.LobbyTable(tableNumber) for tableNumber in range(4)]
        self.activeTableNumbers = []
        return
    
    def runLobby(self):
        self._soundManager.playLobbyMusic()
        self.activeTableNumbers[:] = []
        self._waitForInit()
        SkeletonManager.skeletonDown()
        activeTables = self._waitForActiveTables()
        for table in activeTables:
            self.activeTableNumbers.append(table.tableNumber)
        return
    
    def _waitForInit(self):
        leadTable = self._tables[0]
        leadTable.light.setLightState(ButtonLight.CYCLE_BLINK)
        self._tables[1].light.setLightState(ButtonLight.OFF)
        self._tables[2].light.setLightState(ButtonLight.OFF)
        self._tables[3].light.setLightState(ButtonLight.OFF)
        while True:
            sleep(TIME_PER_CYCLE)
            leadTable.update(TIME_PER_CYCLE)
            if leadTable.button.didClickButton():
                leadTable.light.setLightState(ButtonLight.ON)
                # TODO: play sound effect for lead table
                self._tables[1].light.setLightState(ButtonLight.CYCLE_BLINK)
                self._tables[2].light.setLightState(ButtonLight.CYCLE_BLINK)
                self._tables[3].light.setLightState(ButtonLight.CYCLE_BLINK)
                break
        return
    
    def _waitForActiveTables(self):
        leadTable = self._tables[0]
        activeTables = [leadTable]
        while True:
            sleep(TIME_PER_CYCLE)
            leadTable.update(TIME_PER_CYCLE)
            if leadTable.button.didClickButton():
                return activeTables
            
            for tableNumber in [1,2,3]:
                table = self._tables[tableNumber]
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    if table not in activeTables:
                        activeTables.append(table)
                        # TODO: play sound effect for table
                        table.light.setLightState(ButtonLight.ON)
                    else:
                        activeTables.remove(table)
                        table.light.setLightState(ButtonLight.CYCLE_BLINK)
        return []
                        
                    