import ScoreKeeper
import GameTable
import SoundManager
from time import sleep

# all times in seconds
GAME_TIME = 5
MULTIPLIER_TIME = 5
TIME_PER_CYCLE = 0.05

class GameController:
    
    def __init__(self, soundManager):
        self._soundManager = soundManager
        return;
    
    def setupNewGameWithTableNumbers(self, tableNumbers):
        self._scoreKeeper = ScoreKeeper.ScoreKeeper()
        self._tables = [GameTable.GameTable(tableNumber) for tableNumber in tableNumbers]
        self._timeRemaining = GAME_TIME
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
        for table in self._tables:
            table.scoreboard.tableScore = self._scoreKeeper.scoreForTable(table.tableNumber)
            table.scoreboard.teamScore = self._scoreKeeper.scoreForTeam()
            table.scoreboard.updateDisplay()
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
            self._soundManager.playScoreSound()
        elif score == ScoreKeeper.PURPLE_SCORE:
            self._soundManager.playPowerupSound()
        return;

    def runGame(self):
        self._soundManager.playGameMusic()
        cycle = 0
        while self._timeRemaining > 0:
            sleep(TIME_PER_CYCLE)
            self._update(TIME_PER_CYCLE)
            
            # debug output
            print("Team: " + str(self._scoreKeeper.scoreForTeam()))
            print("Multiplier: " + str(self._calculateMultiplier()))
            print(self._timeRemaining)
            cycle += 1
            if cycle % 10 == 0:
                index = (cycle % 7) % len(self._tables)
                if index == 0:
                    self._tables[index].pendingScore = ScoreKeeper.PURPLE_SCORE
                else:
                    self._tables[index].pendingScore = ScoreKeeper.GREEN_SCORE
        
        score = self._scoreKeeper.scoreForTeam()
        winningScore = ScoreKeeper.winningScoreForTableCount(len(self._tables))
        self.victory = (score >= winningScore)
        return
        
    