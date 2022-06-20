from ...MinecraftAddons.MinecraftDataPacks.minecraft_data_pack import MinecraftDataPack
from .java_edition_functions.armour_stand import ArmourStand
from .java_edition_functions.forever_village import ForeverVillage
from .java_edition_functions.dancing_armour_stand import DancingArmourStand

DATA_PACK_NAME = 'java_default'
DATA_PACK_DESCRIPTION = 'java data pack for misc implementations'

class JavaEditionPack():
    data_pack = None
    def __init__(self) -> None:
        self.data_pack = MinecraftDataPack(DATA_PACK_NAME, pack_description=DATA_PACK_DESCRIPTION)
        self.run_functions()
    
    def run_functions(self):
        ArmourStand(self.data_pack).run_all()
        DancingArmourStand(self.data_pack).run_all()
        ForeverVillage(self.data_pack).run_all()