from typing import List

from ....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from .common.scoreboard import Scoreboard

DELAY_IN_TICKS = 1
VERBOSE = False

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
    
    # Override
    @property
    def scoreboard(self) -> Scoreboard:
        pass

    # Override
    @property
    def delay_in_ticks(self) -> int:
        pass


def create_pose(i:int):
    left_arm = 'LeftArm:[{}f,0f,0f]'.format(-i * 50)
    right_arm = 'RightArm:[{}f,0f,0f]'.format(i * 50)
    head = 'Head:[0f,{}f,0f]'.format(i * 5)
    poses = ','.join([
        head,
        left_arm,
        right_arm,
    ])
    # TODO(Try to move towards player)
    # - This is an interesting idea: https://gaming.stackexchange.com/questions/339637/how-to-use-coordinate-systems-for-motion-nbt
    # - Use Position, instead of Motion
    # return '{Pose:{_POSES_},Motion:[1d, 0d, 0d]}'.replace('_POSES_', poses)
    return '{Pose:{_POSES_}}'.replace('_POSES_', poses)

def create_armor_stand_data():
    data = []
    for i in range(72):
        pose = create_pose(i)
        data.append(pose)
    return data


def execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='='):
    # Use "at" instead of "as"...otherwise will execute relative to world spawn point (because of "schedule")
    return f'execute at {selectors}[scores={{{scoreboard_name}{operator}{score_value}}}] run {command}'

def execute_if_score_equals(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=')

def execute_if_score_less_than(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=..')

# def set_scoreboard():
#     return 'scoreboard players set {} {} {}'.format(SCOREBOARD_TARGETS, SCOREBOARD_NAME, SCORBOARD_STARTING_SCORE)

class DancingArmourStandStart(MinecraftFunction):
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

        self.start_fn = DancingArmourStandStart(self, start_commands)
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

class DancingArmourStand(FunctionLoop):
    entity_tag_name = None
    def __init__(self, data_pack=None) -> None:
        namespace = 'dancing_armor_stand'
        self.entity_tag_name = 'tag_{}'.format(namespace)

        super().__init__(data_pack, namespace=namespace)

    def commands_to_run_first(self):
        tag_name = self.entity_tag_name
        # {ArmorItems:[{id:diamond_boots,Count:1},{id:diamond_leggings,Count:1},{id:diamond_chestplate,Count:1},{id:diamond_helmet,Count:1}]}

        # NBT_ARMOR_HELMET = '[{},{},{},{id:carved_pumpkin,Count:1}]'
        NBT_ARMOR_HELMET = '[{},{},{},{id:diamond_helmet,Count:1}]'

        # '{NoBasePlate:1b,ShowArms:1b,Pose:{Body:[278f,0f,0f],Head:[317f,0f,0f],LeftArm:[270f,0f,0f],RightArm:[270f,0f,0f]}}',
        BASE_DATA = '{NoBasePlate:1b,ShowArms:1b,ArmorItems:_ARMOR_,Tags:["_TAGS_"]}'.replace('_ARMOR_', NBT_ARMOR_HELMET).replace('_TAGS_', tag_name)

        return [
            'kill @e[tag={}]'.format(tag_name),
            'summon minecraft:armor_stand ~ ~ ~-2 {}'.format(BASE_DATA),
        ]
    
    def commands_to_iterate(self):
        commands = []
        armour_stand_data = create_armor_stand_data()
        for pose in armour_stand_data:
            cmd = 'data merge entity @e[tag={},limit=1] {}'.format(self.entity_tag_name, pose)
            commands.append(cmd)
        return commands
    
    def commands_to_run_end_of_every_loop(self):
        tag_name = self.entity_tag_name

        return [
            '# Always face player',
            'execute at @e[tag={}] run tp @e[tag={}] ~ ~ ~ facing entity @p'.format(tag_name, tag_name),
        ]

