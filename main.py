from ui.Home import *
from utils.check_file import Check
from flet import app as runApp

def initialize():
    Check.init()

    try:
        from scripts.training_model import TrainingModel
        TrainingModel.load()
    except:
        ...


if __name__ == '__main__':
    initialize()
    # -----------------------------
    runApp(
        target=Home.init,
        assets_dir="assets"
    )