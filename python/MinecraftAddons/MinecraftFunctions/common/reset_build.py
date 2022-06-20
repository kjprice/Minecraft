from ..minecraft_function.minecraft_function import MinecraftFunction
from .fill_air import fill_air
from .build_around_player import build_around_player
RESET_DISTANCE = 50
RESET_MASSIVE_RADIUS = 1 # How many grids of `RESET_DISTANCE` to build around player
def reset_build(x_offset=0, z_offset=0):
    output = []
    output.append('# Filling with Grass')
    output.append(build_around_player(RESET_DISTANCE, x_offset=x_offset, z_offset=z_offset, block='grass'))
    output.append(fill_air(RESET_DISTANCE, x_offset=x_offset, z_offset=z_offset, y_bottom=1))
    output.append('')
    return '\n'.join(output)

def reset_build_massive():
    output = []
    grids_count = RESET_MASSIVE_RADIUS * 2 + 1 # once on either side plus in the center
    offset_distance = RESET_DISTANCE * 2
    offset_start = -RESET_MASSIVE_RADIUS * offset_distance

    total_distance = offset_distance * grids_count
    output.append('# Reseting x={}, z={} area'.format(total_distance, total_distance))
    offsets = []

    for i in range(grids_count):
        offset = offset_start + offset_distance * i
        offsets.append(offset)

    for x in range(grids_count):
        for z in range(grids_count):
            x_offset = offsets[x]
            z_offset = offsets[z]
            output.append('')
            output.append('# Starting grid x={}, z={}'.format(x_offset, z_offset))
            output.append(reset_build(x_offset=x_offset, z_offset=z_offset))
    
    return '\n'.join(output)

class ResetBuild(MinecraftFunction):
    def __init__(self):
        super().__init__('reset_build')
    def build(self):
        return self.run(reset_build())

class ResetBuildMassive(MinecraftFunction):
    def __init__(self):
        super().__init__('reset_build_massive')
    def build(self):
        return self.run(reset_build_massive())
