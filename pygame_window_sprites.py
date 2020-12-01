import pygame, sys
from pygame.locals import *

sprite = pygame.image.load("block.png")

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    DISPLAYSURF.blit(sprite, (0,0))
    DISPLAYSURF.blit(sprite, (100,200))
    DISPLAYSURF.blit(sprite, (150,100))
    DISPLAYSURF.blit(sprite, (250,250))

    pygame.display.update()         