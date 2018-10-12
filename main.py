import SoundManager
import LobbyController
import GameController
import wiringpi
import TableConfig
import SkeletonManager
import JankyWindow

import pygame
from time import sleep

wiringpi.wiringPiSetupGpio()
pygame.init()
TableConfig.setupPinModes()
SkeletonManager.setupPinModes()
JankyWindow.init()

soundManager = SoundManager.SoundManager()
lobbyController = LobbyController.LobbyController(soundManager)
gameController = GameController.GameController(soundManager)

SkeletonManager.skeletonDown()
soundManager.playLobbyMusic()
while True:
    print("Start Lobby")
    lobbyController.runLobby()
    activeTableNumbers = lobbyController.activeTableNumbers
    
    soundManager.stopMusic()
    lobbyController.runStartingSequence()
    
    print("Start Game")
    soundManager.playGameMusic()
    gameController.setupNewGameWithTableNumbers(activeTableNumbers)
    gameController.runGame()
    
    soundManager.playLobbyMusic()
    if gameController.victory:
        SkeletonManager.skeletonUp()
        soundManager.playVictorySound()
        print("Victory")
        sleep(1.5)
        soundManager.playSkeletonSound()
        print("End Game Idle")
        lobbyController.runEndGameIdle()
        SkeletonManager.skeletonDown()
    else:
        soundManager.playFailSound()
    