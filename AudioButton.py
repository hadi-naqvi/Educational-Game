# Date: December 14th, 2019
# Author: Hadi Naqvi
# Description: Santa's Christmas Challenges - AudioButton.py

# Class for the audio button
class AudioButton(object):
    # Initialization/Constructor method
    def __init__(self, x, y, unmutedSprite, unmutedHoverSprite, mutedSprite, mutedHoverSprite):
        self.x = x
        self.y = y
        self.width = unmutedSprite.get_width()
        self.height = unmutedSprite.get_height()
        self.unmutedSprite = unmutedSprite
        self.unmutedHoverSprite = unmutedHoverSprite
        self.mutedSprite = mutedSprite
        self.mutedHoverSprite = mutedHoverSprite
        self.sprite = self.unmutedSprite
    
    # Method which detects if the user is hovering over the audio button
    def mouseHover(self, mousePos):
        if self.x <= mousePos[0] <= self.x + self.width and self.y <= mousePos[1] <= self.y + self.height:
            return True
   
    # Method which draws the audio button on-screen
    def output(self, window, mousePos):
        if self.mouseHover(mousePos):
            if self.sprite == self.unmutedSprite or self.sprite == self.unmutedHoverSprite:
                window.blit(self.unmutedHoverSprite, (self.x, self.y))
            elif self.sprite == self.mutedSprite or self.sprite == self.mutedHoverSprite:
                window.blit(self.mutedHoverSprite, (self.x, self.y))
        else:
            window.blit(self.sprite, (self.x, self.y))