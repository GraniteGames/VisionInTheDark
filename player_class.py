import pygame

Vector2 = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    speed = 3
    mass = 2
    max_speed = 8

    def __init__(self, current_pos_x, current_pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.pos = Vector2(current_pos_x, current_pos_y)
        self.vel = Player.speed * self.mass
        self.momentum = self.mass * self.vel

    def render(self, screen):
        player_image = pygame.image.load('spr_player.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))