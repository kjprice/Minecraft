from ..minecraft_function.minecraft_function import MinecraftFunction

class MusicNotes(MinecraftFunction):
    def __init__(self):
        super().__init__('music/music_notes')
    def build(self):
        # TODO:
        # - Create a scoreboard if not exists
        # - Continuously runs function, incrementing score
        # - Finds notes to play for each score
        # - Run using a repeating command block

        self.run('')
    def run(self, output):
        self.output.append(output)
