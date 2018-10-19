import ScoreKeeper

def logGame(scoreKeeper):
    file = open("logs.txt", "a")
    file.write("score: %d, normies: %d, purples: %d\n"%(scoreKeeper.score,scoreKeeper.normies,scoreKeeper.purples))
    file.close()
    return
    