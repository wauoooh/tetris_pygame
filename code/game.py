import pygame, sys
from pygame.locals import *
from const import *
from blockGroup import *

class Game(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.surface = surface
        self.fixedBlockGroup = BlockGroup(BlockGroupType.FIXED, BLOCK_SIZE_W, BLOCK_SIZE_H, [], self.getRelPos())
        self.dropBlockGroup = None
        
    def generateDropBlockGroup(self):
        conf = BlockGroup.GenerateBlockGroupConfig(0,GAME_COL/2+1)
        self.dropBlockGroup = BlockGroup(BlockGroupType.DROP, BLOCK_SIZE_W, BLOCK_SIZE_H, conf, self.getRelPos())
    
    def willCollide(self):
        hash = {}
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx]=1
        dropIndexes = self.dropBlockGroup.getBlockNextIndexes()
        
        for dropIdex in dropIndexes:
            if hash.get(dropIdex):
                return True
            if dropIdex[0] >= GAME_ROW:
                return True
        return False
    
    def update(self):
        # self.fixedBlockGroup.update()
        if self.dropBlockGroup:
            self.dropBlockGroup.update()
        else:
            self.generateDropBlockGroup()
            
        if self.willCollide():
            blocks = self.dropBlockGroup.getBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlocks(blk)
            self.dropBlockGroup.clearBlocks()
            self.dropBlockGroup = None
    
    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
    
    
    
    def getRelPos(self):
        return (240,50)