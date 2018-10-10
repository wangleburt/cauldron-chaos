GREEN_SCORE = 10
YELLOW_SCORE = 30
PURPLE_SCORE = 50

WINNING_SCORE_PER_TABLE = 200

def winningScoreForTableCount(tableCount):
    return tableCount * WINNING_SCORE_PER_TABLE;

class ScoreKeeper:
    def __init__(self):
        self.scores = [0, 0, 0, 0]
    
    def scoreForTeam(self):
        total = 0;
        for i in range(len(self.scores)):
            total += self.scores[i]
        return total;
    
    def scoreForTable(self, tableNumber):
        if tableNumber >= 0 and tableNumber < len(self.scores):
            return self.scores[tableNumber]
        else:
            return 0
    
    def addPointsForTable(self, tableNumber, points):
        if tableNumber >= 0 and tableNumber < len(self.scores):
            self.scores[tableNumber] += points
        return;
