import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 464
screen_height = 626

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird')

#define game variables
bg_scroll = 0
scroll_speed = 4

#load images
bg = pygame.image.load('img/Flappy_Bird_bg.png')

run = True
while run:

    clock.tick(fps)

    #draw background
    screen.blit(bg, (bg_scroll,-260))
    bg_scroll -= scroll_speed
    if abs(bg_scroll) > 908:
        bg_scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()