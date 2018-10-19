import ScoreKeeper
import GameTable
import SoundManager
import JankyWindow
import ButtonControl
from time import sleep

# all times in seconds
GAME_TIME = 60
MULTIPLIER_TIME = 5
TIME_PER_CYCLE = 0.01
SOUND_EFFECT_DELAY = 0.3

class GameController:
    
    def __init__(self, soundManager):
        self._soundManager = soundManager
        return;
    
    def setupNewGameWithTableNumbers(self, tableNumbers):
        self.scoreKeeper = ScoreKeeper.ScoreKeeper()
        self._winningScore = ScoreKeeper.winningScoreForTableCount(len(tableNumbers))
        self._tables = [GameTable.GameTable(tableNumber) for tableNumber in tableNumbers]
        for table in self._tables:
            table.scoreboard.winningScore = self._winningScore
            table.scoreboard.gameTime = GAME_TIME
        self._timeRemaining = GAME_TIME
        self._lastSoundPlayed = GAME_TIME + SOUND_EFFECT_DELAY*2
        self._multipliers = []
        self.victory = False
        return;
    
    def _update(self, timeSinceLastUpdate):
        self._timeRemaining -= timeSinceLastUpdate
        self._updateMultipliers()
        self._updateTables(timeSinceLastUpdate)
        self._updateTableScoreboards()
        return;

    def _updateTables(self, timeSinceLastUpdate):
        for table in self._tables:
            table.update(timeSinceLastUpdate)
            if table.pendingScore != 0:
                score = table.pendingScore
                self._playSoundForScore(score)
                score *= self._calculateMultiplier()
                if table.pendingScore == ScoreKeeper.PURPLE_SCORE:
                    self._addNewMultiplier()
                    self.scoreKeeper.purples += 1
                else:
                    self.scoreKeeper.normies += 1
                self.scoreKeeper.score += score
                table.pendingScore = 0
            if table.button.didClickButton():
                self._soundManager.playJoinSoundForTable(table.tableNumber)
        return;
    
    def _updateTableScoreboards(self):
        score = self.scoreKeeper.score
        print("Score: " + str(score) + " / " + str(self._winningScore))
        for table in self._tables:
            table.scoreboard.multiplierMode = (len(self._multipliers) > 0)
            table.scoreboard.updateDisplay(score, self._timeRemaining)
        return;
    
    def _updateMultipliers(self):
        timeout = lambda time : time > self._timeRemaining
        self._multipliers[:] = [time for time in self._multipliers if not timeout(time)]
        return;
    
    def _addNewMultiplier(self):
        multiplierTime = self._timeRemaining - MULTIPLIER_TIME
        self._multipliers.append(multiplierTime)
        return;
    
    def _calculateMultiplier(self):
        #return pow(2, len(self._multipliers))
        return 2 if len(self._multipliers) > 0 else 1

    def _playSoundForScore(self, score):
        if score == ScoreKeeper.GREEN_SCORE:
            if self._lastSoundPlayed > self._timeRemaining + SOUND_EFFECT_DELAY:
                self._soundManager.playScoreSound()
                self._lastSoundPlayed = self._timeRemaining
        elif score == ScoreKeeper.PURPLE_SCORE:
            if self._lastSoundPlayed > self._timeRemaining + SOUND_EFFECT_DELAY:
                self._soundManager.playPowerupSound()
                self._lastSoundPlayed = self._timeRemaining
        return;

    def runGame(self):
        JankyWindow.clear()
        while self._timeRemaining > 0:
            sleep(TIME_PER_CYCLE)
            self._update(TIME_PER_CYCLE)
            print("Game time remaining: " + str(self._timeRemaining))
            click = JankyWindow.clickType()
            if click == JankyWindow.MOUSE_LEFT:
                self._tables[0].pendingScore = ScoreKeeper.GREEN_SCORE
            elif click == JankyWindow.MOUSE_RIGHT:
                self._tables[1].pendingScore = ScoreKeeper.PURPLE_SCORE
            if self.scoreKeeper.score >= self._winningScore:
                self.victory = True
                break
        return
        
    