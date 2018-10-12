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

PixelBoard.clearStrip()
SkeletonManager.skeletonDown()
while True:
    print("Start Lobby")
    soundManager.playLobbyMusic()
    lobbyController.runLobby()
    activeTableNumbers = lobbyController.activeTableNumbers
    
    print("Start Game")
    soundManager.playGameMusic()
    gameController.setupNewGameWithTableNumbers(activeTableNumbers)
    gameController.runGame()
    
    if gameController.victory:
        SkeletonManager.skeletonUp()
        soundManager.playVictoryMusic()
        for tableNumber in activeTableNumbers:
            soundManager.playWinSoundForTable(tableNumber)
        print("Victory")
        sleep(1.5)
        soundManager.playVictorySound()
        print("End Game Idle")
        lobbyController.runEndGameIdle()
        SkeletonManager.skeletonDown()
    else:
        pass