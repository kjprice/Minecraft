from collections import Counter

import numpy as np
import pandas as pd

from ..minecraft_function.minecraft_function import MinecraftFunction

PRINT_STATS = False

BLOCK_TYPES = [
    'wood 0', # Oak Wood
    'wood 0', # Oak Wood
    'wood 5', # Dark Oak Wood
    'wood 5', # Dark Oak Wood
    'wood 5', # Dark Oak Wood
    'wood 1', # Spruce Wood
    'wood 1', # Spruce Wood
    'wood 1', # Spruce Wood
    'log 1', # Srpuce Log
]

def get_random_block():
    return np.random.choice(BLOCK_TYPES)

def set_random_block(x, y, z, block):
    return f'setblock ~{x} ~{y} ~{z} {block}'

class TowerRandomBlocks(MinecraftFunction):
    def __init__(self):
        self.dimensions = (8, 6, 8) # X, Y, Z
        self.is_hollow = True
        super().__init__('shapes/tower_random_blocks')
    def get_x_range(self, width: int):
        if self.is_hollow:
            return [0, width-1]

        return range(width)

    @property
    def width(self):
        return self.dimensions[0]
    @property
    def height(self):
        return self.dimensions[1]
    @property
    def depth(self):
        return self.dimensions[2]

    def should_place_block(self, x: int, z: int) -> bool:
        if not self.is_hollow:
            return True

        if x == 0 or x == self.width - 1:
            return True
        if z == 0 or z == self.depth - 1:
            return True
        
        return False

    def build(self):
        blocks_used = []
        width, height, depth = self.dimensions
        np.random.seed(1000)

        for x in range(width):
            for y in range(height):
                for z in range(depth):
                    if self.should_place_block(x, z):
                        block = get_random_block()
                        self.run(set_random_block(x, y, z, block))
                        blocks_used.append(block)
        
        if PRINT_STATS:
            counter = Counter(blocks_used)
            blocks = []
            counts = []
            for block in counter:
                blocks.append(block)
                counts.append(counter[block])

            df = pd.DataFrame({'block': blocks, 'counts': counts})
            df.to_csv('test.csv')
            df.index = blocks
            fig = df.sort_values('counts').plot(kind='bar',  
                    figsize=(20, 16), fontsize=26).get_figure()

            fig.savefig('test.pdf')
            