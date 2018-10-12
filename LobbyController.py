import SoundManager
import LobbyTable
import ButtonLight
import ButtonControl
import JankyWindow
from time import sleep

TIME_PER_CYCLE = 0.005
LOBBY_TIME = 15

class LobbyController:
    def __init__(self, soundManager):
        self._soundManager = soundManager
        self._tables = [LobbyTable.LobbyTable(tableNumber) for tableNumber in range(4)]
        self.activeTableNumbers = []
        return
    
    def runEndGameIdle(self):
        running = True
        for table in self._tables:
            table.light.setLightState(ButtonLight.OFF)
        while running:
            sleep(TIME_PER_CYCLE)
            JankyWindow.idle()
            for table in self._tables:
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    running = False
                    break
        return
    
    def runLobby(self):
        timeRemaining = LOBBY_TIME
        self.activeTableNumbers[:] = []
        activeTables = []
        for table in self._tables:
            table.light.setLightState(ButtonLight.CYCLE_BLINK)
        while timeRemaining > 0:
            sleep(TIME_PER_CYCLE)
            JankyWindow.idle()
            if len(activeTables) > 0:
                timeRemaining -= TIME_PER_CYCLE
                print("Lobby time remaining: " + str(timeRemaining))
            for table in self._tables:
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    if table in activeTables:
                        timeRemaining -= 3
                        print(table.name + " is impatient!")
                    else:
                        activeTables.append(table)
                        table.light.setLightState(ButtonLight.ON)
                        self._soundManager.playJoinSoundForTable(table.tableNumber)
                        print(table.name + " joined")
            if len(activeTables) >= len(self._tables):
                break
        for table in activeTables:
            self.activeTableNumbers.append(table.tableNumber)
        for table in self._tables:
            if table in activeTables:
                table.light.setLightState(ButtonLight.ON)
            else:
                table.light.setLightState(ButtonLight.OFF)
        return
    
    def runStartingSequence(self):
        self._soundManager.playStartingSound()
        #TODO: play fancy flashing/fading sequence
        sleep(3.5)
    
    '''
    def runLobby(self):
        self.activeTableNumbers[:] = []
        self._waitForInit()
        activeTables = self._waitForActiveTables()
        for table in activeTables:
            self.activeTableNumbers.append(table.tableNumber)
        return
    '''
    
    def _waitForInit(self):
        leadTable = self._tables[0]
        print("Waiting for " + leadTable.name + " to start the lobby...")
        leadTable.light.setLightState(ButtonLight.CYCLE_BLINK)
        self._tables[1].light.setLightState(ButtonLight.OFF)
        self._tables[2].light.setLightState(ButtonLight.OFF)
        self._tables[3].light.setLightState(ButtonLight.OFF)
        while True:
            sleep(TIME_PER_CYCLE)
            JankyWindow.idle()
            leadTable.update(TIME_PER_CYCLE)
            if leadTable.button.didClickButton():
                print(leadTable.name + " started the lobby")
                leadTable.light.setLightState(ButtonLight.ON)
                self._soundManager.playJoinSoundForTable(leadTable.tableNumber)
                self._tables[1].light.setLightState(ButtonLight.CYCLE_BLINK)
                self._tables[2].light.setLightState(ButtonLight.CYCLE_BLINK)
                self._tables[3].light.setLightState(ButtonLight.CYCLE_BLINK)
                break
        return
    
    def _waitForActiveTables(self):
        print("Waiting for others...")
        leadTable = self._tables[0]
        activeTables = [leadTable]
        while True:
            sleep(TIME_PER_CYCLE)
            JankyWindow.idle()
            leadTable.update(TIME_PER_CYCLE)
            if leadTable.button.didClickButton():
                print(leadTable.name + " says go!")
                return activeTables
            
            for tableNumber in [1,2,3]:
                table = self._tables[tableNumber]
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    if table not in activeTables:
                        print(table.name + " joined")
                        activeTables.append(table)
                        self._soundManager.playJoinSoundForTable(tableNumber)
                        table.light.setLightState(ButtonLight.ON)
                    else:
                        print(table.name + " left")
                        activeTables.remove(table)
                        table.light.setLightState(ButtonLight.CYCLE_BLINK)
        return []
                        
                    