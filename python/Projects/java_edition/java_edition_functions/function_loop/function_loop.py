from .....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from ..common.scoreboard import Scoreboard
from .function_loop_interface import FunctionLoopInterface

DELAY_IN_TICKS = 1
VERBOSE = False

def execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='='):
    # Use "at" instead of "as"...otherwise will execute relative to world spawn point (because of "schedule")
    return f'execute at {selectors}[scores={{{scoreboard_name}{operator}{score_value}}}] run {command}'

def execute_if_score_equals(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=')

def execute_if_score_less_than(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=..')


class FunctionLoopStart(MinecraftFunction):
    commands = None
    def __init__(self, parent: FunctionLoopInterface, commands) -> None:
        self.commands = commands

        super().__init__('loop_run_before', data_pack=parent.data_pack, namespace=parent.namespace)
    def build(self):
        for command in self.commands:
            self.run(command)

class FunctionLoopRun(MinecraftFunction):
    loop_commands = None
    each_loop_commands = None
    parent = None
    def __init__(self, parent:FunctionLoopInterface, commands, each_loop_commands) -> None:
        self.loop_commands = commands
        self.each_loop_commands = each_loop_commands
        self.parent = parent
        super().__init__('loop_run', data_pack=parent.data_pack, namespace=parent.namespace)
    def build(self):
        scoreboard = self.parent.scoreboard
        delay_in_ticks = self.parent.delay_in_ticks
        commands_count = len(self.loop_commands)
        for i, command in enumerate(self.loop_commands):
            if VERBOSE:
                self.run('')
                self.run(execute_if_score_equals('@p', scoreboard.name, i, 'say Running step {}'.format(i+1)))
            self.run(execute_if_score_equals('@p', scoreboard.name, i, command))

        self.run('')
        
        self.run('')
        self.run('# Increment score')
        self.run('scoreboard players add {} {} {}'.format(
            scoreboard.targets,
            scoreboard.name,
            scoreboard.increment_by
        ))

        self.run('')
        self.run('# Run again')
        cmd = 'schedule function {} {}t'.format(self.name, delay_in_ticks)
        self.run(execute_if_score_less_than('@p', scoreboard.name, commands_count, cmd))
        
        self.run('')
        self.run('# Start over when finished')
        self.run(execute_if_score_equals('@p', scoreboard.name, commands_count, scoreboard.initialize_players()))

        self.run('')
        self.run('# Run after each loop')
        self.run('\n'.join(self.each_loop_commands))
        
        if VERBOSE:
            self.run(execute_if_score_equals('@p', scoreboard.name, commands_count, 'say All Done!'))

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
