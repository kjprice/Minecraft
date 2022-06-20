from ..minecraft_function.minecraft_function import MinecraftFunction
from ..common.replace_all_fill import replace_all_fill

class ReplaceUnwanted(MinecraftFunction):
    def __init__(self):
        super().__init__('clear/replace_unwanted')
    def build(self):
        unwanted_ore = [
            'coal_ore',
            'copper_ore',
            'iron_ore',
            'lapis_ore',
        ]
        unwanted_blocks = [
            'bedrock',
            'stone',
            'grass',
            'dirt',
            'gravel',
            'sand',
            'deepslate',
            'tuff',
            'dripstone_block',
            # Things that hold onto water
            'pointed_dripstone',
            'seagrass',
            'magma',
            # Flowing stuff
            'water',
            'flowing_water',
            'lava',
            'flowing_lava',
            # Trees
            'log',
            'leaves',
            # Stupid ores
            *unwanted_ore,
            *['deepslate_' + ore for ore in unwanted_ore],
        ]
        for block in unwanted_blocks:
            self.run(replace_all_fill(x_distance=50, y_bottom=-125, y_top=60, replace_from=block, replace_to='air'))
