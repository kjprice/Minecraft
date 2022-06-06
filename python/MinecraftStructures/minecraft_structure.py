import os

from ..common.tools import ensure_directory_exists
from ..common.config import BEHAVIOR_PACK_ROOT_DIR

def create_template_filepath(structure_name: str):
    filename = '{}_template.mcstructure'.format(structure_name)
    return os.path.join('minecraft_structures', filename)

def load_template(name: str):
    with open(create_template_filepath(name), 'rb') as f:
        return f.read()

class MinecraftCommandBlockStructure():
    # Globals
    TEMPLATE_COMMAND = 'say hi'
    TEMPLATE_AUTO = 'auto'
    STRUCTURE_TAGS = [TEMPLATE_COMMAND, TEMPLATE_AUTO]

    # User provided
    name = None
    behavior_pack_dir = os.path.join(BEHAVIOR_PACK_ROOT_DIR, 'first_behavior_pack')

    # For structure
    structure_raw = None
    structure_array = None
    structure_tag_positions = {}
    def __init__(self, name: str, cmd: str, auto_run=False, behavior_pack = None) -> None:
        self.name = name
        self.structure_raw = self.load()
        if behavior_pack is not None:
            self.behavior_pack_dir = behavior_pack.filepath


        self.create_structure_array()
        self.implode_structure_array()
        self.find_structure_tags()

        self.set_structure_command(cmd)
        self.set_structure_auto_run(auto_run)
        self.save_structure()
    
    def save_structure(self):
        name = self.name
        structure_text = self.implode_structure_array()
        structure_dir = os.path.join(self.behavior_pack_dir, 'structures')
        ensure_directory_exists(structure_dir)
        filename = '{}.mcstructure'.format(name)
        filepath = os.path.join(structure_dir, filename)
        with open(filepath, 'wb') as f:
            return f.write(structure_text)


    def save_structure_array(self):
        text_list = []
        for s in self.structure_array:
            text_list.append(str(s))
        text = '\n'.join(text_list)
        with open('structure_array.txt', 'w') as f:
            f.write(text)
    
    def get_command_for_function(self, x = 0, y = 0, z = 0):
        return 'structure load {} ~{} ~{} ~{}'.format(self.name, x, y, z)

    def create_structure_array(self):
        structure_bytes = []
        # Turns bytes into characters when could be text
        for s in self.structure_raw:
            if s >= 32 and s <= 122:
                s = chr(s)
            structure_bytes.append(s)
        
        # Groups text together into words
        structure_bytes_and_words = []
        current_word = ""
        for s in structure_bytes:
            if type(s) is str:
                current_word += s
            else:
                if current_word != "":
                    structure_bytes_and_words.append(current_word)
                    current_word = ""
                structure_bytes_and_words.append(s)
        if current_word:
            structure_bytes_and_words.append(s)

        self.structure_array = structure_bytes_and_words

    def find_structure_tags(self):
        # Sets the position of found tag names
        for i, s in enumerate(self.structure_array):
            if s in self.STRUCTURE_TAGS:
                self.structure_tag_positions[s] = i
        

    def implode_structure_array(self):
        # Takes the array structure, turns all words into bytes, returns just bytes
        output = []
        for s in self.structure_array:
            if type(s) == int:
                output.append(s)
            else:
                for c in s:
                    output.append(ord(c))
        return bytearray(output)

    def load(self):
       return load_template("command_block")
    
    def replace_text(self, from_text, to_text):
        self.structure_raw = self.structure_raw.replace(from_text, to_text)
    
    def set_structure_tag(self, tag_name, value):
        tag_position = self.structure_tag_positions[tag_name]
        self.structure_array[tag_position] = value

        tag_position_text_length = tag_position - 2
        self.structure_array[tag_position_text_length] = len(value)
        # print(self.structure_array[130:145])

    def set_structure_command(self, command: str):
        tag_position = self.structure_tag_positions[self.TEMPLATE_COMMAND]
        self.structure_array[tag_position] = command

        tag_position_text_length = tag_position - 2
        self.structure_array[tag_position_text_length] = len(command)
        # self.set_structure_tag(self.TEMPLATE_COMMAND, command)

    def set_structure_auto_run(self, auto_run):
        tag_position = self.structure_tag_positions[self.TEMPLATE_AUTO]
        self.structure_array[tag_position + 1] = 1 if auto_run else 0

a = MinecraftCommandBlockStructure("give_dirt", "give @p command_block", True)
# print(a.get_command_for_function())
# a.save_structure_array()
#  print(a.structure_array)

