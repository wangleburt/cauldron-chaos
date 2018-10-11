import pygame

class SoundManager:
    def __init__(self):
        self.scoreSound = pygame.mixer.Sound("sfx/points.wav")
        self.powerupSound = pygame.mixer.Sound("sfx/powerup.wav")
        return;
    
    def playScoreSound(self):
        self.scoreSound.play()
        return;
    
    def playPowerupSound(self):
        self.powerupSound.play()
        return;
    
    def playJoinSoundForTable(self, tableNumber):
        self.scoreSound.play()
        return
    
    def playLobbyMusic(self):
        pass
    
    def playGameMusic(self):
        pass
    
    def playVictoryMusic(self):
        pass