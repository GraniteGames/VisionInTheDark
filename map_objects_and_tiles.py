import pygame

Vector2 = pygame.math.Vector2


class Wall(pygame.sprite.Sprite):
    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)

    def render(self, screen):
        player_image = pygame.image.load('map_tiles/wall_tile.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))


class Floor(pygame.sprite.Sprite):
    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)

    def render(self, screen):
        player_image = pygame.image.load('map_tiles/floor_tile.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))
