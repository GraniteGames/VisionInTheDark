import pygame
from pygame.locals import *

# initiate pygame
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

Vector2 = pygame.math.Vector2

# create display
screen_width = 64 * 15
screen_height = 64 * 10
screen = pygame.display.set_mode((screen_width, screen_height))

speed = 8
player = pygame.image.load('spr_player2.png').convert_alpha()
pos = Vector2(screen_width / 2 - 32, screen_height / 2 - 32)
char_width = 64
char_height = 64



wall = pygame.image.load('wall_tile.png').convert_alpha()
wall_pos = Vector2(128, 128)
wall_col = pygame.Rect(wall_pos.x-4, wall_pos.y-4, 68, 68)


def player_movement():
    # variable for key press
    pressed_keys = pygame.key.get_pressed()

    # horizontal movement
    if pressed_keys[K_a] and player_col.colliderect(wall_col) == False:
        pos.x -= speed
    if pressed_keys[K_d]and player_col.colliderect(wall_col) == False:
        pos.x += speed

    # vertical movement
    if pressed_keys[K_w]and player_col.colliderect(wall_col) == False:
        pos.y -= speed
    if pressed_keys[K_s]:
        pos.y += speed

# game while loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    player_col = pygame.Rect(pos.x - 4, pos.y - 4, 68, 68)
    player_movement()

    # horizontal boundaries
    if pos.x > screen_width - char_width:
        pos.x = screen_width - char_width
    elif pos.x < 0:
        pos.x = 0
    # vertical boundaries
    if pos.y > screen_height - char_height:
        pos.y = screen_height - char_height
    elif pos.y < 0:
        pos.y = 0

    # window creation and player blitting
    screen.fill((135, 135, 135))
    screen.blit(player, pos)
    screen.blit(wall, (wall_pos.x, wall_pos.y))

    pygame.display.update()
    fpsClock.tick(FPS)
