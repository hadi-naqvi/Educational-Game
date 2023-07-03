# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - EnglishGame.py

# Module imports needed for the class
import pygame
from Button import *
from Textbox import *
pygame.init()

# Class for the english level of the game
class EnglishGame(object):
    # Initialization/Constructor method
    def __init__(self):
        self.spellingButton = Button(pygame.image.load('assets/images/buttons/spellingButton.png'), pygame.image.load('assets/images/buttons/spellingButton2.png'))
        self.punctuationButton = Button(pygame.image.load('assets/images/buttons/punctuationButton.png'), pygame.image.load('assets/images/buttons/punctuationButton2.png'))
        self.confirmButton = Button(pygame.image.load('assets/images/buttons/confirmButton.png'), pygame.image.load('assets/images/buttons/confirmButton2.png'))
        self.retryButton = Button(pygame.image.load('assets/images/buttons/retryButton.png'), pygame.image.load('assets/images/buttons/retryButton2.png'))
        self.continueButton = Button(pygame.image.load('assets/images/buttons/continueButton.png'), pygame.image.load('assets/images/buttons/continueButton2.png'))
        self.backButton = Button(pygame.image.load('assets/images/buttons/backButton.png'), pygame.image.load('assets/images/buttons/backButton2.png'))
        self.spellingScore = 0
        self.punctuationScore = 0
        self.question = 1
        self.score = 0
        self.game = ""
        self.retry = False
        self.answer = ""
        self.spellingQuestionOneAnswer = "i like to play with snow"
        self.spellingQuestionTwoAnswer = "the north pole is cold"
        self.spellingQuestionThreeAnswer = "my christmas lights are bright"
        self.punctuationQuestionOneAnswer = "hello santa, how are you?"
        self.punctuationQuestionTwoAnswer = "i have snow, ice and presents."
        self.punctuationQuestionThreeAnswer = "i am rudolph. who are you?"
        self.font = pygame.font.SysFont('Callirbi', 40)
        self.englishMenuScreenBackground = pygame.image.load('assets/images/backgrounds/englishMenuScreenBackground.png')
        self.englishGameScreenBackground = pygame.image.load('assets/images/backgrounds/englishGameScreenBackground.png')
        self.answerInput = Textbox(50, 325, 400, 35, "Enter your answer here:")
    
    # Method which drwas the menu screen
    def menuOutput(self, window, mousePos):
        window.blit(self.englishMenuScreenBackground, (0, 0))
        self.spellingButton.output(window, mousePos, 50, 200)
        window.blit(self.font.render("{} / 3".format(self.spellingScore), 1, (0, 0, 0)), (250, 213))
        self.punctuationButton.output(window, mousePos, 50, 250)
        window.blit(self.font.render("{} / 3".format(self.punctuationScore), 1, (0, 0, 0)), (325, 260))
        self.backButton.output(window, mousePos, 0, 450)
    
    # Method which draws the game screen
    def gameOutput(self, window, mousePos):
        window.blit(self.englishGameScreenBackground, (0, 0))
        window.blit(self.font.render("Question: {} / 3".format(self.question), 1, (255, 0, 0)), (500, 50))
        window.blit(self.font.render("Score: {} / 3".format(self.score), 1, (255, 0, 0)), (500, 80))
        if self.game == "spelling":
            if self.question == 1:
                window.blit(self.font.render("Correct the sentence below:", 1, (0, 0, 0)), (100, 50))
                window.blit(self.font.render("I liek to play with snoe", 1, (0, 0, 0)), (100, 100))
                self.answerInput.output(window, mousePos)
            elif self.question == 2:
                window.blit(self.font.render("Correct the sentence below:", 1, (0, 0, 0)), (100, 50))
                window.blit(self.font.render("The nowrth powle is cowld", 1, (0, 0, 0)), (100, 100))
                self.answerInput.output(window, mousePos)
            elif self.question == 3:
                window.blit(self.font.render("Correct the sentence below:", 1, (0, 0, 0)), (100, 50))
                window.blit(self.font.render("My Chrismus lites are bright", 1, (0, 0, 0)), (100, 100))
                self.answerInput.output(window, mousePos)
            self.answerInput.output(window, mousePos)
            if self.retry == False:
                self.confirmButton.output(window, mousePos, 300, 450)
            self.backButton.output(window, mousePos, 0, 450)
        elif self.game == "punctuation":
            if self.question == 1:
                window.blit(self.font.render("Correct the sentence below:", 1, (0, 0, 0)), (100, 50))
                window.blit(self.font.render("hello santa? how are you.", 1, (0, 0, 0)), (100, 100))
                self.answerInput.output(window, mousePos)
            elif self.question == 2:
                window.blit(self.font.render("Correct the sentence below:", 1, (0, 0, 0)), (100, 50))
                window.blit(self.font.render("i have snow ice and presents?", 1, (0, 0, 0)), (100, 100))
                self.answerInput.output(window, mousePos)
            elif self.question == 3:
                window.blit(self.font.render("Correct the sentence below:", 1, (0, 0, 0)), (100, 50))
                window.blit(self.font.render("i am rudolph? who are you?", 1, (0, 0, 0)), (100, 100))
                self.answerInput.output(window, mousePos)
            self.answerInput.output(window, mousePos)
            if self.retry == False:
                self.confirmButton.output(window, mousePos, 300, 450)
            self.backButton.output(window, mousePos, 0, 450)
        if self.retry == True:
                self.retryButton.output(window, mousePos, 500, 300)
                self.continueButton.output(window, mousePos, 500, 350)
