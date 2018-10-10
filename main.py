import SoundManager
import LobbyController
import GameController
import wiringpi
import TableConfig
import SkeletonManager

import pygame

wiringpi.wiringPiSetupGpio()
pygame.init()
TableConfig.setupPinModes()
SkeletonManager.setupPinModes()

soundManager = SoundManager.SoundManager()
lobbyController = LobbyController.LobbyController(soundManager)
gameController = GameController.GameController(soundManager)

SkeletonManager.skeletonDown()
while True:
    lobbyController.runLobby()
    gameController.setupNewGameWithTableNumbers(lobbyController.activeTableNumbers)
    gameController.runGame()
    if gameController.victory:
        SkeletonManager.skeletonUp()
        # TODO: play victory sound effect
    else:
        pass # TODO: play defeat sound effect