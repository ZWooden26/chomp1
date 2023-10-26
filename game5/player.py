import pygame
from game_parameters import *
from fish import Sean_LR, Sean_UD

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.right_image = pygame.image.load(Sean_LR).convert()
        self.right_image.set_colorkey((0, 0, 0))
        self.left_image = pygame.transform.flip(self.right_image, True, False)
        self.up_image = pygame.image.load(Sean_UD).convert()
        self.up_image.set_colorkey((0, 0, 0))
        self.down_image = pygame.transform.flip(self.up_image, True, False)
        self.image = self.up_image
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0

    def move_up(self):
        self.image = self.up_image
        self.y_speed = -PLAYER_SPEED

    def move_down(self):
        self.image = self.down_image
        self.y_speed = PLAYER_SPEED

    def move_left(self):
        self.image = self.left_image
        self.x_speed = -PLAYER_SPEED

    def move_right(self):
        self.x_speed = PLAYER_SPEED
        self.image = self.right_image

    def stop(self):
        self.x_speed = 0
        self.y_speed = 0

    def update(self):
        self.x += self.x_speed
        self.y += self.y_speed
        self.rect.x = self.x
        self.rect.y = self.y
        if (self.rect.x < -tile_size) or (self.rect.x > WIDTH):
            self.x = WIDTH/2
        if (self.rect.y < -tile_size) or (self.rect.y > 400):
            self.y = 200

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)