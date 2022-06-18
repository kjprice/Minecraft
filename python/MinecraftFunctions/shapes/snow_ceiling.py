from ..minecraft_function.minecraft_function import MinecraftFunction
from ..common.build_around_player import build_around_player
# from ..common.fill_command import fill_command

class SnowCeiling(MinecraftFunction):
    def __init__(self):
        super().__init__('shapes/snow_ceiling')
    def build(self):
        chunk_size = 100
        radius = int(chunk_size / 2)
        
        for z_offset in range(-2000, 2000, 100):
            for x_offset in range(-2000, 2000, 100):
                self.run(build_around_player(radius, y_bottom=50, y_distance=2, z_offset=z_offset, x_offset=x_offset, block='snow'))
