import pygame
import random
from game_parameters import *

pygame.init()
green = '../Assets/green_fish.png'
Sean = '../Assets/SEAN.png'

MIN_SPEED = 1
MAX_SPEED = 3
class Fish(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        super().__init__()
        self.image = pygame.image.load(name).convert()
        self.image.set_colorkey((0, 0, 0))
        self.image = pygame.transform.flip(self.image, True, False)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.speed = random.uniform(MIN_SPEED, MAX_SPEED)
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect.x = self.x

    def draw(self, screen):
        screen.blit(self.image, self.rect.center)

fishes = pygame.sprite.Group()