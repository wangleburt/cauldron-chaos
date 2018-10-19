import SoundManager
import LobbyTable
import ButtonLight
import ButtonControl
import JankyWindow
import LightBoard
import TableConfig
from time import sleep

TIME_PER_CYCLE = 0.005
LOBBY_TIME = 15

class LobbyController:
    def __init__(self, soundManager):
        self._soundManager = soundManager
        self._tables = [LobbyTable.LobbyTable(tableNumber) for tableNumber in range(4)]
        self.activeTableNumbers = [0,1,2,3]
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
            for table in self._tables:
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    self._soundManager.playJoinSoundForTable(table.tableNumber)
        return
    
    def runLobby(self):
        for table in self._tables:
            table.light.setLightState(ButtonLight.CYCLE_BLINK)
        JankyWindow.clear()
        antiClickTime = 5
        while True:
            sleep(TIME_PER_CYCLE)
            antiClickTime -= TIME_PER_CYCLE
            if antiClickTime < 0:
                if JankyWindow.didClickMouse():
                    break
            else:
                JankyWindow.idle()
            for table in self._tables:
                table.update(TIME_PER_CYCLE)
                if table.button.didClickButton():
                    table.light.setLightState(ButtonLight.ON)
                    self._soundManager.playJoinSoundForTable(table.tableNumber)
        for table in self._tables:
            table.light.setLightState(ButtonLight.ON)
        return
    
    def runStartingSequence(self):
        self._soundManager.playStartingSound()
        sleep(0.6)
        for x in range(3):
            for i in range(101):
                percent = (100-i)/100.0
                for tableNumber in range(4):
                    stripNumber = 2*tableNumber
                    color = TableConfig.TABLES[tableNumber].lightColor
                    LightBoard.setStrip(stripNumber, 1, int(color[0]*percent), int(color[1]*percent), int(color[2]*percent))
                    stripNumber += 1
                    LightBoard.setStrip(stripNumber, 1, int(color[0]*percent), int(color[1]*percent), int(color[2]*percent))
                sleep(0.01)
        #TODO: play fancy flashing/fading sequence
        #sleep(0.5)