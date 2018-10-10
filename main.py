import SoundManager
import LobbyController
import GameController
import wiringpi
import TableConfig

import pygame

wiringpi.wiringPiSetupGpio()
pygame.init()
TableConfig.setupPinModes()

soundManager = SoundManager.SoundManager()

lobbyController = LobbyController.LobbyController(soundManager)
gameController = GameController.GameController(soundManager)

'''
gameController.setupNewGameWithTableNumbers([0,1,3])
gameController.runGame()
'''

while True:
    lobbyController.runLobby()
    print(lobbyController.activeTableNumbers)
    gameController.setupNewGameWithTableNumbers(lobbyController.activeTableNumbers)
    gameController.runGame()
    if gameController.victory:
        pass # TODO: do victory stuff
    else:
        pass # TODO: do defeat stuff