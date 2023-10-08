class BlockType:
    RED = 0
    ORANGE = 1
    YELLOW = 2
    GREEN = 3
    CYAN = 4
    BLUE = 5
    PURPLE = 6
    BLOCKMAx = 7
 
class BlockGroupType:
    FIXED = 0
    DROP = 1
    WALL = 2
    
BLOCK_RES = {
    BlockType.RED : "pic/red.png",
    BlockType.ORANGE : "pic/orange.png",
    BlockType.YELLOW : "pic/yellow.png",
    BlockType.GREEN : "pic/green.png",
    BlockType.CYAN : "pic/cyan.png",
    BlockType.BLUE : "pic/blue.png",
    BlockType.PURPLE : "pic/purple.png",
}

BLOCK_SIZE_W = 32
BLOCK_SIZE_H = 32
GAME_ROW = 17
GAME_COL = 10

MIN_PRESS_TIME = 100    # 按键按压超过此时间记为有效(ms)
FLICKER_CYCLE = 100

BLOCK_SHAPE = [
    [[(0,0),(0,1),(1,0),(1,1)]],  # 方形
    [[(0,0),(0,1),(0,2),(0,3)],[(0,0),(1,0),(2,0),(3,0)]],  # 长条形
    [[(0,0),(0,1),(1,1),(1,2)],[(0,1),(1,1),(1,0),(2,0)]],  # z字形
    [[(0,1),(1,0),(1,1),(1,2)],[(0,1),(1,1),(2,1),(1,0)],\
        [(0,0),(0,1),(0,2),(1,1)],[(0,1),(1,1),(2,1),(1,2)]],  # 飞机形
]

WALL_BLOCK_SHAPE = [
    [(0, -1), (1, -1), (2, -1), (3, -1), (4, -1), (5, -1), (6, -1), \
        (7, -1), (8, -1), (9, -1), (10, -1), (11, -1), (12, -1), (13, -1),\
            (14, -1), (15, -1), (16, -1), (0, 10), (1, 10), (2, 10), (3, 10), \
                (4, 10), (5, 10), (6, 10), (7, 10), (8, 10), (9, 10), (10, 10),\
                    (11, 10), (12, 10), (13, 10), (14, 10), (15, 10), (16, 10), \
                        (17, -1), (17, 0), (17, 1), (17, 2), (17, 3), (17, 4), (17, 5),\
                            (17, 6), (17, 7), (17, 8), (17, 9), (17, 10)]
]