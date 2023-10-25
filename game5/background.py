import pygame
from game_parameters import *
import random

my_font = pygame.font.Font('../Assets/brainfish.ttf', 100)
font1 = pygame.font.Font('../Assets/Branda.ttf', 64)
font2 = pygame.font.Font('../Assets/Debrosee.ttf', 64)

def draw_background(screen):
    water = pygame.image.load("../Assets/water.png").convert()
    sand = pygame.image.load("../Assets/sand.png").convert()
    seagrass = pygame.image.load("../Assets/seagrass.png").convert()
    sand.set_colorkey((0, 0, 0))
    seagrass.set_colorkey((0, 0, 0))

    for x in range(0, WIDTH, tile_size):
        for y in range(0, HEIGHT, tile_size):
            screen.blit(water, (x, y))

    for x in range(0, WIDTH, tile_size):
        for y in range(400, HEIGHT, int(tile_size/2)):
            screen.blit(sand, (x, y))

    for _ in range(20):
        x = random.randint(0, WIDTH)
        y = random.randint(400, (HEIGHT - tile_size))
        screen.blit(seagrass, (x, y))

    text = my_font.render('CHOMP', True, (255, 0, 0))
    screen.blit(text, ((WIDTH/2) - (text.get_width()/2), 10))
    text1 = font1.render('CHOMP', True, (220, 50, 50))
    screen.blit(text1, ((WIDTH / 2) - (text1.get_width() / 2), (text.get_height())))
    text2 = font2.render('CHOMP', True, (150, 50, 50))
    screen.blit(text2, ((WIDTH / 2) - (text2.get_width() / 2), (text.get_height() + text1.get_height() - 10)))
