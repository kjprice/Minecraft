from ..minecraft_function.minecraft_function import MinecraftFunction
from .epic_train import EpicTrain

class RollerCoaster(MinecraftFunction):
    train = None
    def __init__(self):
        super().__init__('roller_coaster')
        self.train = EpicTrain()
    def build(self):
        self.train.build()
        self.run('\n'.join(self.train.output))
        # self.run('function ')
