# from ..common.fill_command import fill_command
from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.fill_command import fill_command_from_sea_level
from ...common.build_around_player import build_around_player
from ...common.reset_build import reset_build
from ...common.build_tnt_trap import build_tnt_trap
from ...common.tp_to_sealevel import tp_to_sealevel

# Pyramid
class SurvivalGameLevel1Start(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level1/start')
    def build(self):
        wall_distance = 15
        barrier_distance = wall_distance - 1
        ceiling_height = 10
        barrier_height = ceiling_height - 2

        self.run(tp_to_sealevel())
        self.run(reset_build())
        self.run('')

        self.run('spawnpoint @p')

        self.run('title @p title Survival Game')

        self.run(build_around_player(wall_distance, y_distance=ceiling_height, block='lava', other_args=['0 hollow']))
        self.run(build_around_player(wall_distance, y_bottom=barrier_height, y_distance=0, block="barrier"))

        player_position = [0, 5, 0]
        x, y, z = player_position

        self.run(fill_command_from_sea_level(y1=y-1, y2=y-1, x2=3, block='stone'))
        self.run(build_tnt_trap(x1=3, x2=6, y1=y-1, y2=y-1))
        self.run(fill_command_from_sea_level(x1=7, y1=y-1, y2=y-1, x2=9, block='stone'))
        self.run(fill_command_from_sea_level(x1=9, y1=y-1, y2=y-1, x2=9, z2=3, block='stone'))

        # Command Blocks stored in structure blocks:
        # - "game_commands": All command blocks
        # - "level1_end": Command block to end level1
        #   - "Command": execute @[r=2] ~ ~ ~ function survival_game/level1/end

        self.run('# Command block to detect player')
        self.run('tp @p ~ ~5 ~ facing ~5 ~ ~') # Facing east
        # self.run('schedule on_area_loaded add ~-30 ~5 ~-30 ~30 ~30 ~30 test1')
    