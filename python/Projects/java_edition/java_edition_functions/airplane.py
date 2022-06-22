from .function_loop.function_loop import FunctionLoop
# https://minecraft.fandom.com/wiki/Target_selectors#Selecting_targets_by_horizontal_rotation
"""Creates an "airplane" which turns in the direction the player is looking"""
class Airplane(FunctionLoop):
    def __init__(self, data_pack=None) -> None:
        namespace = 'airplane'

        super().__init__(data_pack, namespace=namespace)

    def commands_to_run_first(self):

        return []
    
    def commands_to_iterate(self):
        # TODO: Instead of fill/destroy, create once and tp each time
        # TODO: Maybe create a custom entity like a boat (can ride and move on its own)
        commands = ['execute at @p run fill ~ ~-1 ~ ~ ~-1 ~ stone']

        return commands
    
    def commands_to_run_beginning_of_every_loop(self):
        # TODO: Allow to ascend/descend when looking up/down
        # TODO: Add cannons - shoot tnt
        return [
            'execute at @p run fill ~-1 ~-1 ~-1 ~1 ~-2 ~1 air replace stone',
            'execute at @p[y_rotation=-46..45] run tp @p ~ ~ ~1',
            'execute at @p[y_rotation=46..135] run tp @p ~-1 ~ ~',
            'execute at @p[y_rotation=136..225] run tp @p ~ ~ ~-1',
            'execute at @p[y_rotation=226..-46] run tp @p ~1 ~ ~',
        ]

