import pygame
import time

pygame.init()

# constants
WIDTH = 1920
HEIGHT =  1080

# initialize the game screen
screen = pygame.display.set_mode([WIDTH,HEIGHT],pygame.FULLSCREEN)
pygame.display.set_caption("Cave Explorer")

import Levels
import Level_1
import Player
import Healthbar
import TextRender

next_level = 1
level_num = 0

# add first level sprites
sprite_list = pygame.sprite.LayeredUpdates()
player = Player.Player(1400,200)
health_bar = Healthbar.HealthBar()
level = Level_1.Level01(WIDTH, HEIGHT)

# Populate sprite list with platforms
sprite_list.add(level.platforms)
player.block_list = sprite_list
sprite_list.add(health_bar)

# Add all levels to the level list




# Initialize game clock
clock = pygame.time.Clock()

done = False

# --------- Main Loop --------------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                done = True
            elif event.key == pygame.K_SPACE:
                player.move_up()
            elif event.key == pygame.K_f:
                player.interact()
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move_left()
    if keys[pygame.K_d]:
        player.move_right()
        
            
    # Draw everything to screen
    screen.blit(level.background,[0,0])
    sprite_list.draw(screen)
    screen.blit(player.image,player.rect.topleft)

    # Call updates
    player.update()
    health_bar.update(player.health)
    level.enemies.update(player)

    # load next level
    if player.level_complete:
        

        # Get rid of old sprites
        
        
    # Display refreshed screen
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()

