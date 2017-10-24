import pygame
import math
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('spr_player.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.speed = 0.01
        self.angle = 0

        def move(self):
            self.x += math.sin(self.angle) * self.speed
            self.y -= math.cos(self.angle) * self.speed

#our image source
spr_player = 'spr_player.png'

#initiate pygame
pygame.init()

#variables for positioning and speed
pos_x = 296
pos_y = 216
speed_V = 0
speed_H = 0
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
    if pressedKeys[K_a]:
      #  pos_x += speed_H
        speed_H = speed_H - 0.0001
        if speed_H <= -0.5:
            speed_H = -0.5
        print speed_H
    elif pressedKeys[K_d]:
      #  pos_x += speed_H
        speed_H = speed_H + 0.0001
        if speed_H >= 0.5:
            speed_H = 0.5
    #vertical movement
    if pressedKeys[K_w]:
       # pos_y += speed_V
        speed_V = speed_V + 0.0001
        if speed_V >= 0.5:
            speed_V = 0.5
    if pressedKeys[K_s]:
       # pos_y += speed_V
        speed_V = speed_V - 0.0001
        if speed_V <= -0.5:
            speed_V = -0.5

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

done_2 = False
while not done_2:
    pos_y += speed_V
    pos_x += speed_H
    done_2 = True
    #window creation and player blitting
    screen.fill((255, 255, 255))
    screen.blit(player,(pos_x,pos_y))
    pygame.display.flip()

