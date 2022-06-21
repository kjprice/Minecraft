from .function_loop.function_loop import FunctionLoop

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

