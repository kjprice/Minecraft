from .survival_game.survival_game import SurvivalGame
from .common.fill_air import FillAir
from .common.reset_build import ResetBuild, ResetBuildMassive
from .powers.equip_netherite import EquipNetherite
from .clear.replace_unwanted import ReplaceUnwanted

def create_all():
    survivalGame = SurvivalGame()
    FillAir().run_all()
    ResetBuild().run_all()
    ResetBuildMassive().run_all()
    EquipNetherite().run_all()
    ReplaceUnwanted().run_all()

if __name__ == '__main__':
    create_all()