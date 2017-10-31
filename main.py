import pygame
from player_class import *
from movement import *


# initiate pygame
pygame.init()

# limiting the FPS with this fps clock
FPS = 60
fpsClock = pygame.time.Clock()

# create display
screen_width = 64 * 15
screen_height = 64 * 10
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("The Game")

player = Player(screen_width / 2 - 32, screen_height / 2 - 32)

# game while loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False




    # window creation and player blitting
    screen.fill((0, 0, 0))
    player_movement(player)
    player.render(screen)


    pygame.display.update()
    fpsClock.tick(FPS)