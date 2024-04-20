import pygame
from pygame.sprite import Group
from Constants import *
from Item import *

class Player(pygame.sprite.Sprite, Item):
    def __init__(self,name: str, x=0, y=0):

        pygame.sprite.Sprite.__init__(self)
        Item.__init__(self, name, x, y)

        #Gets the original image and its size
        self.originalImage = pygame.image.load("Sprites/wizard.png").convert_alpha()
        
        self.originalWidth, self.originalHeight = self.originalImage.get_size()

        #Changes the scaling of the Wizard to make it smaller
        self.width = wizardWidth(self.originalWidth)
        self.height = wizardHeight(self.originalHeight)

        #Sets the Sprite
        self.image = pygame.transform.scale(self.originalImage, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.x = WIDTH - self.image.get_size()[0]
        self.y = y - self.height
    
    def getPosition(self):
        return (self.x - self.size / 2,  self.y - self.size / 2)

    def update(self, pressedKeys):
        if pressedKeys[K_LEFT]:
            self.goLeft()

        elif pressedKeys[K_RIGHT]:
            self.goRight()
    
    def getSize(self):
        print(self.size)