import pygame
import sys
from game_parameters import *
from background import draw_background

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHOMP IMPROVED")

# --------- Main Loop ------------

running = True
background = screen.copy()
draw_background(background)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("up")
            if event.key == pygame.K_DOWN:
                print("down")

    screen.blit(background, (0, 0))
    pygame.display.flip()


pygame.quit()
sys.exit()
