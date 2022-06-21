from .....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from .function_loop_interface import FunctionLoopInterface

class FunctionLoopStart(MinecraftFunction):
    commands = None
    def __init__(self, parent: FunctionLoopInterface, commands) -> None:
        self.commands = commands

        super().__init__('loop_run_before', data_pack=parent.data_pack, namespace=parent.namespace)
    def build(self):
        for command in self.commands:
            self.run(command)
