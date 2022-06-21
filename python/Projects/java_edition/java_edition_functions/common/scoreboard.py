DEFAULT_SCOREBOARD_TARGETS = '@a'
DEFAULT_SCORBOARD_STARTING_SCORE = 0
DEFAULT_SCOREBOARD_SCORE_INCREMENT = 1


class Scoreboard():
    name = None
    targets = None
    increment_by = None
    starting_score = None
    def __init__(self, name: str, targets = DEFAULT_SCOREBOARD_TARGETS, starting_score = DEFAULT_SCORBOARD_STARTING_SCORE, increment_by = DEFAULT_SCOREBOARD_SCORE_INCREMENT) -> None:
        self.name = name
        self.targets = targets
        self.starting_score = starting_score
        self.increment_by = increment_by
    
    def initialize_players(self) -> str:
        return 'scoreboard players set {} {} {}'.format(self.targets, self.name, self.starting_score)
