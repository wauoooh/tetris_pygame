import pygame, sys, random
from pygame.locals import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((970, 540))

m_image = pygame.image.load("../pic/1062799.png")
m_image = pygame.transform.scale(m_image,(970/2,540/2))
m_rect = m_image.get_rect()
m_rect.move_ip(0,100)

DISPLAYSURF.blit(m_image,m_rect)

m_rect.move_ip(0,100)
DISPLAYSURF.blit(m_image,m_rect)

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    