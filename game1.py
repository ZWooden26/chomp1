import pygame
import random
import sys

MIN_SPEED = 0.5
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

pygame.init()
WIDTH = 800
HEIGHT = 600
tile_size = 64

clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CHOMP IMPROVED")
green = 'Assets/green_fish.png'
puffer = 'Assets/puffer_fish.png'

#loading font
my_font = pygame.font.Font('Assets/brainfish.ttf', 100)
font1 = pygame.font.Font('Assets/Branda.ttf', 64)
font2 = pygame.font.Font('Assets/Debrosee.ttf', 64)

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

    text = my_font.render('CHOMP', True, (255, 0, 0))
    screen.blit(text, ((WIDTH/2) - (text.get_width()/2), 10))
    text1 = font1.render('CHOMP', True, (220, 50, 50))
    screen.blit(text1, ((WIDTH / 2) - (text1.get_width() / 2), (text.get_height())))
    text2 = font2.render('CHOMP', True, (150, 50, 50))
    screen.blit(text2, ((WIDTH / 2) - (text2.get_width() / 2), (text.get_height() + text1.get_height() - 10)))

#def draw_fish(screen):
    #load the fish
    #puffer = pygame.image.load('Assets/puffer_fish.png').convert()
    #puffer.set_colorkey((0, 0, 0))
    #puffer_width = puffer.get_width()
    #puffer_height = puffer.get_height()
    #for _ in range(random.randint(1,5)):
        #x = random.randint(0 + puffer_width, WIDTH - puffer_width)
        #y = random.randint(0 + puffer_height, 400 - puffer_height)
        #screen.blit(puffer, (x, y))

    #green = pygame.image.load('Assets/green_fish.png').convert()
    #green.set_colorkey((0, 0, 0))
    #green_width = green.get_width()
    #green_height = green.get_height()
    #for _ in range(random.randint(1,5)):
        #x = random.randint(0 + green_width, WIDTH - green_width)
        #y = random.randint(0 + green_height, 400 - green_height)
        #flip_green = pygame.transform.flip(green, True, False)
        #screen.blit(flip_green, (x, y))
# ----------MAIN LOOP---------------------
running = True
background = screen.copy()
draw_background(background)
for _ in range(5):
    fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size,400)))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background, (0, 0))
    fishes.update()
    for fish in fishes:
        if fish.rect.x < -tile_size:
            fishes.remove(fish)
            fishes.add(Fish(green, random.randint(WIDTH, WIDTH + tile_size), random.randint(tile_size,400)))
    fishes.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
