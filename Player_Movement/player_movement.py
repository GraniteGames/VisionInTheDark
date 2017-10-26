import pygame
from pygame.locals import *

time_elapsed_since_last_action = 0
clock = pygame.time.Clock()
milliseconds = 100

#our image source
spr_player = 'spr_player.png'

#initiate pygame
pygame.init()


#variables for positioning and speed
pos_x = 296
pos_y = 216
speed_V = 0
speed_H = 0
speed_increase = 0.002
speed_limit = 1
#create display
screen = pygame.display.set_mode((640, 480))
#create player object to blit
player = pygame.image.load(spr_player).convert_alpha()
#game while loop
done = False
while not done:
    dt = clock.tick()

    time_elapsed_since_last_action += dt
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    #variable for key press
    pressedKeys = pygame.key.get_pressed()
    #horizontal movement
    pos_x += speed_H
    pos_y += speed_V
    if time_elapsed_since_last_action > milliseconds:
        if pressedKeys[K_a]:
            pos_x += speed_H
            speed_H = speed_H - speed_increase
            time_elapsed_since_last_action = 0
            if speed_H <= - speed_limit:
                speed_H = - speed_limit
            print speed_H

    if time_elapsed_since_last_action > milliseconds:
        if pressedKeys[K_d]:
            pos_x += speed_H
            speed_H = speed_H + speed_increase
            time_elapsed_since_last_action = 0
            if speed_H >= speed_limit:
                speed_H = speed_limit
            print speed_H
    #vertical movement

    if time_elapsed_since_last_action > milliseconds:
        if pressedKeys[K_s]:
            pos_y += speed_V
            speed_V = speed_V + speed_increase
            time_elapsed_since_last_action = 0
            if speed_V >= speed_limit:
                speed_V = speed_limit
            print speed_V

    if time_elapsed_since_last_action > milliseconds:
        if pressedKeys[K_w]:
            pos_y += speed_V
            speed_V = speed_V - speed_increase
            time_elapsed_since_last_action = 0
            if speed_V <= - speed_limit:
                speed_V = - speed_limit
            print speed_V

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

