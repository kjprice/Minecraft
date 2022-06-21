from .function_loop.function_loop import FunctionLoop

"""Continuously creates a platform under player"""
class FloatingPlatform(FunctionLoop):
    def __init__(self, data_pack=None) -> None:
        namespace = 'floating_platform'

        super().__init__(data_pack, namespace=namespace)

    def commands_to_run_first(self):

        return []
    
    def commands_to_iterate(self):
        commands = ['execute at @p run fill ~ ~-1 ~ ~ ~-1 ~ stone']

        return commands
    
    def commands_to_run_beginning_of_every_loop(self):

        return [
            'execute at @p run fill ~-1 ~-1 ~-1 ~1 ~-2 ~1 air replace stone',
        ]

