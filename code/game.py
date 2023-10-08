import pygame, sys
from pygame.locals import *
from const import *
from blockGroup import *

class Game(pygame.sprite.Sprite):
    def __init__(self, surface):
        self.surface = surface
        self.pressTime = [pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks(),pygame.time.get_ticks()]
        self.pressFlag = [0,0,0,0]  # 依次为上下左右
        conf = BlockGroup.GenerateWallBlockConfig()
        self.wallBlockGroup = BlockGroup(BlockGroupType.WALL, BLOCK_SIZE_W, BLOCK_SIZE_H, conf, self.getRelPos())
        self.fixedBlockGroup = BlockGroup(BlockGroupType.FIXED, BLOCK_SIZE_W, BLOCK_SIZE_H, [], self.getRelPos())
        self.dropBlockGroup = None
        
    def generateDropBlockGroup(self):
        conf = BlockGroup.GenerateBlockGroupConfig(0,GAME_COL/2+1)
        self.dropBlockGroup = BlockGroup(BlockGroupType.DROP, BLOCK_SIZE_W, BLOCK_SIZE_H, conf, self.getRelPos())
    
    def checkKeyPress(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_UP]:
            if pygame.time.get_ticks() - self.pressTime[0] > MIN_PRESS_TIME:
                self.pressFlag[0] = 1
                self.pressTime[0] = pygame.time.get_ticks()
        if pressed[K_DOWN]:
            self.pressFlag[1] = 1
            self.pressTime[1] = pygame.time.get_ticks()
        else:
            self.pressFlag[1] = 0
        if pressed[K_LEFT]:
            if pygame.time.get_ticks() - self.pressTime[2] > MIN_PRESS_TIME:
                self.pressFlag[2] = 1
                self.pressTime[2] = pygame.time.get_ticks()
        if pressed[K_RIGHT]:
            if pygame.time.get_ticks() - self.pressTime[3] > MIN_PRESS_TIME:
                self.pressFlag[3] = 1
                self.pressTime[3] = pygame.time.get_ticks()
    
    def checkCollide(self):
        dropIndexes = self.dropBlockGroup.getBlockIndexes()
        hash = {}
        allIndexes = self.fixedBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx]=1
        for dropIdex in dropIndexes:
            if hash.get(dropIdex):
                return True
            if dropIdex[0] >= GAME_ROW:
                return True
        hash = {}
        allIndexes = self.wallBlockGroup.getBlockIndexes()
        for idx in allIndexes:
            hash[idx]=1
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
            
        if self.checkCollide():
            self.dropBlockGroup.move((-1,0))
            blocks = self.dropBlockGroup.getBlocks()
            for blk in blocks:
                self.fixedBlockGroup.addBlocks(blk)
            self.dropBlockGroup.clearBlocks()
            self.dropBlockGroup = None
        
        if self.dropBlockGroup:
            if self.pressFlag[1]:
                self.dropBlockGroup.updateTime = 100
            else:
                self.dropBlockGroup.updateTime = 700
            if self.pressFlag[2]+self.pressFlag[3]:
                self.dropBlockGroup.move((0,self.pressFlag[3]-self.pressFlag[2]))
                if self.checkCollide():
                    self.dropBlockGroup.move((0,self.pressFlag[2]-self.pressFlag[3]))
                self.pressFlag[2] = 0
                self.pressFlag[3] = 0
    
    def draw(self):
        self.fixedBlockGroup.draw(self.surface)
        self.wallBlockGroup.draw(self.surface)
        if self.dropBlockGroup:
            self.dropBlockGroup.draw(self.surface)
    

        
    
    
    
    
    def getRelPos(self):
        return (240,50)