import pygame, sys, random
from pygame.locals import *
from block import *
from const import *
from blockGroup import *
from game import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))

game = Game(DISPLAYSURF)
    

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    game.update()
        
    DISPLAYSURF.fill((0,0,0))
    
    game.draw()
    
    pygame.display.update()