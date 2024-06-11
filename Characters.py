# Constants containing WIDTH and HEIGHT for the screen and values for the width and height of each sprite
from Constants import *
from pygame.sprite import Group


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

        # Sets the x and y coordinates of the sprite
        self.rect.center = (x, y)
    

class Wizard(Character):
    def __init__(self, originalImage, width, height,projectileGroup, x=0, y=0):
        Character.__init__(self, originalImage, width, height, x, y)

        self.projectileGroup = projectileGroup

        # Determines whether the projectile is on cooldown or not
        self.onCooldown = False

        # Remaining delay for projectile
        self.coolDown = 0

        # Delay of projectile in ms
        self.shootDelay =   35


    # Moves the wizard when the user presses left or right
    def update(self, pressedKeys):
            
            # Moves wizard to the left if left key is pressed
            # and it's within the left boundary
            if pressedKeys[K_LEFT]:
                if self.rect.center[0] > 0 + self.width // 2:
                    self.rect.move_ip(-7, 0)
            
            # Moves wizard to the right if right key is pressed
            # and it's within the right boundary
            if pressedKeys[K_RIGHT]:
                if self.rect.center[0] < WIDTH - self.width // 2:
                    self.rect.move_ip(7, 0)
            
            # Shoots the projectile if it's not on cooldown and sets it on cooldown
            if pressedKeys[K_SPACE] and not self.onCooldown:
                self.shoot()
                self.onCooldown = True
                self.coolDown = self.shootDelay
            
            # While on cooldown, adjust the current coolDown counter by -1ms
            if self.onCooldown:
                self.coolDown -= 1

                # If the coolDown counter is 0, set onCooldown to False
                if self.coolDown == 0:
                    self.onCooldown = False
                
    
    def shoot(self):
        # Makes a projectile with the wizard's (x, y) coordaintes and adds it to a group
        projectile = Projectile("Sprites/fireball.png", projectileWidth, projectileHeight, self.rect.center[0], self.rect.center[1])
                
        self.projectileGroup.add(projectile)


class Spider(Character):
    def __init__(self, originalImage, width, height, x=0, y=100):
        Character.__init__(self, originalImage, width, height, x, y)
        self.speed = 3

    # Spider moves across the screen from left to right
    def update(self):
        self.rect.move_ip(self.speed, 0)

class Projectile(Character):
    def __init__(self, originalImage, width, height, x=0, y=0):
        Character.__init__(self, originalImage, width, height, x, y)

    # Moves projectile up the screen and kills it once it reaches the top
    def update(self):
        self.rect.move_ip(0, -7)

        if self.rect.center[1] < 0:
            self.kill()

