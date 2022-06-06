from .reset_build import reset_build
from .build_around_player import build_around_player
def build_lava_trap():
    output = []
    output.append(reset_build())
    output.append(build_around_player(10, block='lava'))
    return '\n'.join(output)
# build_lava_trap()