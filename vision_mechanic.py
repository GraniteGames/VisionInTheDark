from screen_settings import *
from player_class import *
from map_genreator import *


def vision_mechanic(player_x, player_y):

    display = (screen_width, screen_height)
    screen.blit(map_image, (0, 0))
    fog_of_war = pygame.Surface(display)
    pygame.draw.circle(fog_of_war, (60, 60, 60), (player_x, player_y), 128, 0)
    fog_of_war.set_colorkey((60, 60, 60))
    screen.blit(fog_of_war, (0, 0))

