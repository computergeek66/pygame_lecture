import pygame, sys, random
from pygame.locals import *

sprite = pygame.image.load("block.png")

FPS = 5

BLACK = (0,0,0)

max_sprites = random.randrange(1,25,1)

fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Drawing Many Sprites')
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    sprites = []

    DISPLAYSURF.fill(BLACK)

    num_sprites = max_sprites

    while(num_sprites > 0):
        x_pos = random.randrange(1,DISPLAYSURF.get_width(), 1)
        y_pos = random.randrange(1,DISPLAYSURF.get_height(), 1)
        DISPLAYSURF.blit(sprite, (x_pos, y_pos))
        num_sprites = num_sprites - 1

#DISPLAYSURF.blit(sprite, (DISPLAYSURF.get_width()/2,DISPLAYSURF.get_height()/2)) #subtract half the image width and height from the middle screen position to center sprite

    pygame.display.update()         
    fpsClock.tick(FPS)