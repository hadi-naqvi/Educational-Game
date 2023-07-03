# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - MathGame.py

# Module imports needed for class
import pygame, random
from Button import *
from Textbox import *
pygame.init()

# Class for the math level of the game
class MathGame(object):
    # Initialization/Constructor method
    def __init__(self):
        self.additionButton = Button(pygame.image.load('assets/images/buttons/additionButton.png'), pygame.image.load('assets/images/buttons/additionButton2.png'))
        self.subtractionButton = Button(pygame.image.load('assets/images/buttons/subtractionButton.png'), pygame.image.load('assets/images/buttons/subtractionButton2.png'))
        self.confirmButton = Button(pygame.image.load('assets/images/buttons/confirmButton.png'), pygame.image.load('assets/images/buttons/confirmButton2.png'))
        self.retryButton = Button(pygame.image.load('assets/images/buttons/retryButton.png'), pygame.image.load('assets/images/buttons/retryButton2.png'))
        self.continueButton = Button(pygame.image.load('assets/images/buttons/continueButton.png'), pygame.image.load('assets/images/buttons/continueButton2.png'))
        self.backButton = Button(pygame.image.load('assets/images/buttons/backButton.png'), pygame.image.load('assets/images/buttons/backButton2.png'))
        self.additionScore = 0
        self.subtractionScore = 0
        self.question = 0
        self.score = 0
        self.game = ""
        self.retry = False
        self.firstNumber = 0
        self.secondNumber = 0
        self.answer = 0
        self.font = pygame.font.SysFont('Callirbi', 40)
        self.mathMenuScreenBackground = pygame.image.load('assets/images/backgrounds/englishMenuScreenBackground.png')
        self.mathGameScreenBackground = pygame.image.load('assets/images/backgrounds/englishGameScreenBackground.png')
        self.answerInput = Textbox(50, 325, 400, 35, "Enter your answer here:")
    
    # Method which randomly generates numbers and a math question
    def randomizeNumbers(self):
        self.firstNumber = random.randint(9, 20)
        self.secondNumber = random.randint(1, 9)
        if self.game == "addition":
            self.answer = str(self.firstNumber + self.secondNumber)
        elif self.game == "subtraction":
            self.answer = str(self.firstNumber - self.secondNumber)
    
    # Method which drwas the menu screen
    def menuOutput(self, window, mousePos):
        window.blit(self.mathMenuScreenBackground, (0, 0))
        self.additionButton.output(window, mousePos, 50, 200)
        window.blit(self.font.render("{} / 3".format(self.additionScore), 1, (0, 0, 0)), (250, 213))
        self.subtractionButton.output(window, mousePos, 50, 250)
        window.blit(self.font.render("{} / 3".format(self.subtractionScore), 1, (0, 0, 0)), (320, 260))
        self.backButton.output(window, mousePos, 0, 450)
    
    # Method which draws the game screen
    def gameOutput(self, window, mousePos):
        window.blit(self.mathGameScreenBackground, (0, 0))
        window.blit(self.font.render("Question: {} / 3".format(self.question), 1, (255, 0, 0)), (500, 50))
        window.blit(self.font.render("Score: {} / 3".format(self.score), 1, (255, 0, 0)), (500, 80))
        if self.game == "addition":
            window.blit(self.font.render("Answer the equation below:", 1, (0, 0, 0)), (100, 50))
            window.blit(self.font.render(str(self.firstNumber) + " + " + str(self.secondNumber), 1, (0, 0, 0)), (100, 100))
            self.answerInput.output(window, mousePos)
            if self.retry == False:
                self.confirmButton.output(window, mousePos, 300, 450)
            self.backButton.output(window, mousePos, 0, 450)
        elif self.game == "subtraction":
            window.blit(self.font.render("Answer the equation below:", 1, (0, 0, 0)), (100, 50))
            window.blit(self.font.render(str(self.firstNumber) + " - " + str(self.secondNumber), 1, (0, 0, 0)), (100, 100))
            self.answerInput.output(window, mousePos)
        if self.retry == False:
            self.confirmButton.output(window, mousePos, 300, 450)
        if self.retry == True:
                self.retryButton.output(window, mousePos, 500, 300)
                self.continueButton.output(window, mousePos, 500, 350)
        self.backButton.output(window, mousePos, 0, 450)
