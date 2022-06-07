from ..minecraft_function.minecraft_function import MinecraftFunction
from .build_around_player import build_around_player
def fill_air(x_distance=50, y_bottom=1, y_top=30, x_offset=0, z_offset=0):
    output = []
    output.append('# Filling with air')
    for i in range(y_bottom, y_top):
        output.append(build_around_player(x_distance, i, 1, x_offset=x_offset, z_offset=z_offset, block='air'))
    return '\n'.join(output)


class FillAir(MinecraftFunction):
    def __init__(self):
        super().__init__('fill_air')
    def build(self):
        return self.run(fill_air(x_distance=50, y_top=100))