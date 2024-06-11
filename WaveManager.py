from Constants import *
from pygame.sprite import Group

class WaveManager:
    def __init__(self):

        self.lives = 3

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
            
            # When a new wave starts, set the lives back to 3
            self.lives = 3

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
            self.updateSpiderSpeed(4)
            
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
