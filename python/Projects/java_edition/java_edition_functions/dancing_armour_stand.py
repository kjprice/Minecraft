from ....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction

SCOREBOARD_NAME = 'dancing_armour_count'
SCOREBOARD_TARGETS = '@a'
SCORBOARD_STARTING_SCORE = 0
SCOREBOARD_SCORE_INCREMENT = 1
DELAY_IN_TICKS = 1
VERBOSE = False
TAG_NAME = 'dancing_armour'

# {ArmorItems:[{id:diamond_boots,Count:1},{id:diamond_leggings,Count:1},{id:diamond_chestplate,Count:1},{id:diamond_helmet,Count:1}]}
# NBT_ARMOR_HELMET = '[{},{},{},{id:carved_pumpkin,Count:1}]'
NBT_ARMOR_HELMET = '[{},{},{},{id:diamond_helmet,Count:1}]'

# '{NoBasePlate:1b,ShowArms:1b,Pose:{Body:[278f,0f,0f],Head:[317f,0f,0f],LeftArm:[270f,0f,0f],RightArm:[270f,0f,0f]}}',
BASE_DATA = '{NoBasePlate:1b,ShowArms:1b,ArmorItems:_ARMOR_,Tags:["_TAGS_"]}'.replace('_ARMOR_', NBT_ARMOR_HELMET).replace('_TAGS_', TAG_NAME)

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

def set_scoreboard():
    return 'scoreboard players set {} {} {}'.format(SCOREBOARD_TARGETS, SCOREBOARD_NAME, SCORBOARD_STARTING_SCORE)

class DancingArmourStandStart(MinecraftFunction):
    def __init__(self, data_pack, namespace) -> None:
        super().__init__('loop_run_before', data_pack=data_pack, namespace=namespace)
    def build(self):
        self.run('kill @e[tag={}]'.format(TAG_NAME))
        self.run('summon minecraft:armor_stand ~ ~ ~-2 {}'.format(BASE_DATA))

class DancingArmourStandAlwaysFacePlayer(MinecraftFunction):
    def __init__(self, data_pack, namespace) -> None:
        super().__init__('loop_dancing_armour_stand_face_player', data_pack=data_pack, namespace=namespace)
    def build(self):
        self.run('# Always face player')
        self.run('execute at @e[tag={}] run tp @e[tag={}] ~ ~ ~ facing entity @p'.format(TAG_NAME, TAG_NAME))
        self.run('schedule function {} 1t'.format(self.name))


class FunctionLoopRun(MinecraftFunction):
    def __init__(self, data_pack, namespace) -> None:
        super().__init__('loop_run', data_pack=data_pack, namespace=namespace)
    def build(self):
        armour_stand_data = create_armor_stand_data()
        poses_count = len(armour_stand_data)
        for i, pose in enumerate(armour_stand_data):
            if VERBOSE:
                self.run('')
                self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, i, 'say Running step {}'.format(i+1)))
            cmd = 'data merge entity @e[tag={},limit=1] {}'.format(TAG_NAME, pose)
            self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, i, cmd))

        self.run('')
        
        self.run('')
        self.run('# Increment score')
        self.run('scoreboard players add {} {} {}'.format(
            SCOREBOARD_TARGETS,
            SCOREBOARD_NAME,
            SCOREBOARD_SCORE_INCREMENT
        ))

        self.run('')
        self.run('# Run again')
        cmd = 'schedule function {} {}t'.format(self.name, DELAY_IN_TICKS)
        self.run(execute_if_score_less_than('@p', SCOREBOARD_NAME, poses_count, cmd))
        
        self.run('')
        self.run('# Start over when finished')
        self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, poses_count, set_scoreboard()))
        
        if VERBOSE:
            self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, poses_count, 'say All Done!'))

class FunctionLoopStart(MinecraftFunction):
    start_fn = None
    loop_fn = None
    def __init__(self, data_pack, namespace:str) -> None:
        self.start_fn = DancingArmourStandStart(data_pack=data_pack, namespace=namespace)
        self.loop_fn = FunctionLoopRun(data_pack=data_pack, namespace=namespace)
        self.face_player_fn = DancingArmourStandAlwaysFacePlayer(data_pack=data_pack, namespace=namespace)

        self.start_fn.run_all()
        self.loop_fn.run_all()
        self.face_player_fn.run_all()
        super().__init__('go', data_pack=data_pack, namespace=namespace)
    def build(self) -> None:
        self.run('scoreboard objectives add {} dummy'.format(SCOREBOARD_NAME))
        self.run(set_scoreboard())
        self.run('')
        self.run_function(self.start_fn)
        self.run_function(self.loop_fn)
        self.run_function(self.face_player_fn)
    
    # Override
    def commands_to_iterate(self):
        raise Exception('This method should be overriden')

class DancingArmourStand(FunctionLoopStart):
    def __init__(self, data_pack=None) -> None:
        super().__init__(data_pack, namespace='dancing_armor_stand')