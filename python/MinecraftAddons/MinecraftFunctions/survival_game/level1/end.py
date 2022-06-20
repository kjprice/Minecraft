# from ..common.fill_command import fill_command
from ...minecraft_function.minecraft_function import MinecraftFunction
from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.reset_build import reset_build
from ...common.tp_to_sealevel import tp_to_sealevel
# Pyramid
class SurvivalGameLevel1End(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level1/end')
    def build(self):
        self.run(tp_to_sealevel())
        self.run(reset_build())
        self.run('')

        self.run('title @p title Game Over')

        self.run('function survival_game/level2/start')

