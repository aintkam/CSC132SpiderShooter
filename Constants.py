#####################################################################
#   File containing constants that you might need in your assignment.
#   Make sure to import the library in all your files using a statement
#   like:
#   from Constants import *
#####################################################################

# import libraries that you will need
import pygame
from random import randint, choice

pygame.init()

# constants for screen size
WIDTH = 1200
HEIGHT = 1000

# sets FPS constant for the game
fps = 144

# Time delay in ms for adding a new spider
spiderCooldown = 1000

# Font used for on-screen text
font = pygame.font.SysFont(None, 36)

# Font used for the "Game Over" screen
gameOverFont = pygame.font.SysFont(None, 50)

# Creating a new custom event for adding more spiders
ADDSPIDER = pygame.USEREVENT + 1
pygame.time.set_timer(ADDSPIDER, spiderCooldown)

# sets constants for wizard size
wizardWidth = lambda originalWidth: originalWidth // 3
wizardHeight = lambda originalHeight: originalHeight // 3

# sets constants for spider size
spiderWidth = lambda originalWidth: originalWidth // 5
spiderHeight = lambda originalHeight: originalHeight // 5

# sets constants for fireball size
projectileWidth = lambda originalWidth: originalWidth // 25
projectileHeight = lambda originalHeight: originalHeight // 25

# constants for colors
RED = [0xe3, 0x1b, 0x23]
BLUE = [0x00,0x2F,0x8B]
GREY = [0xA2, 0xAA, 0xAD]
WHITE = [0xFF, 0xFF, 0xFF]
BLACK = [0x00, 0x00, 0x00]

COLORS = [BLUE, RED, GREY, WHITE, BLACK]

# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
    K_RETURN
)
