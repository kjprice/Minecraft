from typing import List

from .....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from ..common.scoreboard import Scoreboard

class FunctionLoopInterface(MinecraftFunction):
    # Override
    def commands_to_run_first(self) -> List[str]:
        raise Exception('This method should be overriden')

    # Override
    def commands_to_iterate(self) -> List[str]:
        raise Exception('This method should be overriden')

    # Override (optional)
    def commands_to_run_end_of_every_loop(self) -> List[str]:
        return []
    
    # Override (optional)
    def commands_to_run_beginning_of_every_loop(self) -> List[str]:
        return []
    
    # Override
    @property
    def scoreboard(self) -> Scoreboard:
        pass

    # Override
    @property
    def delay_in_ticks(self) -> int:
        pass

