import pygame
import sys
import random
from fish import Fish, fishes, green, puffer
from background import draw_background
from game_parameters import *

# initialize
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Adding a player fish")
clock = pygame.time.Clock()

# draw fish on screen
for _ in range(5):
    fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size,400)))

# orange player

# ------- Main Loop -------
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
            if event.key == pygame.K_DOWN:
                print("down")
            if event.key == pygame.K_LEFT:
                print("left")
            if event.key == pygame.K_RIGHT:
                print("right")

    fishes.update()

    for fish in fishes:
        if fish.rect.x < -tile_size:
            fishes.remove(fish)
            fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size, 400)))

    fishes.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()