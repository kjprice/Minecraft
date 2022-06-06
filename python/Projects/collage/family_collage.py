from .create_collage import Collage
from ...MinecraftBehaviorPacks.minecraft_behavior_pack import MinecraftBehaviorPack
from ...MinecraftFunctions.minecraft_function.minecraft_function import MinecraftFunction
from ...MinecraftResourcePacks.minecraft_resource_pack import MinecraftResourcePack

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
    def __init__(self, behavior_pack):
        super().__init__('family_collage', behavior_pack)
    def build(self):
        pass
    def create_function(self, function_to_run):
        self.run('function {}'.format(function_to_run))

class FamilyCollage():
    x_position = None
    behavior_pack = None
    resource_pack = None
    def __init__(self) -> None:
        self.x_position = 0
        self.behavior_pack = CollageBehaviorPack()
        self.resource_pack = CollagResourcePack()

        self.collage_function = FamilyCollageFunction(self.behavior_pack)
        self.collage_function.run('function reset_build')
        self.create_linear_collages()

        self.collage_function.run_all()

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

        self.collage_function.create_function(namespace)

        return collage

