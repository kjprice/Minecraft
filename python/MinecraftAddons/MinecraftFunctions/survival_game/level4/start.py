from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.reset_build import reset_build
from ...common.tp_to_sealevel import tp_to_sealevel

class SurvivalGameLevel4Start(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level4/start')
    def build(self):
        self.run(reset_build())
        self.run(tp_to_sealevel())
        self.run('kill @e[type=spider]')
        self.run('give @p wooden_sword')
        self.run('structure load "level4" ~-58 ~-1 ~-4')


