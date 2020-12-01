import pygame, sys
from pygame.locals import *

sprite = pygame.image.load("block.png")

x = 0
y = 0

FPS = 30

BLACK = (0,0,0)

fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    DISPLAYSURF.fill(BLACK)
            
    DISPLAYSURF.blit(sprite, (x,y))
    x+=5
    if x > DISPLAYSURF.get_width():
        x = 0
        y += 5
    if y > DISPLAYSURF.get_height():
        y = 0
    
    pygame.display.update()
    fpsClock.tick(FPS)