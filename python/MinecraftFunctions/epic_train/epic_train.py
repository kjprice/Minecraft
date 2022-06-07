from ..minecraft_function.minecraft_function import MinecraftFunction
from ..common.fill_path import fill_path
# from ..common.reset_build import ResetBuild

def create_track_path(y = 0, x_start = 0, x_distance = 0, z_start = 0, z_distance = 0):
    output = []

    output.append(fill_path(y=y, x_start=x_start, x_distance=x_distance, z_start=z_start, z_distance=z_distance, block='redstone_block'))
    output.append(fill_path(y=y + 1, x_start=x_start, x_distance=x_distance, z_start=z_start, z_distance=z_distance, block='golden_rail'))
    return '\n'.join(output)

class EpicTrain(MinecraftFunction):
    def __init__(self):
        super().__init__('epic_train')
    def build(self):
        self.run('# Building epic trains')
        
        self.run('tp @p ~ ~ ~ facing ~5 ~ ~') # Facing east
        self.run('function reset_build')
        self.run('kill @e[type=minecart]')

        self.run('setblock ~-1 ~ ~ stone')
        self.run(create_track_path(x_distance=20))

        self.run('ride @p summon_ride minecart')


