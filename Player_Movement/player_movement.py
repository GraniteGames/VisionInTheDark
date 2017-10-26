import pygame
from pygame.locals import *

pygame.init()

'''Created clocks to make movement smoother, each key_pressed action loop has 
a separate clock to stop the overlapping of events'''
time_elapsed_since_last_action_up = 0
time_elapsed_since_last_action_down = 0
time_elapsed_since_last_action_left = 0
time_elapsed_since_last_action_right = 0
clock_up = pygame.time.Clock()
clock_down = pygame.time.Clock()
clock_left = pygame.time.Clock()
clock_right = pygame.time.Clock()
milliseconds = 100

'''Image source'''
spr_player = 'spr_player.png'

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

'''Game loop'''
done = False
while not done:

    # setting up clock variables to start each clock and set timers for
    # each direction of player movement
    dt_up = clock_up.tick()
    dt_down = clock_down.tick()
    dt_left = clock_left.tick()
    dt_right = clock_right.tick()

    time_elapsed_since_last_action_up += dt_up
    time_elapsed_since_last_action_down += dt_down
    time_elapsed_since_last_action_left += dt_left
    time_elapsed_since_last_action_right += dt_right

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True


    pressedKeys = pygame.key.get_pressed()

    # keeps the momentum when keys are let go
    pos_x += speed_horizontal
    pos_y += speed_vertical

    # movement up
    if time_elapsed_since_last_action_up > milliseconds:
        if pressedKeys[K_w]:
            pos_y += speed_vertical
            speed_vertical -= speed_increase
            time_elapsed_since_last_action_up = 0
            if speed_vertical <= - speed_limit:
                speed_vertical = - speed_limit
            print speed_vertical

        # movement down
        if time_elapsed_since_last_action_down > milliseconds:
            if pressedKeys[K_s]:
                pos_y += speed_vertical
                speed_vertical += speed_increase
                time_elapsed_since_last_action_down = 0
                if speed_vertical >= speed_limit:
                    speed_vertical = speed_limit
                print speed_vertical

    # movement left
    if time_elapsed_since_last_action_left > milliseconds:
        if pressedKeys[K_a]:
            pos_x += speed_horizontal
            speed_horizontal -= speed_increase
            # reset to zero
            time_elapsed_since_last_action_left = 0
            # sets a maximum speed limit
            if speed_horizontal <= - speed_limit:
                speed_horizontal = - speed_limit
            print speed_horizontal

    # movement right
    if time_elapsed_since_last_action_right > milliseconds:
        if pressedKeys[K_d]:
            pos_x += speed_horizontal
            speed_horizontal += speed_increase
            time_elapsed_since_last_action_right = 0
            if speed_horizontal >= speed_limit:
                speed_horizontal = speed_limit
            print speed_horizontal

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
    screen.blit(player, (pos_x, pos_y))
    pygame.display.flip()

