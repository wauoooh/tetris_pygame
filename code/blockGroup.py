import random
import pygame, sys
from pygame.locals import *
from const import *
from block import *


class BlockGroup(object):
    def GenerateBlockGroupConfig(rowIdx, colIdx):
        bShape = random.randint(0,len(BLOCK_SHAPE)-1)
        bType = random.randint(0,len(BLOCK_RES)-1)
        configList = []
        for x in range( len(BLOCK_SHAPE[bShape]) ):
            config = {
                'blockType' : bType,
                'rowIdx' : rowIdx + BLOCK_SHAPE[bShape][x][0],
                'colIdx' : colIdx + BLOCK_SHAPE[bShape][x][1]
            }
            configList.append(config)
        return configList
    
    def __init__(self, blockGroupType, width, height, blockConfigList, relPos):
        super().__init__()
        self.blocks = []
        self.blockGroupType = blockGroupType
        self.time = pygame.time.get_ticks()
        for config in blockConfigList:
            blk = Block(config['blockType'], config['rowIdx'], config['colIdx'], width, height, relPos)
            self.blocks.append(blk)
            
    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)
            
    def update(self):
        if pygame.time.get_ticks() - self.time > 100:
            self.time = pygame.time.get_ticks()
            for b in self.blocks:
                b.drop()
      
               
    def getBlockIndexes(self):
        return [block.getIndex()  for block in self.blocks]
    
    def getBlockNextIndexes(self):
        return [block.getNextIndex()  for block in self.blocks]
    
    def getBlocks(self):
        return self.blocks

    def clearBlocks(self):
        self.blocks = []
    
    def addBlocks(self, blk ):
        self.blocks.append( blk )
        
    def isOnLeftEdge(self):
        for b in self.blocks:
            if b.colIdx == 0:
                return True
        return False
    
    def isOnRightEdge(self):
        for b in self.blocks:
            if b.colIdx == GAME_COL-1:
                return True
        return False