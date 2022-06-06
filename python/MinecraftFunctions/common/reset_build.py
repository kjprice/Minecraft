from ..minecraft_function.minecraft_function import MinecraftFunction
from .fill_air import fill_air
from .build_around_player import build_around_player
def reset_build():
    output = []
    output.append('# Filling with Grass')
    output.append(build_around_player(50, block='grass'))
    output.append(fill_air(y_bottom=1))
    output.append('')
    return '\n'.join(output)

class ResetBuild(MinecraftFunction):
    def __init__(self):
        super().__init__('reset_build')
    def build(self):
        return self.run(reset_build())
