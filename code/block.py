import pygame, sys
from pygame.locals import *
from const import *


class Block(pygame.sprite.Sprite): 
    def __init__(self, blockType, rowIdx, colIdx, width, height, relPos):
        super().__init__()
        self.blockType = blockType
        self.rowIdx = rowIdx
        self.colIdx = colIdx
        self.width = width
        self.height = height
        self.relPos = relPos
        self.display = True
        self.loadImage()
        self.updateImagePos()
        
    def loadImage(self):
        self.image = pygame.image.load(BLOCK_RES[self.blockType])
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
        
    def updateImagePos(self):
        self.rect = self.image.get_rect()
        self.rect.left = self.relPos[0] + self.width*self.colIdx
        self.rect.top = self.relPos[1] + self.height*self.rowIdx
            
    def draw(self, surface):
        if self.display:
            surface.blit(self.image, self.rect)
        
    # 移动方块，distance = (x,y)，下正上负，右正左负
    def move(self, distance):
        self.rowIdx += distance[0]
        self.colIdx += distance[1]
        self.updateImagePos()
        
    def getIndex(self):
        return (int(self.rowIdx), int(self.colIdx))
