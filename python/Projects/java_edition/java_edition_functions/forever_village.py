from ....MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction

class ForeverVillage(MinecraftFunction):
    def __init__(self, data_pack=None) -> None:
        super().__init__('forever_village', data_pack=data_pack)
    def build(self) -> None:
        self.run('place structure minecraft:village_plains')
        self.run('')
        self.run('setblock ~ ~ ~30 minecraft:command_block{auto:1,Command:"function misc:forever_village"}')
        self.run('setblock ~30 ~ ~ minecraft:command_block{auto:1,Command:"function misc:forever_village"}')
        