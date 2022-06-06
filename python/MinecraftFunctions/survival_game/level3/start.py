from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.reset_build import reset_build

class SurvivalGameLevel3Start(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level3/start')
    def build(self):
        self.run(reset_build())
        self.run('structure load "level3" ~ ~ ~')
        self.run('tp @p ~2 ~11 ~25')
