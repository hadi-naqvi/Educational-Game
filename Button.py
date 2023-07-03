# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - button.py

# Class for buttons
class Button(object):
    # Initialization Method
    def __init__(self, normalSprite, hoverSprite):
        self.width = normalSprite.get_width()
        self.height = normalSprite.get_height()
        self.normalSprite = normalSprite
        self.hoverSprite = hoverSprite
        self.sprite = self.normalSprite
    
    # Method which detects if the mouse if hovering over the button
    def mouseHover(self, mousePos, x, y):
        if x <= mousePos[0] <= x + self.width and y <= mousePos[1] <= y + self.height:
            self.sprite = self.hoverSprite
            return True
        else: 
            self.sprite = self.normalSprite
            return False
  
    # Method which outputs the button on screen
    def output(self, window, mousePos, x, y):
        if self.mouseHover(mousePos, x, y):
            window.blit(self.hoverSprite, (x, y))
        else:
            window.blit(self.normalSprite, (x, y))