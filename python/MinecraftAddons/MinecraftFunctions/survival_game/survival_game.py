from .level1.start import SurvivalGameLevel1Start
from .level1.end import SurvivalGameLevel1End
from .level2.start import SurvivalGameLevel2Start
from .level2.end import SurvivalGameLevel2End
from .level3.start import SurvivalGameLevel3Start
from .level3.end import SurvivalGameLevel3End
from .level4.start import SurvivalGameLevel4Start
from .level4.end import SurvivalGameLevel4End
from .level5.start import SurvivalGameLevel5Start
from .level5.end import SurvivalGameLevel5End

class SurvivalGame():
    functions = []
    def __init__(self) -> None:
        self.functions = [
            SurvivalGameLevel1Start(),
            SurvivalGameLevel1End(),
            SurvivalGameLevel2Start(),
            SurvivalGameLevel2End(),
            SurvivalGameLevel3Start(),
            SurvivalGameLevel3End(),
            SurvivalGameLevel4Start(),
            SurvivalGameLevel4End(),
            SurvivalGameLevel5Start(),
            SurvivalGameLevel5End(),
        ]

        for function in self.functions:
            function.run_all()
