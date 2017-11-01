import pygame
from screen_settings import *
from player_class import *
from movement import *
from map_genreator import *

# initiate pygame
pygame.init()

# limiting the FPS with this fps clock
FPS = 60
fpsClock = pygame.time.Clock()

player = Player(screen_width / 2 - 32, screen_height / 2 - 32)

generate_a_map()

# game while loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            generate_a_map()

    # running core gameplay elements
    render_map()
    player.render(screen)
    player_movement(player)

    pygame.display.update()
    fpsClock.tick(FPS)
