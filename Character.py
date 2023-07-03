# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - character.py

# Module imports needed for the class
import pygame
pygame.init()

# Class for the player/character
class Character(object):
    # Initialization/Constructor method
    def __init__(self):
        self.x = 325
        self.y = 410
        self.width = pygame.image.load('assets/images/characterSprites/walkDown1.png').get_width()
        self.height = pygame.image.load('assets/images/characterSprites/walkDown1.png').get_height()
        self.standingSprite = pygame.image.load('assets/images/characterSprites/walkDown1.png')
        self.walkRightSprites = [pygame.image.load('assets/images/characterSprites/walkRight' + str(i) + '.png') for i in range(3)]
        self.walkLeftSprites = [pygame.image.load('assets/images/characterSprites/walkLeft' + str(i) + '.png') for i in range(3)]
        self.walkUpSprites = [pygame.image.load('assets/images/characterSprites/walkUp' + str(i) + '.png') for i in range(3)]
        self.walkDownSprites = [pygame.image.load('assets/images/characterSprites/walkDown' + str(i) + '.png') for i in range(3)]
        self.walkCount = 0
        self.sprite = self.standingSprite
        self.speed = 4
        self.direction = "standing"
        self.nameOutput = pygame.font.SysFont('Callibri', 20).render("", 1, (0, 0, 0))
    
    # Method which moves the player based on their keypresses in the 'main.py' module
    def move(self):
        if self.walkCount == 25:
            self.walkCount = 0 # Resets the walkCount to 0 if it exceeds 50
        if self.direction == "right":
            self.sprite = self.walkRightSprites[self.walkCount // 12]
            self.x += self.speed
            self.walkCount += 1
        if self.direction == "left":
            self.sprite = self.walkLeftSprites[self.walkCount // 12]
            self.x -= self.speed
            self.walkCount += 1
        if self.direction == "up":
            self.sprite = self.walkUpSprites[self.walkCount // 12]
            self.y -= self.speed
            self.walkCount += 1
        if self.direction == "down":
            self.sprite = self.walkDownSprites[self.walkCount // 12]
            self.y += self.speed
            self.walkCount += 1
        if self.direction == "standing":
            self.sprite = self.standingSprite
    
    # Method which detects if the character/player is colliding with the borders of the screen or the house
    def collision(self, direction):
        # [255, 235] [535, 235] [255, 400] [535, 400]
        if self.x <= 535 and self.x + self.width >= 255 and self.y - 4 <= 400 and self.y - 4 + self.height >= 235 and direction == "up":
            return True
        elif self.x <= 535 and self.x + self.width >= 255 and self.y + 4 <= 400 and self.y + 4 + self.height >= 235 and direction == "down":
            return True
        elif self.x - 4 <= 535 and self.x - 4 + self.width >= 255 and self.y <= 400 and self.y + self.height >= 235 and direction == "left":
            return True
        elif self.x + 4 <= 535 and self.x + 4 + self.width >= 255 and self.y <= 400 and self.y + self.height >= 235 and direction == "right":
            return True
        else:
            if self.y - 4 <= 36 and direction == "up":
                return True
            elif self.y + 4 + self.height >= 464 and direction == "down":
                return True
            elif self.x - 4 <= 36 and direction == "left":
                return True
            elif self.x + 4 + self.height >= 664 and direction == "right":
                return True
            else:
                return False
    
    # Method which detects if the character/player is within the boundaries of the achievements house's door
    def atHouse(self):
        if 395 <= self.y <= 402 and 265 <= self.x <= 402:
            return True
        else:
            return False
    
    # Method which detects if the character/player is colliding with the math/blue portal
    def mathPortalCollision(self):
        if self.x <= 235 + 30 and self.x + self.width >= 235 and self.y <= 55 + 50 and self.y + self.height >= 55:
            return True
    
    # Method which detects if the character/player is colliding with the math/blue portal
    def englishPortalCollision(self):
        if self.x <= 434 + 30 and self.x + self.width >= 434 and self.y <= 55 + 50 and self.y + self.height >= 55:
            return True
    
    # Method which drwas the character/player on-screen
    def output(self, window, name):
        self.outputName = self.nameOutput = pygame.font.SysFont('Callibri', 25).render(name, 1, (0, 0, 0))
        window.blit(self.outputName, (self.x - self.outputName.get_width() / 2 + 22, self.y - 15))
        window.blit(self.sprite, (self.x, self.y))
