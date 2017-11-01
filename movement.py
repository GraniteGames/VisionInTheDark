import pygame
from pygame.locals import *

Vector2 = pygame.math.Vector2
clock = pygame.time.Clock()


def player_movement(player):
    # variable for key press
    pressed_keys = pygame.key.get_pressed()

    # horizontal movement
    if pressed_keys[K_a]:
        player.pos.x -= player.speed

    if pressed_keys[K_d]:
        player.pos.x += player.speed

    # vertical movement
    if pressed_keys[K_w]:
        player.pos.y -= player.speed

    if pressed_keys[K_s]:
        player.pos.y += player.speed


#def deceleration(player):
    '''
    while player.vel != 0:
        if player.vel < 0:
            clock.get_time()

        else:
            clock.get_time()
    '''