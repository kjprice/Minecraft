from ....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction

SCOREBOARD_NAME = 'dancing_armour_count'
SCOREBOARD_TARGETS = '@a'
SCORBOARD_STARTING_SCORE = 0
SCOREBOARD_SCORE_INCREMENT = 1
DELAY_IN_SECONDS = 0.5
VERBOSE = False

def create_pose(i:int):
    return 'LeftArm:[{}f,0f,0f]'.format(i *20)

def create_armor_stand_data():
    data = []
    for i in range(6):
        pose = create_pose(i)
        # '{NoBasePlate:1b,ShowArms:1b,Pose:{Body:[278f,0f,0f],Head:[317f,0f,0f],LeftArm:[270f,0f,0f],RightArm:[270f,0f,0f]}}',
        base_data = '{NoBasePlate:1b,ShowArms:1b,Pose:{_POSE_}}'.replace('_POSE_', pose)
        data.append(base_data)
    return data


def execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='='):
    # Use "at" instead of "as"...otherwise will execute relative to world spawn point (because of "schedule")
    return f'execute at {selectors}[scores={{{scoreboard_name}{operator}{score_value}}}] run {command}'

def execute_if_score_equals(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=')

def execute_if_score_less_than(selectors, scoreboard_name, score_value, command):
    return execute_if_score_with_operator(selectors, scoreboard_name, score_value, command, operator='=..')

class DancingArmourStandStart(MinecraftFunction):
    def __init__(self, data_pack=None) -> None:
        super().__init__('dancing_armour_stand_start', data_pack=data_pack)
    def build(self):
        self.run('# TODO: Update')
        self.run('scoreboard objectives add {} dummy'.format(SCOREBOARD_NAME))
        self.run('scoreboard players set {} {} {}'.format(SCOREBOARD_TARGETS, SCOREBOARD_NAME, SCORBOARD_STARTING_SCORE))

class DancingArmourStandLoop(MinecraftFunction):
    def __init__(self, data_pack=None) -> None:
        super().__init__('dancing_armour_stand_loop', data_pack=data_pack)
    def build(self):
        armour_stand_data = create_armor_stand_data()
        poses_count = len(armour_stand_data)
        self.run('kill @e[type=minecraft:armor_stand]')
        for i, pose in enumerate(armour_stand_data):
            if VERBOSE:
                self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, i, 'say Running step {}'.format(i+1)))
            cmd = 'summon minecraft:armor_stand ~ ~ ~2 {}'.format(pose)
            self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, i, cmd))
        #     # TODO: Optionally, would be fun to have armour stand face the nearest player
        #     # self.run('summon minecraft:armor_stand ~ ~ ~ {NoBasePlate:1b,ShowArms:1b,Pose:{Body:[278f,0f,0f],Head:[317f,0f,0f],LeftArm:[270f,0f,0f],RightArm:[270f,0f,0f]}}')
            self.run('')
        
        self.run('# Increment score')
        self.run('scoreboard players add {} {} {}'.format(
            SCOREBOARD_TARGETS,
            SCOREBOARD_NAME,
            SCOREBOARD_SCORE_INCREMENT
        ))

        self.run('')
        self.run('# Run again')
        cmd = 'schedule function {} {}s'.format(self.name, DELAY_IN_SECONDS)
        self.run(execute_if_score_less_than('@p', SCOREBOARD_NAME, poses_count, cmd))
        
        if VERBOSE:
            self.run(execute_if_score_equals('@p', SCOREBOARD_NAME, poses_count, 'say All Done!'))
        

class DancingArmourStand(MinecraftFunction):
    start_fn = None
    loop_fn = None
    def __init__(self, data_pack=None) -> None:
        self.start_fn = DancingArmourStandStart(data_pack=data_pack)
        self.loop_fn = DancingArmourStandLoop(data_pack=data_pack)

        self.start_fn.run_all()
        self.loop_fn.run_all()
        super().__init__('dancing_armour_stand', data_pack=data_pack)
    def build(self) -> None:
        self.run_function(self.start_fn)
        self.run_function(self.loop_fn)
