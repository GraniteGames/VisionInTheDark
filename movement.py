import pygame
from pygame.locals import *


def player_movement(Player):

    # variable for key press
    pressed_keys = pygame.key.get_pressed()

    # horizontal movement
    if pressed_keys[K_a]:
        Player.pos.x -= Player.speed
    if pressed_keys[K_d]:
        Player.pos.x += Player.speed

    # vertical movement
    if pressed_keys[K_w]:
        Player.pos.y -= Player.speed
    if pressed_keys[K_s]:
        Player.pos.y += Player.speed