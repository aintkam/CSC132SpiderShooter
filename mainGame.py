from pygame.sprite import Group
from Constants import *
from Characters import *

# Clock for updating the game on a set interval (FPS)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Sets the groups for sprites
spiderGroup = pygame.sprite.Group()

playerGroup = pygame.sprite.Group()

projectileGroup = pygame.sprite.Group()

# Creates the player
character = Wizard("Sprites/wizard.png",  wizardWidth, wizardHeight, projectileGroup, WIDTH // 2.15, HEIGHT //1.15)

# Adds player to its group
playerGroup.add(character)

# Initializes the score and lives for the game
score = 0
lives = 3

# Initializes the game running
running = True

# Value for if the game has ended or not
gameOver = False

while running:
    if not gameOver:
        for event in pygame.event.get():

            # Checks if user exits the window or presses escape then quits game
            if event.type == pygame.QUIT:
                running = False

            elif event.type == KEYDOWN and event.key == K_ESCAPE:
                running = False
            
            # Adds a new spider to the game
            elif event.type == ADDSPIDER:
                newSpider = Spider("Sprites/spider.png", spiderWidth, spiderHeight, randint(0, 150), randint(40, 750))
                spiderGroup.add(newSpider)
        
        # Ends the game if the player runs out of lives
        if lives <= 0:
            gameOver = True

        # Sets background of game to white
        screen.fill((255, 255, 255))

        # Checks any keys pressed
        pressedKeys = pygame.key.get_pressed()
        
        # moves the character if left or right is pressed and shoots if space is pressed
        character.update(pressedKeys)

        # updates the spiders' state
        spiderGroup.update()

        # updates the projectile's state
        projectileGroup.update()

        # Adds collisions between projectile and spider, automatically kills both if they collide
        collisions = pygame.sprite.groupcollide(projectileGroup, spiderGroup, True, True)

        # For every spider hit, add 1 to the current score
        for projectile, spidersHit in collisions.items():
            for spider in spidersHit:
                score += 1

        # Once the spider hits the border, it gets killed and lives get decreased
        for spider in spiderGroup:
            if spider.rect.center[0] >= WIDTH:
                lives -= 1
                spider.kill()
        
        # Draws the number of lives in the top left hand corner
        livesText = font.render(f"Lives: {lives}", True, (0,0,0))
        screen.blit(livesText, (15, 10))

        # Draws the score in the top right hand corner
        scoreText = font.render(f"Score: {score}", True, (0,0,0))
        screen.blit(scoreText, (WIDTH-115, 10))

        # draws the character, spiders, and projectiles to the screen
        playerGroup.draw(screen)
        spiderGroup.draw(screen)
        projectileGroup.draw(screen)

    # If game is over, create a "Game Over" screen
    else:
            for event in pygame.event.get():
                
                # Quits the game if the user closes the window
                if event.type == pygame.QUIT:
                    running = False
                    gameOver = False

                elif event.type == KEYDOWN:
                    
                    # Quits the game if user presses escape
                    if event.key == K_ESCAPE:
                        running = False
                        gameOver = False

                    # Restarts the game if user presses enter
                    elif event.key == K_RETURN:
                        lives = 3
                        gameOver = False

                        spiderGroup.empty()
                        projectileGroup.empty()
                        character.rect.center = (WIDTH // 2.15, HEIGHT //1.15)

            screen.fill((255, 255, 255))

            # Adds text to indicate the game is over and shows the player their score
            gameOverText = gameOverFont.render(f"Game Over: You made it to {score}!", True, (0,0,0))
            screen.blit(gameOverText, (WIDTH // 2 - 250, HEIGHT // 2))

            # Text for telling the player what key restarts the game
            restartText = gameOverFont.render("Press Enter to Restart", True, (0,0,0))
            screen.blit(restartText, (WIDTH // 4 - 175 , HEIGHT // 2 + 75))

            # Text for telling the player what key exits the game
            exitText = gameOverFont.render("Press Escape to Quit", True, (0,0,0))
            screen.blit(exitText, (WIDTH// 2 + 50, HEIGHT // 2 + 75))


    # Updates the screen
    pygame.display.update()

    # Limit the FPS by sleeping for the remainder of the frame time
    clock.tick(fps)



pygame.quit()