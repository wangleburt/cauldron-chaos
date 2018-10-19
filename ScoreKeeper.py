GREEN_SCORE = 10
YELLOW_SCORE = 30
PURPLE_SCORE = 50

WINNING_SCORE_PER_TABLE = 200

def winningScoreForTableCount(tableCount):
    return tableCount * WINNING_SCORE_PER_TABLE;

class ScoreKeeper:
    def __init__(self):
        self.score = 0
        self.normies = 0
        self.purples = 0