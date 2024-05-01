import pygame
from pygame.sprite import Group
from Constants import *
from Characters import *

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Creates the wizard 
spider = Spider("Sprites/spider.png", spiderWidth, spiderHeight, 15, randint(40, 750))

# Sets the groups for sprites
spiderGroup = pygame.sprite.Group()
spiderGroup.add(spider)

playerGroup = pygame.sprite.Group()

projectileGroup = pygame.sprite.Group()

character = Wizard("Sprites/wizard.png",  wizardWidth, wizardHeight, projectileGroup, WIDTH // 2.15, HEIGHT //1.15)

playerGroup.add(character)

running = True

while running:

    for event in pygame.event.get():

        # Checks if user quits the game
        if event.type == pygame.QUIT:
            running = False

        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.fill((255, 255, 255))

    pressedKeys = pygame.key.get_pressed()
    
    # moves the character if left or right is pressed
    character.update(pressedKeys)

    # updates the spiders' position
    spiderGroup.update()

    # updates the projectile's position
    projectileGroup.update()

    # draws the character, spiders, and projectiles to the screen
    playerGroup.draw(screen)
    spiderGroup.draw(screen)
    projectileGroup.draw(screen)


    pygame.display.flip()


pygame.quit()