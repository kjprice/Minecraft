from ...minecraft_function.minecraft_function import MinecraftFunction
from ...common.reset_build import reset_build
from ...common.tp_to_sealevel import tp_to_sealevel

class SurvivalGameLevel5End(MinecraftFunction):
    def __init__(self):
        super().__init__('survival_game/level5/end')
    def build(self):
        self.run(tp_to_sealevel())
        self.run(reset_build())
        self.run('')

        self.run('title @p title Game Over')