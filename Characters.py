import pygame
from pygame.sprite import Group
from Constants import *

class Character(pygame.sprite.Sprite):
    def __init__(self, spriteImage, getWidth, getHeight, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        
        # Gets original image
        self.originalImage = pygame.image.load(spriteImage).convert_alpha()
        
        # Gets original image's size (width, height)
        self.originalWidth, self.originalHeight = self.originalImage.get_size()

        # Changes scaling of the Wizard to make it smaller
        self.width = getWidth(self.originalWidth)
        self.height = getHeight(self.originalHeight)

        # Sets the Sprite
        self.image = pygame.transform.scale(self.originalImage, (self.width, self.height))
        self.rect = self.image.get_rect()

        self.rect.center = (x, y)
    

class Wizard(Character):
    def __init__(self, originalImage, width, height,projectileGroup, x=0, y=0):
        Character.__init__(self, originalImage, width, height, x, y)

        self.projectileGroup = projectileGroup

    # Moves the wizard when the user presses left or right
    def update(self, pressedKeys):
            
            # Moves wizard to the left if left key is pressed
            # and it's within the left boundary
            if pressedKeys[K_LEFT]:
                if self.rect.center[0] > 0 + self.width // 2:
                    self.rect.move_ip(-1, 0)
            
            # Moves wizard to the right if right key is pressed
            # and it's within the right boundary
            if pressedKeys[K_RIGHT]:
                if self.rect.center[0] < WIDTH - self.width // 2:
                    self.rect.move_ip(1, 0)
            
            # Shoots the projectile if it's not on cooldown
            if pressedKeys[K_SPACE]:
                self.shoot()
  
    
    def shoot(self):
        projectile = Projectile("Sprites/fireball.png", projectileWidth, projectileHeight, WIDTH // 2.15, HEIGHT //1.15)
                
        self.projectileGroup.add(projectile)


class Spider(Character):
    def __init__(self, originalImage, width, height, x=0, y=100):
        Character.__init__(self, originalImage, width, height, x, y)

    # Spider moves across the screen, from left to right
    def update(self):
        self.rect.move_ip(1, 0)

        # Once the spider hits the border, it gets killed
        if self.rect.center[0] > WIDTH:
            self.kill()

class Projectile(Character):
    def __init__(self, originalImage, width, height, x=0, y=0):
        Character.__init__(self, originalImage, width, height, x, y)

    def update(self):
        self.rect.move_ip(0, -3)

        if self.rect.center[1] < 0:
            self.kill()

