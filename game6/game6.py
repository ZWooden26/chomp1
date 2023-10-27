import pygame
import sys
import random
from fish import Fish, fishes, green, Sean_LR, Sean_UD
from background import draw_background
from game_parameters import *
from player import Player

# initialize
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chomp Game")
clock = pygame.time.Clock()

# orange player
player = Player(WIDTH/2, HEIGHT/2)

# score
score_font = pygame.font.Font('../Assets/Branda.ttf', 25)
score = 0

# sounds
oof = pygame.mixer.Sound('../Assets/hurt.wav')

# ------- Main Loop -------
running = True
background = screen.copy()
draw_background(background)

# draw fish on screen
for _ in range(5):
    fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size,400)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # control player fish
        player.stop()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.move_up()
            if event.key == pygame.K_DOWN:
                player.move_down()
            if event.key == pygame.K_LEFT:
                player.move_left()
            if event.key == pygame.K_RIGHT:
                player.move_right()

    screen.blit(background, (0, 0))
    fishes.update()
    player.update()

    # collisions
    result = pygame.sprite.spritecollide(player, fishes, True)
    if result:
        pygame.mixer.Sound.play(oof)
        for x in result:
            score += 1
        for _ in range(len(result)):
            fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size, 400)))

    for fish in fishes:
        if fish.rect.x < -tile_size:
            fishes.remove(fish)
            fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size, 400)))
    fishes.draw(screen)
    player.draw(screen)

    #score_text = score_font.render(f"Score:{score}", True, (255, 0, 0))
    score_text = score_font.render(f"Score: {score}", True, (255, 0, 0))
    screen.blit(score_text, (WIDTH - score_text.get_width() - 5, 10))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()