# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - Achievement.py

# Module imports needed for class
import pygame
pygame.init()

# Class for achievements
class Achievement(object):
    # Initialization/Constructor method
    def __init__(self, x, y, achievementName):
        self.x = x
        self.y = y
        self.achievementName = achievementName
        self.lockedSprite = pygame.image.load('assets/images/lockedAchievement.png')
        self.unlockedSprite = pygame.image.load('assets/images/unlockedAchievement.png')
        self.sprite = self.lockedSprite
    
    # Method which draws the achievement on-screen
    def output(self, window):
        window.blit(self.sprite, (self.x, self.y))
        window.blit(pygame.font.SysFont('Callibri', 25).render(self.achievementName, 1, (0, 0, 0)), (self.x, self.y - 20))