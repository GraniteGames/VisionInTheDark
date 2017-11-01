import pygame
from pygame.locals import *

Vector2 = pygame.math.Vector2
clock = pygame.time.Clock()


def player_movement(Player):
    """"# variable for key press
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
        player.pos.y += player.speed"""


#def deceleration(player):
    '''
    while player.vel != 0:
        if player.vel < 0:
            clock.get_time()

        else:
            clock.get_time()
    '''

    pressed_keys = pygame.key.get_pressed()

    Player.dt_up = Player.clock_up.tick()
    Player.dt_down = Player.clock_down.tick()
    Player.dt_left = Player.clock_left.tick()
    Player.dt_right = Player.clock_right.tick()

    Player.time_elapsed_since_last_action_up += Player.dt_up
    Player.time_elapsed_since_last_action_down += Player.dt_down
    Player.time_elapsed_since_last_action_left += Player.dt_left
    Player.time_elapsed_since_last_action_right += Player.dt_right

    Player.pos.x += Player.speed_h
    Player.pos.y += Player.speed_v

    # movement up
    if Player.time_elapsed_since_last_action_up > Player.milliseconds:
        if pressed_keys[K_w]:
            Player.pos.y += Player.speed_v
            Player.speed_v -= Player.increase
            Player.time_elapsed_since_last_action_up = 0
            if Player.speed_v <= - Player.speed_limit:
                Player.speed_v = - Player.speed_limit
            print Player.speed_v

    # movement down
    if Player.time_elapsed_since_last_action_down > Player.milliseconds:
        if pressed_keys[K_s]:
            Player.pos.y += Player.speed_v
            Player.speed_v += Player.increase
            Player.time_elapsed_since_last_action_down = 0
            if Player.speed_v >= Player.speed_limit:
                Player.speed_v = Player.speed_limit
            print Player.speed_v

    # movement left
    if Player.time_elapsed_since_last_action_left > Player.milliseconds:
        if pressed_keys[K_a]:
            Player.pos.x += Player.speed_h
            Player.speed_h -= Player.increase
            Player.time_elapsed_since_last_action_left = 0
            if Player.speed_h <= - Player.speed_limit:
                Player.speed_h = - Player.speed_limit
            print Player.speed_h

    # movement right
    if Player.time_elapsed_since_last_action_right > Player.milliseconds:
        if pressed_keys[K_d]:
            Player.pos.x += Player.speed_h
            Player.speed_h += Player.increase
            Player.time_elapsed_since_last_action_right = 0
            if Player.speed_h >= Player.speed_limit:
                Player.speed_h = Player.speed_limit
            print Player.speed_h