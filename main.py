import SoundManager
import LobbyController
import GameController

import pygame


pygame.init()

soundManager = SoundManager.SoundManager()

lobbyController = LobbyController.LobbyController(soundManager)
gameController = GameController.GameController(soundManager)


gameController.setupNewGameWithTableNumbers([0,1,3])
gameController.runGame()

'''
while True:
    lobbyController.runLobby()
    gameController.setupNewGameWithTableNumbers(lobbyController.activeTableNumbers)
    gameController.runGame()
    if gameController.victory:
        pass # TODO: do victory stuff
    else:
        pass # TODO: do defeat stuff
'''