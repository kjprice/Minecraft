import os
import shutil

from ..common.json_helper import read_json, write_json

class MinecraftAddon():
    destination_filepath = None
    template_path = None
    def __init__(self, destination_filepath, template_path) -> None:
        self.destination_filepath = destination_filepath
        self.template_path = template_path
    
    def create(self):
        shutil.rmtree(self.destination_filepath)
        shutil.copytree(self.template_path, self.destination_filepath, dirs_exist_ok=True)

    # Can be overridden for additional configuration
    def configure(self):
        pass

    def read_json(self, filename: str) -> object:
        filepath = os.path.join(self.destination_filepath, filename)
        return read_json(filepath)

    def write_json(self, filename: str, data: object) -> None:
        filepath = os.path.join(self.destination_filepath, filename)
        return write_json(filepath, data)
