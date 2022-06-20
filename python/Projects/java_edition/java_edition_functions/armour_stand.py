from ....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction

class ArmourStand(MinecraftFunction):
    def __init__(self, data_pack=None) -> None:
        super().__init__('armour_stand', data_pack=data_pack)
    def build(self) -> None:
        tag_name = 'test_armor_stand'
        self.run('kill @e[type=minecraft:armor_stand]')
        self.run(f'summon minecraft:armor_stand ~-2 ~ ~-2 {{NoBasePlate:1b,ShowArms:1b,Tags:["{tag_name}"]}}')
        self.run(f'data get entity @e[tag={tag_name},limit=1]')
