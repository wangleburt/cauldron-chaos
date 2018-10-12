import ScoreKeeper
import GameTable
import SoundManager
import JankyWindow
from time import sleep

# all times in seconds
GAME_TIME = 60
MULTIPLIER_TIME = 5
TIME_PER_CYCLE = 0.05
SOUND_EFFECT_DELAY = 0.3

class GameController:
    
    def __init__(self, soundManager):
        self._soundManager = soundManager
        return;
    
    def setupNewGameWithTableNumbers(self, tableNumbers):
        self._scoreKeeper = ScoreKeeper.ScoreKeeper()
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
        self._updateTableScores()
        self._updateTableScoreboards()
        return;

    def _updateTableScores(self):
        for table in self._tables:
            table.update()
            if table.pendingScore != 0:
                score = table.pendingScore
                self._playSoundForScore(score)
                if score == ScoreKeeper.PURPLE_SCORE:
                    self._addNewMultiplier()
                score *= self._calculateMultiplier()
                self._scoreKeeper.addPointsForTable(table.tableNumber, score)
                table.pendingScore = 0
        return;
    
    def _updateTableScoreboards(self):
        score = self._scoreKeeper.scoreForTeam()
        print("Score: " + str(score) + " / " + str(self._winningScore))
        for table in self._tables:
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
        return pow(2, len(self._multipliers))

    def _playSoundForScore(self, score):
        if score == ScoreKeeper.GREEN_SCORE:
            if self._lastSoundPlayed > self._timeRemaining + SOUND_EFFECT_DELAY:
                self._soundManager.playScoreSound()
                self._lastSoundPlayed = self._timeRemaining
        elif score == ScoreKeeper.PURPLE_SCORE:
            self._soundManager.playPowerupSound()
        return;

    def runGame(self):
        while self._timeRemaining > 0:
            sleep(TIME_PER_CYCLE)
            self._update(TIME_PER_CYCLE)
            print("Game time remaining: " + str(self._timeRemaining))
            if JankyWindow.didClickMouse():
                self._tables[0].pendingScore = ScoreKeeper.GREEN_SCORE
            score = self._scoreKeeper.scoreForTeam()
            if score >= self._winningScore:
                self.victory = True
                break
        return
        
    