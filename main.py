from scripts.mind import MindThread
from ui.Home import *
from utils.check_file import Check
from flet import app as runApp

def initialize():
    Check.init()


if __name__ == '__main__':
    # mind = MindThread(title="AI")
    # mind.start()

    # -----------------------------
    initialize()
    runApp(
        target=Home.init,
        assets_dir="assets"
    )