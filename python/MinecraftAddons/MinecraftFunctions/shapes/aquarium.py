from ..minecraft_function.minecraft_function import MinecraftFunction
from ..common.build_around_player import build_around_player
# from ..common.fill_command import fill_command
from ..common.build_empty_cube import build_empty_cube_relative_y

class Aquarium(MinecraftFunction):
    def __init__(self):
        # TODO: Rename
        super().__init__('shapes/aquarium')
    def build(self):
        chunk_size = 100
        radius = int(chunk_size / 2)
        # print('kj')
        height = 5
        width = 3
        depth = 4
        # height = 17
        # width = 11
        # depth = 7

        # self.run(build_around_player(radius, y_bottom=50, y_distance=2, z_offset=z_offset, x_offset=x_offset, block='snow'))
        self.run(build_empty_cube_relative_y(x1=0, y1=0, z1=0, x2=7, y2=-height, z2=width, block='stone'))
        
        # for z_offset in range(-2000, 2000, 100):
        #     for x_offset in range(-2000, 2000, 100):
        #         self.run(build_around_player(radius, y_bottom=50, y_distance=2, z_offset=z_offset, x_offset=x_offset, block='snow'))
