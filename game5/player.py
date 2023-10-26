import pygame
from game_parameters import *

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('../Assets/orange_fish.png').convert()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.x_speed = 0
        self.y_speed = 0
