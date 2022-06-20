import os

from ...common.config import DATA_PACK_ROOT_DIR, DATA_PACK_TEMPLATE_DIR
from ..minecraft_addon import MinecraftAddon

DEFAULT_DATA_PACK_DESCRIPTION = 'Just Another Data Pack'
PACK_METADATA_FILENAME = 'pack.mcmeta'

class MinecraftDataPack(MinecraftAddon):
    folder_name = None
    pack_description = None
    def __init__(self, pack_name, pack_description = DEFAULT_DATA_PACK_DESCRIPTION) -> None:
        self.folder_name = '{}_data_pack'.format(pack_name)
        self.pack_description = pack_description

        filepath = os.path.join(DATA_PACK_ROOT_DIR, self.folder_name)
        super().__init__(filepath, DATA_PACK_TEMPLATE_DIR)

    def configure(self):
        self.set_pack_meta()

    def set_pack_meta(self):
        pack_meta = self.read_json(PACK_METADATA_FILENAME)
        pack_meta['pack']['description'] = self.pack_description
        self.write_json(PACK_METADATA_FILENAME, pack_meta)

