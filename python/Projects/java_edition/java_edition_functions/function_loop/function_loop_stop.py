from .....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from .function_loop_interface import FunctionLoopInterface

class FunctionLoopStop(MinecraftFunction):
    cleanup_commands = None
    parent = None
    def __init__(self, parent: FunctionLoopInterface, cleanup_commands = []) -> None:
        self.parent = parent
        self.cleanup_commands = cleanup_commands

        super().__init__('loop_stop', data_pack=parent.data_pack, namespace=parent.namespace)
    def build(self):
        scoreboard = self.parent.scoreboard
        self.run(scoreboard.clear())
        for command in self.cleanup_commands:
            self.run(command)
