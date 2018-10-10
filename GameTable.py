import ScoreKeeper

class ScoreBoard:
    
    def __init__(self, tableNumber):
        self.tableScore = 0
        self.teamScore = 0
        self.tableNumber = tableNumber
        return;
    
    def updateDisplay(self):
        print("Table " + str(self.tableNumber) + ": " + str(self.tableScore))
        return;

class GameTable:
    
    def __init__(self, tableNumber):
        self.tableNumber = tableNumber
        self.pendingScore = 0
        self.scoreboard = ScoreBoard(tableNumber)
        return;
    
    def update(self):
        # currentLaserState = check lasers for current state
        # if currentLaserState == blank and lastLaserState != blank
        #     self.pendingScore = pointsForState(lastLaserState)
        # self.lastLaserState = currentLaserState
        return;
    
