import pygame
import random
import sys

pygame.init()
WIDTH = 800
HEIGHT = 600
tile_size = 64

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHOMP IMPROVED")

#loading font
my_font = pygame.font.Font('Assets/brainfish.ttf', 128)

def draw_background(screen):
    water = pygame.image.load("Assets/water.png").convert()
    sand = pygame.image.load("Assets/sand.png").convert()
    seagrass = pygame.image.load("Assets/seagrass.png").convert()
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

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
