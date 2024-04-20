import pygame
from pygame.sprite import Group
from Constants import *
import Wizard

pygame.init()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

character = Wizard.Player("Player", int(WIDTH // 2.15), int(HEIGHT // 1.15))

running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN and event.key == K_ESCAPE:
            running = False

    screen.fill((255, 255, 255))

    pressedKeys = pygame.key.get_pressed()
    
    character.update(pressedKeys)
    print(character.x)

    screen.blit(character.image, character.getPosition())

    pygame.display.flip()


pygame.quit()