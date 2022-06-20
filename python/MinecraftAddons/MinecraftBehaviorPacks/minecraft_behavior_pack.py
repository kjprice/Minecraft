import os
import shutil
from typing import List

from ...common.config import BEHAVIOR_PACK_ROOT_DIR, BEHAVIOR_PACK_TEMPLATE_DIR
from ..minecraft_addon import MinecraftAddon

class MinecraftBehaviorPack(MinecraftAddon):
    filepath = None
    pack_name = None
    output = None
    behavior_pack_folder_name = None
    uuids = None
    root_dir = BEHAVIOR_PACK_ROOT_DIR
    def __init__(self, pack_name: str, uuids: List[str]) -> None:
        self.output = []
        self.pack_name = pack_name
        self.behavior_pack_folder_name = '{}_behavior_pack'.format(pack_name)
        filepath = os.path.join(BEHAVIOR_PACK_ROOT_DIR, self.behavior_pack_folder_name)
        self.uuids = uuids
        super().__init__(filepath, BEHAVIOR_PACK_TEMPLATE_DIR)
    
    # Override method
    def configure(self):
        self.set_manifest()

    def set_manifest(self):
        # TODO(kjprice): Set description and other things to manifest
        manifest = self.read_json('manifest.json')
        manifest['header']['uuid'] = self.uuids[0]
        manifest['dependencies'][0]['uuid'] = self.uuids[1]
        self.write_json('manifest.json', manifest)

    def save_block(self, namespace, block_name):
        # TODO:
        # - blocks/{name}.json
        block_with_namespace = '{}:{}'.format(namespace, block_name)
        block_data = self.read_json(os.path.join('blocks', 'canvasblock.json'))
        block_data['minecraft:block']['description']['identifier'] = block_with_namespace
        self.write_json(os.path.join('blocks', '{}.json'.format(block_name)), block_data)
