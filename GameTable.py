import LightBoard
import ButtonControl
import TableConfig

class ScoreBoard:
    
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        self.winningScore = 0
        self.gameTime = 0
        self.multiplierMode = False
        return
    
    def updateDisplay(self, score, timeRemaining):
        # start with score strip
        stripNumber = 2*self.tableNumber
        percent = score / float(self.winningScore)
        #print("score percent: " + str(percent))
        color = TableConfig.TABLES[self.tableNumber].lightColor
        if self.multiplierMode:
            color = [255,0,255]
        LightBoard.setStrip(stripNumber, percent, color[0], color[1], color[2])
        
        # next show time strip
        stripNumber += 1
        if not self.multiplierMode:
            color = TableConfig.TABLES[self.tableNumber].lightColor
        percent = timeRemaining / float(self.gameTime)
        #print("time percent: " + str(percent))
        LightBoard.setStrip(stripNumber, percent, color[0], color[1], color[2])
        return

class GameTable:
    
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        self.pendingScore = 0
        self.scoreboard = ScoreBoard(tableNumber)
        self.button = ButtonControl.ButtonControl(TableConfig.TABLES[tableNumber])
        return
    
    def update(self, timeSinceLastUpdate):
        self.button.update()
        # currentLaserState = check lasers for current state
        # if currentLaserState == blank and lastLaserState != blank
        #     self.pendingScore = pointsForState(lastLaserState)
        # self.lastLaserState = currentLaserState
        return
    