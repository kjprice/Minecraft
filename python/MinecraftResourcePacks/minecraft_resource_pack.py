import os
import shutil
from typing import List

import cv2
from numpy import block

from ..common.json_helper import read_json, write_json

class MinecraftResourcePack():
    ROOT_DIR = 'minecraft_resource_packs'
    TEMPLATE_DIR = os.path.join(ROOT_DIR, 'basic_resource_pack')
    filepath = None
    pack_name = None
    output = None
    resource_pack_folder_name = None
    uuids = None
    def __init__(self, pack_name: str, uuids: List[str]) -> None:
        self.output = []
        self.pack_name = pack_name
        self.resource_pack_folder_name = '{}_resource_pack'.format(pack_name)
        self.filepath = os.path.join(self.ROOT_DIR, self.resource_pack_folder_name)
        self.uuids = uuids
        self.create_resource_pack_from_template()
    def create_resource_pack_from_template(self):
        shutil.rmtree(self.filepath)
        shutil.copytree(self.TEMPLATE_DIR, self.filepath, dirs_exist_ok=True)
        # print(os.listdir(self.filepath))
        self.set_uuids()
    def set_uuids(self):
        # TODO(kjprice): Set description and other things too
        manifest = self.read_json('manifest.json')
        manifest['header']['uuid'] = self.uuids[0]
        self.write_json('manifest.json', manifest)
    def read_json(self, filename: str) -> object:
        filepath = os.path.join(self.filepath, filename)
        return read_json(filepath)
    def write_json(self, filename: str, data: object) -> None:
        filepath = os.path.join(self.filepath, filename)
        return write_json(filepath, data)
    @property
    def block_texture_filepath(self):
        return os.path.join(self.filepath, 'textures', 'blocks')
    def save_block(self, img_array, namespace, block_name):
        self.save_block_image(img_array, block_name)
        self.add_terrain_texture(block_name)
        self.add_block_data(namespace, block_name)
        # TODO(kjprice): Add namespace to language
        self.add_language(block_name)
    
    def add_language(self, block_name):
        language_filepath = os.path.join(self.filepath, 'texts', 'en_US.lang')
        with open(language_filepath, 'a') as f:
            f.write('tile.{}.name=Custom Block\n'.format(block_name))

    def add_terrain_texture(self, block_name):
        terrain_textures_filepath = os.path.join('textures', 'terrain_texture.json')
        terrain_textures = self.read_json(terrain_textures_filepath)
        block_filepath = 'textures/blocks/{}.png'.format(block_name)
        terrain_textures['texture_data'][block_name] = {
            'textures': block_filepath
        }
        self.write_json(terrain_textures_filepath, terrain_textures)
    def add_block_data(self, namespace, block_name):
        block_with_namespace = '{}:{}'.format(namespace, block_name)
        blocks_data = self.read_json('blocks.json')
        blocks_data[block_with_namespace] = {
            "sound": "dirt",
            'textures': block_name
        }
        self.write_json('blocks.json', blocks_data)
    def save_block_image(self, img_array, block_name):
        filename='{}.png'.format(block_name)
        filepath = os.path.join(self.block_texture_filepath, filename)
        cv2.imwrite(filepath, img_array)

