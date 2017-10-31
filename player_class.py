from pygame.locals import *
import pygame

Vector2 = pygame.math.Vector2

class Player(pygame.sprite.Sprite):

    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 8
        self.pos = Vector2(current_pos_x, current_pos_y)


    #def update(self, player_pos_x, player_pos_y ):
    #    self.pos.x = player_pos_x
    #    self.pos.y = player_pos_y


    def render(self, screen):
        player_image = pygame.image.load('spr_player.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))


'''
    def player_movement(self):

        player_speed_vertical = 0
        player_speed_horizontal = 0
        player_speed_increase = 0.5
        player_speed_limit = 5

        pressed_keys = pygame.key.get_pressed()

        # keeps the momentum when keys are let go
        self.pos.x += player_speed_horizontal
        self.pos.y += player_speed_vertical

        # movement up
        if pressed_keys[K_w]:
            self.pos.y += player_speed_vertical
            player_speed_vertical -= player_speed_increase
            # reset to zero
            # sets a maximum speed limit
            if player_speed_vertical <= - player_speed_limit:
                player_speed_vertical = - player_speed_limit
            print player_speed_vertical

            # movement down
        if pressed_keys[K_s]:
            self.pos.y += player_speed_vertical
            player_speed_vertical += player_speed_increase
            if player_speed_vertical >= player_speed_limit:
                player_speed_vertical = player_speed_limit
            print player_speed_vertical

            # movement left
        if pressed_keys[K_a]:
            self.pos.x += player_speed_horizontal
            player_speed_horizontal -= player_speed_increase
            if player_speed_horizontal <= - player_speed_limit:
                player_speed_horizontal = - player_speed_limit
            print player_speed_horizontal

            # movement right
        if pressed_keys[K_d]:
            self.pos.x += player_speed_horizontal
            player_speed_horizontal += player_speed_increase
            if player_speed_horizontal >= player_speed_limit:
                player_speed_horizontal = player_speed_limit
            print player_speed_horizontal
'''


