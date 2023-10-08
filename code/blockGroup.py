import random
import pygame, sys
from pygame.locals import *
from const import *
from block import *


class BlockGroup(object):
    def GenerateBlockGroupConfig(rowIdx, colIdx):
        bShape = random.randint(0,len(BLOCK_SHAPE)-1)
        bRotate = random.randint(0,len(BLOCK_SHAPE[bShape])-1)
        bType = random.randint(0,len(BLOCK_RES)-1)
        blockList = []
        for x in range( len(BLOCK_SHAPE[bShape][bRotate]) ):
            config = {
                'blockType' : bType,
                'rowIdx' : rowIdx + BLOCK_SHAPE[bShape][bRotate][x][0],
                'colIdx' : colIdx + BLOCK_SHAPE[bShape][bRotate][x][1]
            }
            blockList.append(config)
        configList = [bShape,bRotate,blockList]
        return configList
    
    def GenerateWallBlockConfig():
        blockList = []
        for x in range(len(WALL_BLOCK_SHAPE[0])):
            config = {
                'blockType' : 0,
                'rowIdx' : WALL_BLOCK_SHAPE[0][x][0],
                'colIdx' : WALL_BLOCK_SHAPE[0][x][1]
            }
            blockList.append(config)
        configList = [0,0,blockList]
        return configList
    
    def __init__(self, blockGroupType, width, height, blockConfigList, relPos):
        super().__init__()
        self.blocks = []
        self.shape = 0
        self.rotated = 0
        self.blockGroupType = blockGroupType
        self.updateTime = 700
        self.time = pygame.time.get_ticks()
        if blockConfigList:
            self.shape = blockConfigList[0]
            self.rotated = blockConfigList[1]
            for config in blockConfigList[2]:
                blk = Block(config['blockType'], config['rowIdx'], config['colIdx'], width, height, relPos)
                self.blocks.append(blk)
     
    # 移动方块，distance = (x,y)，下正上负，右正左负         
    def move(self, distance):
        for b in self.blocks:
            b.move(distance)  
    
    # 转动方块，dir: 0-逆时针，1-顺时针
    def rotate(self,dir):
        nextRotated = self.rotated - (dir*2-1)
        if nextRotated > len(BLOCK_SHAPE[self.shape]) - 1:
            nextRotated = 0
        if nextRotated < 0:
            nextRotated = len(BLOCK_SHAPE[self.shape]) - 1
        for x,b in enumerate(self.blocks):
            b.move((BLOCK_SHAPE[self.shape][nextRotated][x][0]-BLOCK_SHAPE[self.shape][self.rotated][x][0],\
                BLOCK_SHAPE[self.shape][nextRotated][x][1]-BLOCK_SHAPE[self.shape][self.rotated][x][1]))
        self.rotated = nextRotated
                    
    def draw(self, surface):
        for b in self.blocks:
            b.draw(surface)
            
    def update(self):
        if pygame.time.get_ticks() - self.time > self.updateTime:
            self.time = pygame.time.get_ticks()
            self.move((1,0))
      
               
    def getBlockIndexes(self):
        return [block.getIndex()  for block in self.blocks]
    
    def getBlocks(self):
        return self.blocks

    def clearBlocks(self):
        self.blocks = []
    
    def addBlocks(self, blk ):
        self.blocks.append( blk )
        