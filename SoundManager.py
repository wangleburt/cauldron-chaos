import pygame
import TableConfig

class TableSoundPack:
    pass

class SoundManager:
    def __init__(self):
        self.scoreSound = pygame.mixer.Sound("sfx/points-green.wav")
        self.scoreSound.set_volume(0.6)
        self.powerupSound = pygame.mixer.Sound("sfx/points-purple.wav")
        self.victorySound = pygame.mixer.Sound("sfx/fanfare.wav")
        self.skeletonSound = pygame.mixer.Sound("sfx/skeleton-rant.wav")
        self.startingSound = pygame.mixer.Sound("sfx/ready-set-go.wav")
        self.startingSound.set_volume(0.3)
        self.failSound = pygame.mixer.Sound("sfx/buzzer.wav")
        self.tableSounds = [TableSoundPack() for i in range(4)]
        for i in range(4):
            config = TableConfig.TABLES[i]
            self.tableSounds[i].joinSound = pygame.mixer.Sound(config.joinSound)
            self.tableSounds[i].joinSound.set_volume(config.soundVolume)
            self.tableSounds[i].winSound = pygame.mixer.Sound(config.winSound)
            self.tableSounds[i].winSound.set_volume(config.soundVolume)
            self.tableSounds[i].bonusSound = pygame.mixer.Sound(config.bonusSound)
            self.tableSounds[i].bonusSound.set_volume(config.soundVolume)
        self.lobbyMusic = pygame.mixer.Sound("music/Lobby Music 1.ogg")
        self.lobbyMusic.set_volume(0.8)
        self.gameMusic = pygame.mixer.Sound("music/Game Music 1.ogg")
        self.currentMusic = None
        return;
    
    def playScoreSound(self):
        self.scoreSound.play()
        return;
    
    def playPowerupSound(self):
        self.powerupSound.play()
        return;
    
    def playJoinSoundForTable(self, tableNumber):
        self.tableSounds[tableNumber].joinSound.play()
        return
    
    def playWinSoundForTable(self, tableNumber):
        self.tableSounds[tableNumber].winSound.play()
        return
    
    def playBonusSoundForTable(self, tableNumber):
        self.tableSounds[tableNumber].bonusSound.play()
        return
    
    def playStartingSound(self):
        self.startingSound.play()
        return
    
    def playVictorySound(self):
        self.victorySound.play()
        return
    
    def playFailSound(self):
        self.failSound.play()
        return
    
    def playSkeletonSound(self):
        self.skeletonSound.play()
        return
    
    def playLobbyMusic(self):
        if self.currentMusic is self.lobbyMusic:
            return
        if self.currentMusic is not None:
            self.currentMusic.stop()
        self.lobbyMusic.play(-1)
        self.currentMusic = self.lobbyMusic
        return
    
    def playGameMusic(self):
        if self.currentMusic is self.gameMusic:
            return
        if self.currentMusic is not None:
            self.currentMusic.stop()
        self.gameMusic.play(-1)
        self.currentMusic = self.gameMusic
        return
    
    def stopMusic(self):
        if self.currentMusic is not None:
            self.currentMusic.stop()
            self.currentMusic = None
        return
    
    def playVictoryMusic(self):
        pass