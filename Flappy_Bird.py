import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 100

#screen details
screen_width = 464
screen_height = 626
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define game variables
bg_scroll = 0
scroll_speed = 1

#load image
bg = pygame.image.load('img/Flappy_Bird_bg.png')

#bird
class Bird(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        #bird animation
        self.images = []
        self.index = 0
        self.counter = 0
        for num in range(1, 4):
            img = pygame.image.load(f'img/bird{num}.png')
            self.images.append(img)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]

    def update(self):
        #animation counter
        self.counter += 1
        flap_cooldown = 5
        if self.counter > flap_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
        self.image = self.images[self.index]

#bird position
bird_group = pygame.sprite.Group()
flappy = Bird(100, int(screen_height / 2))
bird_group.add(flappy)


#while running
run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (bg_scroll,-260))

    bird_group.draw(screen)
    bird_group.update()

    bg_scroll -= scroll_speed
    if abs(bg_scroll) > 908:
        bg_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()