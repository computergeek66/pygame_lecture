import pygame, sys
from pygame.locals import *

sprite = pygame.image.load("block.png")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Drawing Sprites')
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    DISPLAYSURF.blit(sprite, (DISPLAYSURF.get_width()/2,DISPLAYSURF.get_height()/2)) #subtract half the image width and height from the middle screen position to center sprite

    pygame.display.update()         