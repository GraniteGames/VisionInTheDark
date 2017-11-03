import pygame

Vector2 = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    speed_limit = 5
    milliseconds = 100

    def __init__(self, (current_pos_x, current_pos_y)):
        pygame.sprite.Sprite.__init__(self)

        self.speed_h = 0
        self.speed_v = 0
        self.increase = 0.5
        self.pos = Vector2(current_pos_x, current_pos_y)

        self.time_elapsed_since_last_action_up = 0
        self.time_elapsed_since_last_action_down = 0
        self.time_elapsed_since_last_action_left = 0
        self.time_elapsed_since_last_action_right = 0

        self.clock_up = pygame.time.Clock()
        self.clock_down = pygame.time.Clock()
        self.clock_left = pygame.time.Clock()
        self.clock_right = pygame.time.Clock()

        self.dt_up = self.clock_up.tick()
        self.dt_down = self.clock_down.tick()
        self.dt_left = self.clock_left.tick()
        self.dt_right = self.clock_right.tick()

        self.time_elapsed_since_last_action_up += self.dt_up
        self.time_elapsed_since_last_action_down += self.dt_down
        self.time_elapsed_since_last_action_left += self.dt_left
        self.time_elapsed_since_last_action_right += self.dt_right


    def render(self, screen):
        player_image = pygame.image.load('spr_player.png').convert_alpha()
        screen.blit(player_image, (self.pos.x, self.pos.y))
        self.player_image = pygame.Surface([64, 64])
        self.rect = self.player_image.get_rect()
        self.rect.center = (self.pos.x + 32, self.pos.y + 32)