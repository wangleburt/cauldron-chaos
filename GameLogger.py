import ScoreKeeper

def logGame(scoreKeeper):
    file = open("logs.txt", "a")
    file.write("score: %d\n"%(scoreKeeper.scoreForTeam()))
    file.close()
    return
    