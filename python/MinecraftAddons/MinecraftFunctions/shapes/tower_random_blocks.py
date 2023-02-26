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
        super().__init__('shapes/tower_random_blocks')
    def build(self):
        blocks_used = []
        width, height, depth = self.dimensions
        np.random.seed(1000)

        for x in range(width):
            for y in range(height):
                for z in range(depth):
                    block = get_random_block()
                    # print(block)
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
            