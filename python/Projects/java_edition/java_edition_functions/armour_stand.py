from ....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction

class ArmourStand(MinecraftFunction):
    def __init__(self, data_pack=None) -> None:
        super().__init__('armour_stand', data_pack=data_pack)
    def build(self) -> None:
        self.run('summon minecraft:armor_stand ~ ~ ~ {NoBasePlate:1b,ShowArms:1b,Pose:{Body:[278f,0f,0f],Head:[317f,0f,0f],LeftArm:[270f,0f,0f],RightArm:[270f,0f,0f]}}')
