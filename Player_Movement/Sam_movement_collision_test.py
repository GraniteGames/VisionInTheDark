import pygame
from pygame.locals import *

# initiate pygame
pygame.init()

# limiting the FPS with this fps clock
FPS = 60
fpsClock = pygame.time.Clock()

Vector2 = pygame.math.Vector2

# create display
screen_width = 64 * 15
screen_height = 64 * 10
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Collision Detection Testing")


# Player class
class Player(pygame.sprite.Sprite):
    width = 64
    height = 64
    speed = 8
    pos = Vector2(screen_width / 2 - 32, screen_height / 2 - 32)
    player_col = pygame.Rect(pos.x - 4, pos.y - 4, 68, 68)
    image = pygame.image.load('spr_player2.png').convert_alpha()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([Player.width, Player.height])
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.center = (Player.pos.x + 32, Player.pos.y + 32)


# Wall class
class Wall(pygame.sprite.Sprite):
    pos = Vector2(128, 128)
    col = pygame.Rect(pos.x - 4, pos.y - 4, 68, 68)
    image = pygame.image.load('wall_tile.png').convert_alpha()

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([64, 64])
        self.rect = self.image.get_rect()
        self.rect.center = (Wall.pos.x + 32, Wall.pos.y + 32)


def player_controller():
    # variable for key press
    pressed_keys = pygame.key.get_pressed()

    # horizontal movement
    if pressed_keys[K_a]:
        Player.pos.x -= Player.speed
        if pygame.sprite.collide_rect(player, wall):
            Player.pos.x += Player.speed
    if pressed_keys[K_d]:
        Player.pos.x += Player.speed
        #if pygame.sprite.collide_rect(player, wall):
        #    Player.pos.x -= Player.speed

    # vertical movement
    if pressed_keys[K_w]:
        Player.pos.y -= Player.speed
    if pressed_keys[K_s]:
        Player.pos.y += Player.speed


# game while loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

    player = Player()
    wall = Wall()

    player.update()
    player_controller()

    if pygame.sprite.collide_rect(player, wall):
        print "collided!"

    # horizontal boundaries
    if Player.pos.x > screen_width - Player.width:
        Player.pos.x = screen_width - Player.width
    elif Player.pos.x < 0:
        Player.pos.x = 0
    # vertical boundaries
    if Player.pos.y > screen_height - Player.height:
        Player.pos.y = screen_height - Player.height
    elif Player.pos.y < 0:
        Player.pos.y = 0

    # window creation and player blitting
    screen.fill((135, 135, 135))
    screen.blit(Player.image, Player.pos)
    screen.blit(Wall.image, (Wall.pos.x, Wall.pos.y))

    pygame.display.update()
    fpsClock.tick(FPS)
