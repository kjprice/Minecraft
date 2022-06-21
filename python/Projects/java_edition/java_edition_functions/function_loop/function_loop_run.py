from .....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from .function_loop_interface import FunctionLoopInterface

VERBOSE = False

def execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='='):
    # Use "at" instead of "as"...otherwise will execute relative to world spawn point (because of "schedule")
    return f'execute at {selectors}[scores={{{scoreboard_name}{operator}{score_value}}}] run {command}'

def execute_if_score_equals(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=')

def execute_if_score_less_than(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=..')


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
