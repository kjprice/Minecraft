from .....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from ..common.scoreboard import Scoreboard
from .function_loop_interface import FunctionLoopInterface
from .function_loop_start import FunctionLoopStart
from .function_loop_run import FunctionLoopRun

DELAY_IN_TICKS = 1

class FunctionLoop(FunctionLoopInterface):
    start_fn = None
    loop_fn = None
    _scoreboard = None
    _delay_in_ticks = None
    def __init__(self, data_pack, namespace:str, delay_in_ticks = DELAY_IN_TICKS) -> None:
        self._scoreboard = Scoreboard(name=f'{namespace}_count')
        self._delay_in_ticks = delay_in_ticks

        super().__init__('go', data_pack=data_pack, namespace=namespace)

    def run_dependent_functions(self):
        start_commands = self.commands_to_run_first()
        loop_commands = self.commands_to_iterate()
        each_loop_commands = self.commands_to_run_end_of_every_loop()

        self.start_fn = FunctionLoopStart(self, start_commands)
        self.loop_fn = FunctionLoopRun(self, loop_commands, each_loop_commands)

        self.start_fn.run_all()
        self.loop_fn.run_all()

    def build(self) -> None:
        self.run_dependent_functions()

        self.run('scoreboard objectives add {} dummy'.format(self.scoreboard.name))
        self.run(self.scoreboard.initialize_players())
        self.run('')
        self.run_function(self.start_fn)
        self.run_function(self.loop_fn)
    
    @property
    def scoreboard(self) -> Scoreboard:
        return self._scoreboard
    
    @property
    def delay_in_ticks(self) -> int:
        return self._delay_in_ticks
