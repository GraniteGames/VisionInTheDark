import pygame
from pygame.locals import *

Vector2 = pygame.math.Vector2
clock = pygame.time.Clock()


def player_movement(Player, wall):

    pressed_keys = pygame.key.get_pressed()

    Player.dt_up = Player.clock_up.tick()
    Player.dt_down = Player.clock_down.tick()
    Player.dt_left = Player.clock_left.tick()
    Player.dt_right = Player.clock_right.tick()

    Player.time_elapsed_since_last_action_up += Player.dt_up
    Player.time_elapsed_since_last_action_down += Player.dt_down
    Player.time_elapsed_since_last_action_left += Player.dt_left
    Player.time_elapsed_since_last_action_right += Player.dt_right

    # movement up
    if Player.time_elapsed_since_last_action_up > Player.milliseconds:
        if pressed_keys[K_w] or pressed_keys[K_UP]:
            Player.speed_v -= Player.increase
            Player.time_elapsed_since_last_action_up = 0
            if Player.speed_v <= - Player.speed_limit:
                Player.speed_v = - Player.speed_limit
            #print Player.speed_v

    # movement down
    if Player.time_elapsed_since_last_action_down > Player.milliseconds:
        if pressed_keys[K_s] or pressed_keys[K_DOWN]:
            Player.speed_v += Player.increase
            Player.time_elapsed_since_last_action_down = 0
            if Player.speed_v >= Player.speed_limit:
                Player.speed_v = Player.speed_limit
            #print Player.speed_v

    # movement left
    if Player.time_elapsed_since_last_action_left > Player.milliseconds:
        if pressed_keys[K_a] or pressed_keys[K_LEFT]:
            Player.speed_h -= Player.increase
            Player.time_elapsed_since_last_action_left = 0
            if Player.speed_h <= - Player.speed_limit:
                Player.speed_h = - Player.speed_limit
            #print Player.speed_h

    # movement right
    if Player.time_elapsed_since_last_action_right > Player.milliseconds:
        if pressed_keys[K_d] or pressed_keys[K_RIGHT]:
            Player.speed_h += Player.increase
            Player.time_elapsed_since_last_action_right = 0
            if Player.speed_h >= Player.speed_limit:
                Player.speed_h = Player.speed_limit
            #print Player.speed_h

    collision_detect(Player, wall)

    Player.pos.x += Player.speed_h
    Player.pos.y += Player.speed_v


def collision_detect(Player, wall_list):
    collision_rect = Player.rect

    collision_rect.left += Player.speed_h
    collision_rect.right += Player.speed_h
    collision_rect.top += Player.speed_v
    collision_rect.bottom += Player.speed_v
    for wall in wall_list:
        if collision_rect.colliderect(wall.rect):
            #print "collided!"

            if Player.rect.x < wall.rect.x:
                Player.speed_h = -0.5

            elif Player.rect.x > wall.rect.x:
                Player.speed_h = 0.5

            if Player.rect.y < wall.rect.y:
                Player.speed_v = -0.5

            elif Player.rect.y > wall.rect.y:
                Player.speed_v = 0.5