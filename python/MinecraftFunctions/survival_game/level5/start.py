from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.reset_build import reset_build

class SurvivalGameLevel5Start(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level5/start')
    def build(self):
        self.run(reset_build())
        self.run('structure load "water_dry" ~ ~ ~')
        self.run('tp @p ~32 ~32 ~32')