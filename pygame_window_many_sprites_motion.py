from multiprocessing.connection import deliver_challenge
import pygame, sys, random
from pygame.locals import *

class Sprite:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y
        self.y_dir = random.randrange(-1,1,1)
        self.x_dir = random.randrange(-1,1,1)
        self.dirchange = random.randrange(25,150, 1)
        
    def move(self, x_bound, y_bound):
        if(self.x > x_bound or self.x < 0):
            self.x_dir = self.x_dir * -1
        if(self.y > y_bound or self.y < 0):
            self.y_dir = self.y_dir * -1
        self.x += self.x_dir
        self.y += self.y_dir

        #uncomment to see how biased python's randrange function is

        #self.dirchange -= 1
        #if(self.dirchange < 0):
        #    self.y_dir = random.randrange(-1,1,1)
        #    self.x_dir = random.randrange(-1,1,1)
        #    self.dirchange = random.randrange(25,150, 1)


image = pygame.image.load("block.png")

FPS = 60

BLACK = (0,0,0)

num_sprites = random.randrange(1,25,1)

fpsClock = pygame.time.Clock()

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Drawing Many Moving Sprites')

sprites = []

while(num_sprites > 0):
        x_pos = random.randrange(1,DISPLAYSURF.get_width(), 1)
        y_pos = random.randrange(1,DISPLAYSURF.get_height(), 1)
        new_sprite = Sprite(image, x_pos, y_pos)
        sprites.append(new_sprite)
        num_sprites = num_sprites - 1

while True: #main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    #draw black background
    DISPLAYSURF.fill(BLACK)

    #draw all sprites
    for sprite in sprites:
        sprite.move(DISPLAYSURF.get_width(), DISPLAYSURF.get_height())
        DISPLAYSURF.blit(sprite.image, (sprite.x, sprite.y))

    pygame.display.update()         
    fpsClock.tick(FPS)