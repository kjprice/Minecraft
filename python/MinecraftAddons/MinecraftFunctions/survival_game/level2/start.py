from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.build_empty_cube import build_empty_cube
from ...common.fill_command import fill_command_from_sea_level

# Pyramid
class SurvivalGameLevel2Start(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level2/start')
    def build(self):
        self.run(fill_command_from_sea_level(y1=10, y2=10, x1=29, x2=31, z1=29, z2=31, block='stone'))
        self.run('structure load "birch_forest" ~ ~ ~')
        self.run(build_empty_cube(0, 0, 0, 50, 20, 50, block='barrier'))
        self.run('tp @p ~30 ~10 ~30')
        # self.run('gamemode s @p')
        self.run(fill_command_from_sea_level(y1=10, y2=10, x1=-1, x2=1, z1=-1, z2=1, block='stone'))
        # self.run('schedule on_area_loaded add ~-30 ~5 ~-30 ~30 ~30 ~30 test1')