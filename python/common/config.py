import os

BEHAVIOR_PACK_ROOT_DIR = 'minecraft_behavior_packs'
DATA_PACK_ROOT_DIR = 'minecraft_data_packs'

BEHAVIOR_PACK_DEFAULT_NAME = 'first_behavior_pack'
BEHAVIOR_PACK_TEMPLATE_NAME = 'basic_behavior_pack'
BEHAVIOR_PACK_TEMPLATE_DIR = os.path.join(BEHAVIOR_PACK_ROOT_DIR, BEHAVIOR_PACK_TEMPLATE_NAME)

DATA_PACK_TEMPLATE_NAME = 'template_data_pack'
DATA_PACK_TEMPLATE_DIR = os.path.join(DATA_PACK_ROOT_DIR, DATA_PACK_TEMPLATE_NAME)

def get_behavior_pack_functions_dir(behavior_pack_name:str = BEHAVIOR_PACK_DEFAULT_NAME):
    return os.path.join(BEHAVIOR_PACK_ROOT_DIR, behavior_pack_name, 'functions')
