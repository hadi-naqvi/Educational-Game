# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - main.py

# Module imports needed for game
import pygame, sys, string
from Button import *
from AudioButton import *
from Textbox import *
from Character import *
from Achievement import *
from MathGame import *
from EnglishGame import *
pygame.init() # Initializes pygame

# Class for game
class Game(object):
    # Initialization/Constructor method
    def __init__(self):
        # Window/display setup
        self.windowWidth = 700
        self.windowHeight = 500
        self.window = pygame.display.set_mode((self.windowWidth, self.windowHeight))
        pygame.display.set_caption("Santa's Christmas Challenges")
        pygame.display.set_icon(pygame.image.load('assets/images/gameIcon.png'))
        self.output = "homeScreen" # Variable which stores which screen the game is on
        
        # Background music setup
        pygame.mixer.music.load('assets/sounds/music.mp3')
        pygame.mixer.music.play(-1)        
        
        # Important game variables/attributes
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.running = True
        self.previousScreen = ""
        self.name = "" # User's name
        
        # Variables which contain sets of characters for later when filtering text input in textboxes
        self.keyPressed = pygame.key.get_pressed()
        self.chars = string.ascii_letters + ' 1234567890_'
        self.alphabet = string.ascii_letters + " "
        self.punctuation = string.ascii_letters + " ,.?"
        self.numbers = "1234567890"        
        
        # Objects and Vairables for achievements
        self.achievementUnlock = False
        self.achievementSoundEffect = pygame.mixer.Sound('assets/sounds/achievement.wav')
        self.additionAchievement = Achievement(100, 150, "Addition Master")
        self.subtractionAchievement = Achievement(300, 150, "Subtraction Sensei")
        self.spellingAchievement = Achievement(100, 300, "Super Spelling")
        self.punctuationAchievement = Achievement(300, 300, "Perfect Punctuation")
        
        # Objects/Instances of other classes needed for game
        self.player = Character()
        self.mathGame = MathGame()
        self.englishGame = EnglishGame()

        # Textbox and Buttons
        self.namePrompt = Textbox(250, 210, 200, 35, "Enter your name here:") # Textbox which prompt's user for his/her namme
        self.startButton = Button(pygame.image.load('assets/images/buttons/startButton.png'), pygame.image.load('assets/images/buttons/startButton2.png'))
        self.tutorialButton = Button(pygame.image.load('assets/images/buttons/tutorialButton.png'), pygame.image.load('assets/images/buttons/tutorialButton2.png'))
        self.quitButton = Button(pygame.image.load('assets/images/buttons/quitButton.png'), pygame.image.load('assets/images/buttons/quitButton2.png'))
        self.resumeButton = Button(pygame.image.load('assets/images/buttons/resumeButton.png'), pygame.image.load('assets/images/buttons/resumeButton2.png'))
        self.backButton = Button(pygame.image.load('assets/images/buttons/backButton.png'), pygame.image.load('assets/images/buttons/backButton2.png'))
        self.audioButton = AudioButton(600, 400, pygame.image.load('assets/images/buttons/unmutedSprite.png'), pygame.image.load('assets/images/buttons/unmutedHoverSprite.png'), pygame.image.load('assets/images/buttons/mutedSprite.png'), pygame.image.load('assets/images/buttons/mutedHoverSprite.png'))
        self.buttons = [self.startButton, self.tutorialButton, self.quitButton] # List with every homeScreen button for easier iteration later on
               
        # Graphics/Images and audio imports
        self.homeScreenBackgrounds = [pygame.image.load('assets/images/backgrounds/homeScreenBackground' + str(i) + '.png') for i in range(6)]
        self.homeScreenBackgroundCount = 0 # Animation counter
        self.bluePortalSprites = [pygame.image.load('assets/images/portalSprites/portal' + str(i) + 'a.png') for i in range(4)]
        self.orangePortalSprites = [pygame.image.load('assets/images/portalSprites/portal' + str(i) + 'b.png') for i in range(4)]
        self.portalAnimationCount = 0 # Animation counter
        self.tutorialScreenBackground = pygame.image.load('assets/images/backgrounds/tutorialScreenBackground.png')
        self.lobbyScreenBackground = pygame.image.load('assets/images/backgrounds/lobbyScreenBackground.png')
        self.pauseScreenBackground = pygame.image.load('assets/images/backgrounds/pauseScreenBackground.png')
        self.achievementsScreenBackground = pygame.image.load('assets/images/backgrounds/achievementsScreenBackground.png')          
        self.doorEnterPrompt = pygame.font.SysFont('Callibri', 50).render("Press [SPACE] to view achievements", 1, (255, 0, 0)) # Text which prompts user to press SPACE to enter achievements house
        self.portalSound = pygame.mixer.Sound('assets/sounds/portalSound.wav')
        self.rewardAnimation = pygame.image.load('assets/images/rewardAnimation.png')
        self.rewardAnimationX = 800 # X position of santa sleigh for user reward animation
    
    # Method which toggles the in-game audio on/off
    def audioToggle(self):
        if self.audioButton.sprite == self.audioButton.unmutedSprite:
            self.audioButton.sprite = self.audioButton.mutedSprite
            pygame.mixer.pause()
            pygame.mixer.music.pause()
        else:
            self.audioButton.sprite = self.audioButton.unmutedSprite
            pygame.mixer.unpause()
            pygame.mixer.music.unpause()
    
    # Method which processes user input 
    def detectUserInput(self):
        for event in pygame.event.get():
            # If user clicks X button, the game closes
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                self.running = False
            
            
            # If the user presses ESC and they are not in the homescreen or pausescreen, they are sent to the pausescreen
            if self.output != "pauseScreen" and self.output != "homeScreen" and event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.englishGame.answerInput.state = "inactive"
                self.previousScreen = self.output # Saves previous screen so game can resume after user leaves pausescreen
                self.output = "pauseScreen"
            
            
            # User input for the homescreen
            if self.output == "homeScreen":
                # Allows user to click the textbox and start typing
                if event.type == pygame.MOUSEBUTTONDOWN and self.namePrompt.mouseHover(pygame.mouse.get_pos()):
                    self.namePrompt.state = "active"
                elif event.type == pygame.MOUSEBUTTONDOWN and self.namePrompt.mouseHover(pygame.mouse.get_pos()) == False:
                    self.namePrompt.state = "inactive"
                if self.namePrompt.state == "active" and event.type == pygame.KEYDOWN:
                    # If backspace is pressed, the last character is removed
                    if event.key == 8:
                        self.namePrompt.textInBox = self.namePrompt.textInBox[:-1]
                    elif event.key == 13 or event.key == 27:
                        self.namePrompt.state = "inactive"
                    elif pygame.font.SysFont('Callibri', 25).render("".join(self.namePrompt.textInBox), 1, (0, 0, 0)).get_width() < 120:
                        # Filters the user input so only letters and numbers can be entered
                        for char in self.chars:
                            if event.unicode == char:
                                self.namePrompt.textInBox.append(event.unicode)
                
                # If user presses start button, they are sent to the lobbyscreen (on the condition that they have entered a name)
                if event.type == pygame.MOUSEBUTTONDOWN and self.startButton.mouseHover(pygame.mouse.get_pos(), 250, 275) and len(self.namePrompt.textInBox) >= 1:
                    self.name = "".join(self.namePrompt.textInBox)
                    self.namePrompt.state = "inactive"
                    self.output = "lobbyScreen"
                    self.player.x = 325
                    self.player.y = 410                    
                
                # If user clicks tutorial button, they are sent to the tutorial screen
                if event.type == pygame.MOUSEBUTTONDOWN and self.tutorialButton.mouseHover(pygame.mouse.get_pos(), 250, 325):
                    self.output = "tutorialScreen"
                
                # If user clicks the quit button, the game closes
                if event.type == pygame.MOUSEBUTTONDOWN and self.quitButton.mouseHover(pygame.mouse.get_pos(), 250, 375):
                    pygame.quit()
                    sys.exit()
                    self.running = False
                
                # If user clicks the audio button, they toggle the audio mute
                if event.type == pygame.MOUSEBUTTONDOWN and self.audioButton.mouseHover(pygame.mouse.get_pos()):
                    self.audioToggle()
            
            
            # User input for the tutorialscreen
            if self.output == "tutorialScreen":
                # If user presses back button, they are sent back to the homescreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.backButton.mouseHover(pygame.mouse.get_pos(), 500, 450):
                    self.output = "homeScreen"
            
            
            # User input for the pausescreen
            if self.output == "pauseScreen":
                # Allows user to click the textbox and start typing
                if event.type == pygame.MOUSEBUTTONDOWN and self.namePrompt.mouseHover(pygame.mouse.get_pos()):
                    self.namePrompt.state = "active"
                elif event.type == pygame.MOUSEBUTTONDOWN and self.namePrompt.mouseHover(pygame.mouse.get_pos()) == False:
                    self.namePrompt.state = "inactive"
                if self.namePrompt.state == "active" and event.type == pygame.KEYDOWN:
                    # If backspace is pressed, the last character is removed
                    if event.key == pygame.K_BACKSPACE:
                        self.namePrompt.textInBox = self.namePrompt.textInBox[:-1]
                    elif event.key == 27 or event.key == 13:
                        self.namePrompt.state = "inactive"
                    elif pygame.font.SysFont('Callibri', 25).render("".join(self.namePrompt.textInBox), 1, (0, 0, 0)).get_width() < 100:
                        # Filters the user input so only letters and numbers can be entered
                        for char in self.chars:
                            if event.unicode == char:
                                self.namePrompt.textInBox.append(event.unicode)
                
                # If user presses resume button, they are sent back to the previous screen they were on
                if event.type == pygame.MOUSEBUTTONDOWN and self.resumeButton.mouseHover(pygame.mouse.get_pos(), 250, 275) and len(self.namePrompt.textInBox) >= 1:
                    self.name = "".join(self.namePrompt.textInBox)
                    self.output = self.previousScreen
                    self.previousScreen = ""
                    self.namePrompt.state = "inactive"
                    self.player.x = 325
                    self.player.y = 410 
                
                # If user presses quit button, they are sent back to the homescreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.quitButton.mouseHover(pygame.mouse.get_pos(), 250, 325):
                    self.name = "".join(self.namePrompt.textInBox)
                    self.namePrompt.state = "inactive"
                    self.previousScreen = ""
                    self.output = "homeScreen"
                
                # If user clicks the audio button, they toggle the audio mute
                if event.type == pygame.MOUSEBUTTONDOWN and self.audioButton.mouseHover(pygame.mouse.get_pos()):
                    print("Mute button has been pressed")
                    self.audioToggle()
            
            
            # User input for lobbyscreen
            if self.output == "lobbyScreen":
                # If user is at the door of the house and they press SPACE they are sent to the achievementsscreen
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.player.atHouse():
                    self.output = "achievementsScreen"
            
            
            # User input for achievementsscreen
            if self.output == "achievementsScreen":
                # If user presses back button, they are sent back to the lobbyscreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.resumeButton.mouseHover(pygame.mouse.get_pos(), 0, 450):
                    self.output = "lobbyScreen"
                    self.player.x = 325
                    self.player.y = 410                     
            
            
            # User input for the mathmenuscreen
            if self.output == "mathMenuScreen":
                # If user presses back button, they are sent back to the lobbyscreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.backButton.mouseHover(pygame.mouse.get_pos(), 0, 450):
                    self.achievementUnlock = False
                    self.output = "lobbyScreen"
                    self.player.x = 325
                    self.player.y = 410
                
                # If user presses addition button, they are sent to the addition game/mathgamescreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.additionButton.mouseHover(pygame.mouse.get_pos(), 50, 200):
                    self.mathGame.game = "addition"
                    self.mathGame.answerInput.textInBox.clear()
                    self.mathGame.randomizeNumbers()
                    self.mathGame.score = 0
                    self.mathGame.question = 1
                    self.mathGame.retry = False
                    self.output = "mathGameScreen"
                
                # If user presses subtraction button, they are sent to the addition game/mathgamescreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.subtractionButton.mouseHover(pygame.mouse.get_pos(), 50, 250):
                    self.mathGame.game = "subtraction"
                    self.mathGame.answerInput.textInBox.clear()
                    self.mathGame.randomizeNumbers()
                    self.mathGame.score = 0
                    self.mathGame.question = 1
                    self.mathGame.retry = False
                    self.output = "mathGameScreen"



            # User input for mathgamescreen
            if self.output == "mathGameScreen":
                # Allows user to click the textbox and begin typing
                if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.answerInput.mouseHover(pygame.mouse.get_pos()):
                    self.mathGame.answerInput.state = "active"
                elif event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.answerInput.mouseHover(pygame.mouse.get_pos()) == False:
                    self.mathGame.answerInput.state = "inactive"
                if self.mathGame.answerInput.state == "active" and event.type == pygame.KEYDOWN:
                    # Pressing backspace removes the last character from the textbox
                    if event.key == 8:
                        self.mathGame.answerInput.textInBox = self.mathGame.answerInput.textInBox[:-1]
                    elif event.key == 13 or event.key == 27:
                        self.mathGame.answerInput.state = "inactive"
                    elif pygame.font.SysFont('Callibri', 25).render("".join(self.mathGame.answerInput.textInBox), 1, (0, 0, 0)).get_width() < 250:
                        # Filters user text input and only allows numbers to be typed
                        for number in self.numbers:
                            if event.unicode == number:
                                self.mathGame.answerInput.textInBox.append(event.unicode)
                
                # If back button is pressed, user is sent back to the mathmenuscreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.backButton.mouseHover(pygame.mouse.get_pos(), 0, 450):
                    self.output = "mathMenuScreen"
                    if self.mathGame.game == "addition":
                        if self.mathGame.score >= self.mathGame.additionScore:
                            self.mathGame.additionScore = self.mathGame.score
                    elif self.mathGame.game == "subtraction":
                        if self.mathGame.score >= self.mathGame.subtractionScore:
                            self.mathGame.subtractionScore = self.mathGame.score
                    # Checks if the user has unlocked an achievement
                    if self.additionAchievement.sprite == self.additionAchievement.lockedSprite and self.mathGame.additionScore == 3:
                        self.additionAchievement.sprite = self.additionAchievement.unlockedSprite
                        self.achievementUnlock = True
                        self.achievementSoundEffect.play()
                    elif self.subtractionAchievement.sprite == self.subtractionAchievement.lockedSprite and self.mathGame.subtractionScore == 3:
                        self.subtractionAchievement.sprite = self.subtractionAchievement.unlockedSprite
                        self.achievementUnlock = True
                        self.achievementSoundEffect.play()                        
                
                # If the user presses the confirm button, the appropriate game response occurs depending on whether the user's answer was correct or incorrect
                if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.confirmButton.mouseHover(pygame.mouse.get_pos(), 300, 450) and self.mathGame.retry == False:
                    if "".join(self.mathGame.answerInput.textInBox) == self.mathGame.answer:
                        self.rewardAnimationX = -500
                        self.mathGame.answerInput.textInBox.clear() # Clears textbox for next question
                        self.mathGame.score += 1
                        if self.mathGame.question == 3:
                            self.output = "mathMenuScreen"
                            if self.mathGame.game == "addition":
                                if self.mathGame.score >= self.mathGame.additionScore:
                                    self.mathGame.additionScore = self.mathGame.score
                            elif self.mathGame.game == "subtraction":
                                if self.mathGame.score >= self.mathGame.subtractionScore:
                                    self.mathGame.subtractionScore = self.mathGame.score
                            if self.additionAchievement.sprite == self.additionAchievement.lockedSprite and self.mathGame.additionScore == 3:
                                self.additionAchievement.sprite = self.additionAchievement.unlockedSprite
                                self.achievementUnlock = True
                                self.achievementSoundEffect.play()
                            elif self.subtractionAchievement.sprite == self.subtractionAchievement.lockedSprite and self.mathGame.subtractionScore == 3:
                                self.subtractionAchievement.sprite = self.subtractionAchievement.unlockedSprite
                                self.achievementUnlock = True
                                self.achievementSoundEffect.play()                                        
                        else:
                            self.mathGame.answerInput.textInBox.clear()
                            self.mathGame.randomizeNumbers()
                            self.mathGame.question += 1
                    else:
                        self.mathGame.retry = True
                
                # If the user answers incorrectly, they are able to retry the question or continue onto the next question
                if self.mathGame.retry:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.retryButton.mouseHover(pygame.mouse.get_pos(), 500, 300):
                        self.mathGame.answerInput.textInBox.clear()
                        self.mathGame.retry = False
                    if event.type == pygame.MOUSEBUTTONDOWN and self.mathGame.continueButton.mouseHover(pygame.mouse.get_pos(), 500, 350):
                        self.mathGame.answerInput.textInBox.clear()
                        self.mathGame.retry = False
                        self.mathGame.randomizeNumbers()
                        if self.mathGame.question == 3:
                            self.output = "mathMenuScreen"
                            if self.mathGame.game == "addition":
                                if self.mathGame.score >= self.mathGame.additionScore:
                                    self.mathGame.additionScore = self.mathGame.score
                            elif self.mathGame.game == "subtraction":
                                if self.mathGame.score >= self.mathGame.subtractionScore:
                                    self.mathGame.subtractionScore = self.mathGame.score
                            if self.additionAchievement.sprite == self.additionAchievement.lockedSprite and self.mathGame.additionScore == 3:
                                self.additionAchievement.sprite = self.additionAchievement.unlockedSprite
                                self.achievementUnlock = True
                                self.achievementSoundEffect.play()
                            elif self.subtractionAchievement.sprite == self.subtractionAchievement.lockedSprite and self.mathGame.subtractionScore == 3:
                                self.subtractionAchievement.sprite = self.subtractionAchievement.unlockedSprite
                                self.achievementUnlock = True
                                self.achievementSoundEffect.play()                                        
                        self.mathGame.question += 1
            
            
            # User input for the englishmenuscreen
            if self.output == "englishMenuScreen":
                # If user presses back button, they are sent back to the lobbyscreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.backButton.mouseHover(pygame.mouse.get_pos(), 0, 450):
                    self.achievementUnlock = False
                    self.output = "lobbyScreen"
                    self.player.x = 325
                    self.player.y = 410
                
                # If user presses spelling button, they are sent to the spelling game/englishgamescreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.spellingButton.mouseHover(pygame.mouse.get_pos(), 50, 200):
                    self.englishGame.answerInput.textInBox.clear()
                    self.englishGame.answer = self.englishGame.spellingQuestionOneAnswer
                    self.englishGame.score = 0
                    self.englishGame.question = 1
                    self.englishGame.retry = False
                    self.englishGame.game = "spelling"
                    self.output = "englishGameScreen"
                
                # If user presses punctuation button, they are sent to the punctuation game/englishgamescreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.punctuationButton.mouseHover(pygame.mouse.get_pos(), 50, 250):
                    self.englishGame.answerInput.textInBox.clear()
                    self.englishGame.answer = self.englishGame.punctuationQuestionOneAnswer
                    self.englishGame.score = 0
                    self.englishGame.question = 1
                    self.englishGame.retry = False
                    self.englishGame.game = "punctuation"
                    self.output = "englishGameScreen"



            # User input for the englishgamescreen
            if self.output == "englishGameScreen":
                # Allows the user to click the textbox and begin typing
                if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.answerInput.mouseHover(pygame.mouse.get_pos()):
                    self.englishGame.answerInput.state = "active"
                elif event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.answerInput.mouseHover(pygame.mouse.get_pos()) == False:
                    self.englishGame.answerInput.state = "inactive"
                if self.englishGame.answerInput.state == "active" and event.type == pygame.KEYDOWN:
                    # If the user presses backspace, the last character in the textbox is deleted
                    if event.key == 8:
                        self.englishGame.answerInput.textInBox = self.englishGame.answerInput.textInBox[:-1]
                    elif event.key == 13 or event.key == 27:
                        self.englishGame.answerInput.state = "inactive"
                    elif pygame.font.SysFont('Callibri', 25).render("".join(self.englishGame.answerInput.textInBox), 1, (0, 0, 0)).get_width() < 250:
                        if self.englishGame.game == "spelling":
                            # Filters the user's textbox input and only allows letters to be typed
                            for letter in self.alphabet:
                                if event.unicode == letter:
                                    self.englishGame.answerInput.textInBox.append(event.unicode)
                        elif self.englishGame.game == "punctuation":
                            # Filters the user's tetxbox input and only allows letters and punctuation to be typed
                            for char in self.punctuation:
                                if event.unicode == char:
                                    self.englishGame.answerInput.textInBox.append(event.unicode)
                
                # If the user presses the back button, they are sent back to the englishmenuscreen
                if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.backButton.mouseHover(pygame.mouse.get_pos(), 0, 450):
                    self.output = "englishMenuScreen"
                    if self.englishGame.game == "spelling":
                        if self.englishGame.score >= self.englishGame.spellingScore:
                            self.englishGame.spellingScore = self.englishGame.score
                    elif self.englishGame.game == "punctuation":
                        if self.englishGame.score >= self.englishGame.punctuationScore:
                            self.englishGame.punctuationScore = self.englishGame.score
                        self.englishGame.punctuationScore = self.englishGame.score
                    if self.spellingAchievement.sprite == self.spellingAchievement.lockedSprite and self.englishGame.spellingScore == 3:
                        self.spellingAchievement.sprite = self.spellingAchievement.unlockedSprite
                        self.achievementUnlock = True
                        self.achievementSoundEffect.play()
                    elif self.punctuationAchievement.sprite == self.punctuationAchievement.lockedSprite and self.englishGame.punctuationScore == 3:
                        self.punctuationAchievement.sprite = self.punctuationAchievement.unlockedSprite
                        self.achievementUnlock = True
                        self.achievementSoundEffect.play()                            
                
                # If the user presses the confirm button, the appropriate game response occurs depending on whether they answer correctly or incorrectly
                if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.confirmButton.mouseHover(pygame.mouse.get_pos(), 300, 450) and self.englishGame.retry == False:
                    if "".join(self.englishGame.answerInput.textInBox).lower() == self.englishGame.answer:
                        self.rewardAnimationX = -500
                        self.englishGame.answerInput.textInBox.clear()
                        self.englishGame.score += 1
                        if self.englishGame.question == 3:
                            self.output = "englishMenuScreen"
                            if self.englishGame.game == "spelling":
                                if self.englishGame.score >= self.englishGame.spellingScore:
                                    self.englishGame.spellingScore = self.englishGame.score
                            elif self.englishGame.game == "punctuation":
                                if self.englishGame.score >= self.englishGame.punctuationScore:
                                    self.englishGame.punctuationScore = self.englishGame.score
                            if self.spellingAchievement.sprite == self.spellingAchievement.lockedSprite and self.englishGame.spellingScore == 3:
                                self.spellingAchievement.sprite = self.spellingAchievement.unlockedSprite
                                self.achievementUnlock = True
                                self.achievementSoundEffect.play()
                            elif self.punctuationAchievement.sprite == self.punctuationAchievement.lockedSprite and self.englishGame.punctuationScore == 3:
                                self.punctuationAchievement.sprite = self.punctuationAchievement.unlockedSprite
                                self.achievementUnlock = True
                                self.achievementSoundEffect.play()                           
                        else:
                            self.englishGame.answerInput.textInBox.clear()
                            if self.englishGame.game == "spelling":
                                if self.englishGame.question == 1:
                                    self.englishGame.answer = self.englishGame.spellingQuestionTwoAnswer
                                elif self.englishGame.question == 2:
                                    self.englishGame.answer = self.englishGame.spellingQuestionThreeAnswer
                            elif self.englishGame.game == "punctuation":
                                if self.englishGame.question == 1:
                                    self.englishGame.answer = self.englishGame.punctuationQuestionTwoAnswer
                                elif self.englishGame.question == 2:
                                    self.englishGame.answer = self.englishGame.punctuationQuestionThreeAnswer
                            self.englishGame.question += 1
                    else:
                        self.englishGame.retry = True
                
                # If the user answers incorrectly, they are able to retry the question or continue to the next one
                if self.englishGame.retry:
                    if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.retryButton.mouseHover(pygame.mouse.get_pos(), 500, 300):
                        self.englishGame.answerInput.textInBox.clear()
                        self.englishGame.retry = False
                    if event.type == pygame.MOUSEBUTTONDOWN and self.englishGame.continueButton.mouseHover(pygame.mouse.get_pos(), 500, 350):
                        self.englishGame.answerInput.textInBox.clear()
                        self.englishGame.retry = False
                        if self.englishGame.game == "spelling":
                            if self.englishGame.question == 1:
                                self.englishGame.answer = self.englishGame.spellingQuestionTwoAnswer
                            elif self.englishGame.question == 2:
                                self.englishGame.answer = self.englishGame.spellingQuestionThreeAnswer
                            elif self.englishGame.question == 3:
                                self.output = "englishMenuScreen"
                                if self.englishGame.game == "spelling":
                                    if self.englishGame.score >= self.englishGame.spellingScore:
                                        self.englishGame.spellingScore = self.englishGame.score
                                elif self.englishGame.game == "punctuation":
                                    if self.englishGame.score >= self.englishGame.punctuationScore:
                                        self.englishGame.punctuationScore = self.englishGame.score
                                if self.spellingAchievement.sprite == self.spellingAchievement.lockedSprite and self.englishGame.spellingScore == 3:
                                    self.spellingAchievement.sprite = self.spellingAchievement.unlockedSprite
                                    self.achievementUnlock = True
                                    self.achievementSoundEffect.play()
                                elif self.punctuationAchievement.sprite == self.punctuationAchievement.lockedSprite and self.englishGame.punctuationScore == 3:
                                    self.punctuationAchievement.sprite = self.punctuationAchievement.unlockedSprite
                                    self.achievementUnlock = True
                                    self.achievementSoundEffect.play()                               
                            self.englishGame.question += 1                                
                        elif self.englishGame.game == "punctuation":
                            if self.englishGame.question == 1:
                                self.englishGame.answer = self.englishGame.punctuationQuestionTwoAnswer
                            elif self.englishGame.question == 2:
                                self.englishGame.answer = self.englishGame.punctuationQuestionTwoAnswer
                            elif self.englishGame.question == 3:
                                self.output = "englishMenuScreen"
                                if self.englishGame.game == "spelling":
                                    if self.englishGame.score >= self.englishGame.spellingScore:
                                        self.englishGame.spellingScore = self.englishGame.score
                                elif self.englishGame.game == "punctuation":
                                    if self.englishGame.score >= self.englishGame.punctuationScore:
                                        self.englishGame.punctuationScore = self.englishGame.score
                                if self.spellingAchievement.sprite == self.spellingAchievement.lockedSprite and self.englishGame.spellingScore == 3:
                                    self.spellingAchievement.sprite = self.spellingAchievement.unlockedSprite
                                    self.achievementUnlock = True
                                    self.achievementSoundEffect.play()
                                elif self.punctuationAchievement.sprite == self.punctuationAchievement.lockedSprite and self.englishGame.punctuationScore == 3:
                                    self.punctuationAchievement.sprite = self.punctuationAchievement.unlockedSprite
                                    self.achievementUnlock = True
                                    self.achievementSoundEffect.play()                                           
                            self.englishGame.question += 1


        # User input for character/player on-screen in the lobbyscreen
        if self.output == "lobbyScreen":
            # Stores the user's keypress in a variable
            self.keyPressed = pygame.key.get_pressed()
            
            # Depending on which direction key the user presses, they move as long as they are not colliding with the screen borders or house
            if self.keyPressed[pygame.K_RIGHT] and self.player.collision("right") == False:
                self.player.direction = "right"
                self.player.move()
            elif self.keyPressed[pygame.K_LEFT] and self.player.collision("left") == False:
                self.player.direction = "left"
                self.player.move()
            if self.keyPressed[pygame.K_UP] and self.player.collision("up") == False:
                self.player.direction = "up"
                self.player.move()
            elif self.keyPressed[pygame.K_DOWN] and self.player.collision("down") == False:
                self.player.direction = "down"
                self.player.move()
            if self.keyPressed[pygame.K_RIGHT] == False and self.keyPressed[pygame.K_LEFT] == False and self.keyPressed[pygame.K_UP] == False and self.keyPressed[pygame.K_DOWN] == False:
                self.player.direction = "standing"
                self.player.move()
            
            # If the user walks into the math portal, they are sent to the mathmenuscreen
            if self.player.mathPortalCollision():
                self.output = "mathMenuScreen"
                if self.audioButton.sprite == self.audioButton.unmutedHoverSprite or self.audioButton.sprite == self.audioButton.unmutedSprite:
                    self.portalSound.play()
            
            # If the user walks into the english portal, they are sent to the englishmenuscreen
            if self.player.englishPortalCollision():
                self.output = "englishMenuScreen"
                if self.audioButton.sprite == self.audioButton.unmutedHoverSprite or self.audioButton.sprite == self.audioButton.unmutedSprite:
                    self.portalSound.play()
        
    # Method which updates the display
    def updateWindow(self):
        # Draws the homescreen
        if self.output == "homeScreen":
            if self.homeScreenBackgroundCount == 51:
                self.homeScreenBackgroundCount = 0
            self.window.blit(self.homeScreenBackgrounds[self.homeScreenBackgroundCount // 17], (0, 0))
            self.homeScreenBackgroundCount += 1
            self.namePrompt.output(self.window, pygame.mouse.get_pos())
            self.startButton.output(self.window, pygame.mouse.get_pos(), 250, 275)
            self.tutorialButton.output(self.window, pygame.mouse.get_pos(), 250, 325)
            self.quitButton.output(self.window, pygame.mouse.get_pos(), 250, 375)
            self.audioButton.output(self.window, pygame.mouse.get_pos())
        
        # Draws the tutorialscreen
        elif self.output == "tutorialScreen":
            self.window.blit(self.tutorialScreenBackground, (0, 0))
            self.backButton.output(self.window, pygame.mouse.get_pos(), 500, 450)            
        
        # Drwas the lobbyscreen
        elif self.output == "lobbyScreen":
            self.window.blit(self.lobbyScreenBackground, (0, 0))
            if self.portalAnimationCount == 27:
                self.portalAnimationCount = 0
            self.window.blit(self.bluePortalSprites[self.portalAnimationCount // 9], (235, 55))
            self.window.blit(self.orangePortalSprites[self.portalAnimationCount // 9], (435, 55))
            self.portalAnimationCount += 1
            self.player.output(self.window, self.name)
            if self.player.atHouse():
                self.window.blit(self.doorEnterPrompt, (45, 25))
        
        # Draws the pausescreen
        elif self.output == "pauseScreen":
            self.window.blit(self.pauseScreenBackground, (0, 0))
            self.namePrompt.output(self.window, pygame.mouse.get_pos())
            self.resumeButton.output(self.window, pygame.mouse.get_pos(), 250, 275)
            self.quitButton.output(self.window, pygame.mouse.get_pos(), 250, 325)
            self.audioButton.output(self.window, pygame.mouse.get_pos())
        
        # Draws the achievementsscreen
        elif self.output == "achievementsScreen":
            self.window.blit(self.achievementsScreenBackground, (0, 0))
            self.backButton.output(self.window, pygame.mouse.get_pos(), 0, 450)
            self.additionAchievement.output(self.window)
            self.subtractionAchievement.output(self.window)
            self.spellingAchievement.output(self.window)
            self.punctuationAchievement.output(self.window)
        
        
        # Draws the mathmenuscreen
        elif self.output == "mathMenuScreen":
            self.mathGame.menuOutput(self.window, pygame.mouse.get_pos())
            if self.achievementUnlock:
                pygame.draw.rect(self.window, (220, 170, 0), (205, 450, 495, 50))
                pygame.draw.rect(self.window, (0, 0, 0), (202, 448, 500, 55), 2)
                self.window.blit(pygame.font.SysFont('Callibri', 25).render("Congratulations " + self.name + ", you unlocked an achievement!", 1, (0, 0, 0)), (210, 460))
                self.window.blit(pygame.font.SysFont('Callibri', 25).render("Go to the achievements house to view it!", 1, (0, 0, 0)), (210, 480))
        
        # Draws the mathgamescreen
        elif self.output == "mathGameScreen":
            self.mathGame.gameOutput(self.window, pygame.mouse.get_pos())
        
        # Draws the englishmenuscreen
        elif self.output == "englishMenuScreen":
            self.englishGame.menuOutput(self.window, pygame.mouse.get_pos())
            if self.achievementUnlock:
                pygame.draw.rect(self.window, (220, 170, 0), (205, 450, 495, 50))
                pygame.draw.rect(self.window, (0, 0, 0), (202, 448, 500, 55), 2)
                self.window.blit(pygame.font.SysFont('Callibri', 25).render("Congratulations " + self.name + ", you unlocked an achievement!", 1, (0, 0, 0)), (210, 460))
                self.window.blit(pygame.font.SysFont('Callibri', 25).render("Go to the achievements house to view it!", 1, (0, 0, 0)), (210, 480))
            
        # Draws the englishgamescreen
        elif self.output == "englishGameScreen":
            self.englishGame.gameOutput(self.window, pygame.mouse.get_pos())
        
        # If the user reward animation is active, it draws it on screen and moves to the right until it is off-screen
        if self.rewardAnimationX <= 700:
            self.window.blit(self.rewardAnimation, (self.rewardAnimationX, 225))
            self.window.blit(pygame.font.SysFont('Callibri', 70).render("Good job, " + self.name + "!", 1, (0, 175, 0)), (100, 150))
            self.rewardAnimationX += 10
        
        # Updates the window/display
        pygame.display.update()
        
    # Method which runs the main gameloop of the game
    def run(self):
        while self.running:
            self.clock.tick(self.FPS)
            self.detectUserInput()
            self.updateWindow()
 
# Creates an instance of the game and runs it          
game = Game()
game.run()