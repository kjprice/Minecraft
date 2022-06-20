from .create_collage import Collage
from ...MinecraftAddons.MinecraftBehaviorPacks.minecraft_behavior_pack import MinecraftBehaviorPack
from ...MinecraftAddons.MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from ...MinecraftAddons.MinecraftResourcePacks.minecraft_resource_pack import MinecraftResourcePack
from ...MinecraftStructures.minecraft_structure import MinecraftCommandBlockStructure

RESOURCE_PACK_UUID = '858eb5be-3590-4be7-a81d-86cb833ecc6d'

class CollageBehaviorPack(MinecraftBehaviorPack):
    def __init__(self) -> None:
        uuids = ['c909500c-2fec-43cf-ae2e-892e7a294b08', RESOURCE_PACK_UUID]
        super().__init__('collage', uuids)

class CollagResourcePack(MinecraftResourcePack):
    def __init__(self) -> None:
        uuids = [RESOURCE_PACK_UUID, 'b2495e1a-05d6-4e1b-8d10-050364668472']
        super().__init__('collage', uuids)

class FamilyCollageFunction(MinecraftFunction):
    behavior_pack = None
    def __init__(self, behavior_pack):
        self.behavior_pack = behavior_pack
        super().__init__('family_collage', behavior_pack)
    def build(self):
        pass

    def create_functions(self, command_blocks: MinecraftCommandBlockStructure):
        x = 0
        for command_block in command_blocks:
            self.run(command_block.get_command_for_function(x=x))
            x += 1

class FamilyCollage():
    x_position = None
    behavior_pack = None
    resource_pack = None

    collage_function = None
    collage_namespaces = None
    def __init__(self) -> None:
        self.x_position = 0
        self.collage_namespaces = []
        self.behavior_pack = CollageBehaviorPack()
        self.resource_pack = CollagResourcePack()

        self.collage_function = FamilyCollageFunction(self.behavior_pack)
        self.collage_function.run('function reset_build')

        self.create_linear_collages()

        command_blocks = self.create_command_blocks_for_functions()
        self.collage_function.create_functions(command_blocks)

        self.collage_function.run_all()
    
    def create_command_blocks_for_functions(self):
        command_blocks = []
        for namespace in self.collage_namespaces:
            structure_name = 'collage_{}'.format(namespace)
            command_fn = 'execute @p ~ ~ ~ function {}'.format(namespace)
            command_block = MinecraftCommandBlockStructure(structure_name,
                command_fn,
                auto_run=True,
                behavior_pack=self.behavior_pack
            )
            command_blocks.append(command_block)

        return command_blocks

    def create_linear_collages(self):
        self.create_linear_collage('01babygabegirafe', 'baby-gabe-girafe.jpg')
        self.create_linear_collage('02gabewithevebaby', 'gabe-eve-baby-portrait.jpg')
        self.create_linear_collage('03evebaby', 'eve-baby-portrait.jpg')
        self.create_linear_collage('04eveberlin', 'Eve-Berlin.jpg')
        self.create_linear_collage('05berlin1', 'Berlin-family.jpg')

    def create_linear_collage(self, namespace: str, img_filepath: str):
        collage = self.create_collage(namespace, img_filepath, self.x_position)
        self.x_position = self.x_position + collage.canvas_dimensions[1]

        return collage


    def create_collage(self, namespace: str, img_filepath: str, starting_x=0):
        collage = Collage(
            self.behavior_pack,
            self.resource_pack,
            namespace,
            img_filepath,
            # resize_ratio=0.05,
            # resize_ratio=0.45,
            resize_block_height=5,
            starting_x=starting_x
        )

        # self.collage_function.create_function(namespace)
        self.collage_namespaces.append(namespace)

        return collage

