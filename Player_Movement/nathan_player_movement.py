import pygame
import random
import os
from pygame.locals import *

pygame.init()

'''Image source'''
spr_player = 'spr_player.png'
spr_wall = 'spr_wall.png'
'''Variable for object sizes'''
screen_width = 1280
screen_height = 960
player_width = 48
player_height = 48

'''Player variables for position and speeds'''
pos_x = (screen_width / 2) - (player_width / 2)
pos_y = (screen_height / 2) - (player_height / 2)
speed_vertical = 0
speed_horizontal = 0
speed_increase = 0.02
speed_limit = 1

'''Screen and player creation'''
screen = pygame.display.set_mode((screen_width, screen_height))
player = pygame.image.load(spr_player).convert_alpha()
wall = pygame.image.load(spr_wall)
#recttangle = pygame.draw.rect(screen, (0,0,0), player, 0)
#player_collision = player.rect()

class Player(object):

    def __int__(self):
        self.rect = pygame.Rect(32, 32, 16, 16)

        def move(self, dx, dy):

            if dx != 0:
                self.move_single_axis(dx,0)
            if dy != 0:
                self.move_single_axis(0, dy)

        def move_single_axis(self, dx, dy):

            self.rect.x += dx
            self.rect.y += dy

            for wall in walls:
                if self.rect.colliderect(wall.rect):
                    if dx > 0:  # Moving right; Hit the left side of the wall
                        self.rect.right = wall.rect.left
                    if dx < 0:  # Moving left; Hit the right side of the wall
                        self.rect.left = wall.rect.right
                    if dy > 0:  # Moving down; Hit the top side of the wall
                        self.rect.bottom = wall.rect.top
                    if dy < 0:  # Moving up; Hit the bottom side of the wall
                        self.rect.top = wall.rect.bottom


# Nice class to hold a wall rect
class Wall(object):
    def __init__(self, pos):
        walls.append(self)
        self.rect = pygame.Rect(pos[0], pos[1], 16, 16)

'''Game loop'''
done = False
while not done:



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True


    # horizontal boundaries
    if pos_x > (screen_width - player_width):
        pos_x = (screen_width - player_width)
    elif pos_x < 0:
        pos_x = 0

    # vertical boundaries
    if pos_y > (screen_height - player_height):
        pos_y = (screen_height - player_height)
    elif pos_y < 0:
        pos_y = 0

    # window creation and player blitting
    screen.fill((255, 255, 255))
    screen.blit(wall,(100,100))
    screen.blit(player, (pos_x, pos_y))
    pygame.display.flip()

