import pygame
import sys

pygame.init()
WIDTH = 800
HEIGHT = 600
BLUE = (0, 0, 225)
BROWN = (204, 129, 43)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHOMP")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    pygame.draw.rect(screen, BROWN, (0, 500, WIDTH, 100))
    pygame.display.flip()
