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

    map_matrix = numpy.random.randint(2, size=(screen_height / 64, screen_width / 64))

    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):

            tile_above = (row_num - 1, tile_num[0])
            tile_left = (row_num, tile_num[0] - 1)
            current_pos = (row_num, tile_num[0])

            # IF statement rules to apply to the map matrix
            if row_num == 0 or row_num == screen_height / 64 - 1 or tile_num[0] == 0 or tile_num[0] == screen_width / 64 -1:
                map_matrix.itemset(current_pos, 1)

            elif random.random() < 0.8:
                map_matrix.itemset(current_pos, 0)

    print map_matrix

    for row_num, row_list in enumerate(map_matrix):
        for tile_num in enumerate(row_list):
            wall = Wall(pos_x, pos_y)
            floor = Floor(pos_x, pos_y)
            if tile_num[1] == 1:
                wall.render(map_image)
            else:
                floor.render(map_image)

            pos_x += 64
        pos_y += 64
        pos_x = 0


def render_map():
    screen.blit(map_image, (0, 0))
