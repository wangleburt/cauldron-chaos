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
        startingTime = 15
        timeRemaining = startingTime
        JankyWindow.clear()
        for table in self._tables:
            table.light.setLightState(ButtonLight.OFF)
        while timeRemaining > 0:
            sleep(TIME_PER_CYCLE)
            timeRemaining -= TIME_PER_CYCLE
            if timeRemaining < startingTime - 8:
                if JankyWindow.didClickMouse():
                    break;
            else:
                JankyWindow.idle()
        return
    
    def runLobby(self):
        timeRemaining = LOBBY_TIME
        self.activeTableNumbers[:] = []
        activeTables = []
        for table in self._tables:
            table.light.setLightState(ButtonLight.CYCLE_BLINK)
        JankyWindow.clear()
        while timeRemaining > 0:
            sleep(TIME_PER_CYCLE)
            if len(activeTables) > 0:
                timeRemaining -= TIME_PER_CYCLE
                print("Lobby time remaining: " + str(timeRemaining))
                if JankyWindow.didClickMouse():
                    break
            else:
                JankyWindow.idle()
            for table in self._tables:
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    if table not in activeTables:
                        activeTables.append(table)
                        table.light.setLightState(ButtonLight.ON)
                        self._soundManager.playJoinSoundForTable(table.tableNumber)
                        JankyWindow.clear()
                        print(table.name + " joined")
            if len(activeTables) >= len(self._tables):
                break
        for i in range(4):
            self.activeTableNumbers.append(i)
        for table in self._tables:
            table.light.setLightState(ButtonLight.ON)
        return
    
    def runStartingSequence(self):
        self._soundManager.playStartingSound()
        #TODO: play fancy flashing/fading sequence
        sleep(3.5)