import pygame
from pygame.locals import *


#our image source
spr_player = 'spr_player.png'

#initiate pygame
pygame.init()

#variables for positioning and speed
speed = 0.1
pos_x = 296
pos_y = 216


#create display
screen = pygame.display.set_mode((640, 480))
#create player object to blit
player = pygame.image.load(spr_player).convert_alpha()
#game while loop
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
    #variable for key press
    pressedKeys = pygame.key.get_pressed()
    #horizontal movement
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
            pos_x -= speed
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_a:
            pos_x -= speed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_d:
            pos_x += speed
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_d:
            pos_x += speed

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_w:
            pos_y -= speed
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_w:
            pos_y -= speed
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_s:
            pos_y += speed
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_s:
            pos_y += speed







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
