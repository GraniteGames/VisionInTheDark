import pygame
from pygame.locals import *


#our image source
spr_player = 'spr_player.png'

#initiate pygame
pygame.init()

#variables for positioning and speed
block_speed = 0.1
half_block_speed = 0.05
screen_height = 480
screen_width = 640
pos_x = screen_width / 2
pos_y = screen_height / 2



#create display
screen = pygame.display.set_mode((screen_width, screen_height))
#create player object to blit
player = pygame.image.load(spr_player).convert_alpha()
#game while loop
done = False
moving_right = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            pos_x += block_speed
            moving_right = True
        elif event.key == pygame.K_a:
            pos_x += -block_speed
        elif event.key == pygame.K_w:
            pos_y += -block_speed
        elif event.key == pygame.K_s:
            pos_y += block_speed

    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            pos_x += block_speed
        elif event.key == pygame.K_a:
            pos_x += -block_speed
        if event.key == pygame.K_w:
            pos_y += -block_speed
        elif event.key == pygame.K_s:
            pos_y += block_speed






    #horizontal boundaries
    if pos_x > 592:
        pos_x = 592
    elif pos_x < 0:
        pos_x = 0
    #vertical boundaries
    if pos_y > 432:
        pos_y = 432
    elif pos_y < 0:
        pos_y = 0

    #window creation and player blitting
    screen.fill((255, 255, 255))
    screen.blit(player,(pos_x,pos_y))
    pygame.display.flip()
