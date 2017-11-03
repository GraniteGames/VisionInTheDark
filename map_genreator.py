import pygame
import random
import numpy
from map_objects_and_tiles import *
from screen_settings import *

Vector2 = pygame.math.Vector2
map_image = pygame.Surface((screen_width, screen_height))


def generate_a_map():
    pos_x = 0
    pos_y = 0

    map_matrix = numpy.random.randint(3, size=(screen_height / 64, screen_width / 64))
    generate_a_map.player_spawn_pos = (0,0)
    generate_a_map.spawn_walls = (0,0)

    player_spawn = False

    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):

            tile_above = (row_num - 1, tile_num[0])
            tile_left = (row_num, tile_num[0] - 1)
            current_pos = (row_num, tile_num[0])

            # IF statement rules to apply to the map matrix
            if row_num == 0 or row_num == screen_height / 64 - 1 or tile_num[0] == 0 or tile_num[0] == screen_width / 64 -1:
                map_matrix.itemset(current_pos, 1)

            elif random.random() < 0.2 and map_matrix.item(tile_left) == 1:
                map_matrix.itemset(current_pos, 1)

            elif random.random() < 0.6 or (player_spawn == True and tile_num[1] == 2):
                map_matrix.itemset(current_pos, 0)

            elif random.random() < 0.3 and player_spawn == False:
                map_matrix.itemset(current_pos, 2)
                player_spawn = True

    print map_matrix

# Creates the map image from the map matrix
    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):
            wall = Wall((pos_x, pos_y))
            floor = Floor(pos_x, pos_y)
            player_tile = Player_spawn_tile(pos_x, pos_y)
            if tile_num[1] == 1:
                wall.render(map_image)
                generate_a_map.spawn_walls = (pos_x, pos_y)
            elif tile_num[1] == 2:
                player_tile.render(map_image)
                generate_a_map.player_spawn_pos = (pos_x,pos_y)
            elif tile_num[1] == 0:
                floor.render(map_image)

            pos_x += 64
        pos_y += 64
        pos_x = 0


def render_map():
    screen.blit(map_image, (0, 0))
