import os
import shutil
from typing import List

from ..common.json_helper import read_json, write_json

class MinecraftBehaviorPack():
    ROOT_DIR = 'minecraft_behavior_packs'
    TEMPLATE_DIR = os.path.join(ROOT_DIR, 'basic_behavior_pack')
    filepath = None
    pack_name = None
    output = None
    behavior_pack_folder_name = None
    uuids = None
    def __init__(self, pack_name: str, uuids: List[str]) -> None:
        self.output = []
        self.pack_name = pack_name
        self.behavior_pack_folder_name = '{}_behavior_pack'.format(pack_name)
        self.filepath = os.path.join(self.ROOT_DIR, self.behavior_pack_folder_name)
        self.uuids = uuids
        self.create_behavior_pack_from_template()
    def create_behavior_pack_from_template(self):
        shutil.rmtree(self.filepath)
        shutil.copytree(self.TEMPLATE_DIR, self.filepath, dirs_exist_ok=True)
        # print(os.listdir(self.filepath))
        self.set_manifest()
    def set_manifest(self):
        # TODO(kjprice): Set description and other things to manifest
        manifest = self.read_json('manifest.json')
        manifest['header']['uuid'] = self.uuids[0]
        manifest['dependencies'][0]['uuid'] = self.uuids[1]
        self.write_json('manifest.json', manifest)
    def read_json(self, filename: str) -> object:
        filepath = os.path.join(self.filepath, filename)
        return read_json(filepath)
    def write_json(self, filename: str, data: object) -> None:
        filepath = os.path.join(self.filepath, filename)
        return write_json(filepath, data)
    def save_block(self, namespace, block_name):
        # TODO:
        # - blocks/{name}.json
        block_with_namespace = '{}:{}'.format(namespace, block_name)
        block_data = self.read_json(os.path.join('blocks', 'canvasblock.json'))
        block_data['minecraft:block']['description']['identifier'] = block_with_namespace
        self.write_json(os.path.join('blocks', '{}.json'.format(block_name)), block_data)
    # def save_function(self, function_name, function_contents):
    #     filepath_dir = os.path.join(self.filepath, 'functions')
    #     # os.makedirs(filepath_dir)
    #     filepath = os.path.join(filepath_dir, '{}.mcfunction'.format(function_name))
    #     with open(filepath, 'w') as f:
    #         f.write(function_contents)

