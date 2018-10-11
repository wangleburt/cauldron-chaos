import SoundManager
import LobbyController
import GameController
import wiringpi
import TableConfig
import SkeletonManager
import JankyWindow

import pygame

wiringpi.wiringPiSetupGpio()
pygame.init()
TableConfig.setupPinModes()
SkeletonManager.setupPinModes()
JankyWindow.init()

soundManager = SoundManager.SoundManager()
lobbyController = LobbyController.LobbyController(soundManager)
gameController = GameController.GameController(soundManager)

SkeletonManager.skeletonDown()
while True:
    print("Start Lobby")
    soundManager.playLobbyMusic()
    lobbyController.runLobby()
    
    print("Start Game")
    soundManager.playGameMusic()
    gameController.setupNewGameWithTableNumbers(lobbyController.activeTableNumbers)
    gameController.runGame()
    
    if gameController.victory:
        SkeletonManager.skeletonUp()
        soundManager.playVictoryMusic()
        print("Victory")
    else:
        pass # TODO: play defeat sound effect
    
    print("End Game Idle")
    lobbyController.runEndGameIdle()
    SkeletonManager.skeletonDown()