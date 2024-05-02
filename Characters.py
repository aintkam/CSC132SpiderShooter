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

class WaveManager:
    def __init__(self):

        # Sets the wave
        self.currentWave = 1

        # Sets base spiders for each wave
        self.baseSpiders = 3

        # Sets how many more spiders should spawn each wave
        self.ratio = 1.7

        # Timer for spider spawning cooldown
        self.spawnTimer = 500

        # Running timer since last spawn
        self.timeToSpawn = 0

        # Timer for wave cooldown
        self.waveTimer = 1500

        # Running timer since last spider killed
        self.timeUntilWave = 0

        # Total number of spiders for current wave
        self.totalSpiders = self.numSpiders()

        # Ttotal spiders spawned for current wave
        self.spidersSpawned = 0

    # Gets the number of spiders for that wave
    def numSpiders(self):
        return int(self.baseSpiders + (self.ratio * self.currentWave))
    
    # Manually calls the ADDSPIDER event
    def triggerEvent(self):
        pygame.event.post(pygame.event.Event(ADDSPIDER))
    
    # Updates how fast the spider moves
    def updateSpiderSpeed(self, value):
        for spider in spiderGroup:
            spider.speed = value
    
    # Checks if the wave timer sould be incrimented or if the wave should be incrimented
    def updateWave(self):
        if self.timeUntilWave > 0:
            self.timeUntilWave -= 1
        else:
            self.currentWave += 1
            self.timeUntilWave = self.waveTimer
            self.spidersSpawned = 0
            self.totalSpiders = self.numSpiders()
    
    # Checks if it can spawn a spider or not
    def updateSpawn(self):
        
        # If running count isn't 0, decrease its value 
        if self.timeToSpawn > 0:
            self.timeToSpawn -= 1

        # If the total number of spiders spawned for current wave hasn't been spawned
        # yet and running timer is 0, spawn spider, increase total spiders spawned, reset spawn running timer and wave running timer
        if self.spidersSpawned < self.totalSpiders and self.timeToSpawn <= 0:
            self.triggerEvent()
            self.timeToSpawn = self.spawnTimer
            self.spidersSpawned += 1
            self.timeUntilWave = self.waveTimer



    def update(self):

        # Updates the spawning and waves
        self.updateSpawn()
        
        self.updateWave()
        
        # Decreases spawn cooldown and increases spider speed to the game after given amount of waves
        # To increase difficulty
        if self.currentWave >= 3:
            self.spawnTimer = 450
            self.updateSpiderSpeed(5)
            
        elif self.currentWave >= 5:
            self.spawnTimer = 400
        
        elif self.currentWave >= 10:
            self.spawnTimer = 325
            self.updateSpiderSpeed(6)
        
        elif self.currentWave >= 15:
            self.spawnTimer = 275
        
        elif self.currentWave > 20:
            self.spawnTimer = 200
            self.updateSpiderSpeed(8)
