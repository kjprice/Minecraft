import numpy as np

from ..minecraft_function.minecraft_function import MinecraftFunction
from ..common.build_around_player import build_around_player
# from ..common.fill_command import fill_command
from ..common.build_empty_cube import build_empty_cube_relative_y

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

def set_random_block(x, y, z):
    block = np.random.choice(BLOCK_TYPES)
    return f'setblock ~{x} ~{y} ~{z} {block}'

class TowerRandomBlocks(MinecraftFunction):
    def __init__(self):
        self.dimensions = (8, 6, 8) # X, Y, Z
        super().__init__('shapes/tower_random_blocks')
    def build(self):
        width, height, depth = self.dimensions

        for x in range(width):
            for y in range(height):
                for z in range(depth):
                    self.run(set_random_block(x, y, z))
        