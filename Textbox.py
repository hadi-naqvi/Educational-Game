# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - textbox.py

# Module impots needed for the class
import pygame
pygame.init()

# Class for textbox objects
class Textbox(object):
    # Initialization/Constructor method
    def __init__(self, x, y, width, height, prompt):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.prompt = prompt
        self.promptText = pygame.font.SysFont('Callibri', 25).render(self.prompt, 1, (0, 0, 0))
        self.state = "inactive"
        self.textInBox = []
    
    # Method which detects if the user is hovering over the textbox
    def mouseHover(self, mousePos):
        if self.x <= mousePos[0] <= self.x + self.width and self.y <= mousePos[1] <= self.y + self.height:
            return True
        else:
            return False
    
    # Method which draws the textbox on-screen
    def output(self, window, mousePos):
        window.blit(self.promptText, (self.x, self.y - 20))
        pygame.draw.rect(window, (0, 0, 0), (self.x - 2, self.y - 2, self.width + 3, self.height + 3), 2)
        if self.state == "active":
            pygame.draw.rect(window, (255, 255, 255), (self.x, self.y, self.width, self.height))
            window.blit(pygame.font.SysFont('Callibri', 35).render("".join(self.textInBox) + "|", 1, (0, 0, 0)), (self.x, self.y + 5))
        elif self.mouseHover(mousePos):
            pygame.draw.rect(window, (225, 225, 225), (self.x, self.y, self.width, self.height))
            window.blit(pygame.font.SysFont('Callibri', 35).render("".join(self.textInBox) + '|', 1, (0, 0, 0)), (self.x, self.y + 5))            
        else:
            pygame.draw.rect(window, (200, 200, 200), (self.x, self.y, self.width, self.height))
            window.blit(pygame.font.SysFont('Callibri', 35).render("".join(self.textInBox), 1, (0, 0, 0)), (self.x, self.y + 5))
