import pygame, sys
from pygame.locals import *

sprite = pygame.image.load("block.png")



FPS = 60

BLACK = (0,0,0)

fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Keyboard Controls')

#start the character in the middle of the screen
x = DISPLAYSURF.get_width()/2
y = DISPLAYSURF.get_height()/2

#change the speed to see what happens!
speed = 3

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            
    keys = pygame.key.get_pressed()

    if keys[K_w]:
        y-=speed
    if keys[K_s]:
        y+=speed
    if keys[K_a]:
        x-=speed
    if keys[K_d]:
        x+=speed

    DISPLAYSURF.fill(BLACK)
            
    DISPLAYSURF.blit(sprite, (x,y))
    
    pygame.display.update()
    fpsClock.tick(FPS)